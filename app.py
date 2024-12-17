import streamlit as st
from statsbombpy import sb
import pandas as pd
from mplsoccer import Pitch
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt

# Configuración de Streamlit
st.set_page_config(
    layout="wide", 
    page_title="Análisis de Datos de Fútbol",
    page_icon="⚽")
    
st.title("⚽ Visualización de Datos de Fútbol con StatsBomb")

# Paso 1: Cargar competiciones disponibles
st.sidebar.header("Selecciona Competición y Temporada")
free_comps = sb.competitions()
if not free_comps.empty:
    competition_options = free_comps[["competition_name", "season_name", "competition_id", "season_id"]]
    selected_competition = st.sidebar.selectbox(
        "Competición:",
        competition_options["competition_name"].unique()
    )

    # Filtrar temporadas disponibles
    competition_id = competition_options.loc[competition_options["competition_name"] == selected_competition, "competition_id"].values[0]
    seasons = competition_options[competition_options["competition_name"] == selected_competition]
    selected_season = st.sidebar.selectbox("Temporada:", seasons["season_name"].unique())
    season_id = seasons.loc[seasons["season_name"] == selected_season, "season_id"].values[0]

    # Paso 2: Cargar partidos
    st.sidebar.header("Selecciona Partido")
    mundial_matches = sb.matches(competition_id=competition_id, season_id=season_id)
    match_options = mundial_matches[["home_team", "away_team", "match_id"]]
    match_options["match_name"] = match_options["home_team"] + " vs " + match_options["away_team"]
    selected_match = st.sidebar.selectbox("Partido:", match_options["match_name"])
    match_id = match_options.loc[match_options["match_name"] == selected_match, "match_id"].values[0]

    # Paso 3: Cargar eventos del partido
    events = sb.events(match_id=match_id)

    if not events.empty:
        st.write(f"Análisis de eventos para el partido: **{selected_match}**")
        
        # Crear pestañas
        tab1, tab2, tab3, tab4 = st.tabs([
            "Análisis de Pases", 
            "Análisis Defensivo", 
            "Análisis de Tiros", 
            "Rendimiento Individual"
        ])

        with tab1:
            # Filtrar pases
            passes = events[events["type"] == "Pass"].copy()
            if not passes.empty:
                passes[["x", "y"]] = passes["location"].apply(pd.Series)
                passes[["pass_end_x", "pass_end_y"]] = passes["pass_end_location"].apply(pd.Series)

                # Filtrar pases por equipo
                team_options = passes["team"].unique()
                selected_team = st.selectbox("Selecciona Equipo:", team_options)
                team_passes = passes[passes["team"] == selected_team]

                if not team_passes.empty:
                    # Visualizar pases en un campo de fútbol
                    st.subheader(f"Pases del equipo: {selected_team}")
                    player_options = team_passes["player"].unique()
                    selected_player = st.selectbox("Selecciona Jugador:", player_options)

                    player_passes = team_passes[team_passes["player"] == selected_player]

                    if not player_passes.empty:
                        # Configuración de colores
                        white = "white"
                        sbred = "#e21017"
                        darkgrey = "#9A9A9A"
                        cmaplist = [white, darkgrey, sbred]
                        cmap = LinearSegmentedColormap.from_list("", cmaplist)

                        # Dibujar campo
                        pitch = Pitch(pitch_type="statsbomb", pitch_color="white", line_color="black")
                        fig, ax = pitch.draw(figsize=(10, 7))
                        fig.set_facecolor(white)

                        # Graficar pases
                        pitch.arrows(
                            player_passes["x"], player_passes["y"],
                            player_passes["pass_end_x"], player_passes["pass_end_y"],
                            width=2, headwidth=6, headlength=5, color=sbred, ax=ax
                        )
                        st.pyplot(fig)

                    else:
                        st.warning("No hay datos de pases para este jugador.")
                else:
                    st.warning("No hay datos de pases para este equipo.")
            else:
                st.warning("No hay datos de pases en este partido.")

        with tab2:
            # Análisis de Presión y Recuperaciones
            st.header("🏆 Análisis Defensivo")

            # Filtrar eventos de presión y recuperación
            pressure_events = events[(events["type"] == "Pressure") | (events["type"] == "Ball Recovery")]
            if not pressure_events.empty:
                # Crear métricas de presión por equipo
                pressure_stats = pressure_events.groupby("team").agg({
                    "type": "count"
                }).rename(columns={"type": "Total Acciones Defensivas"})
                
                st.subheader("Métricas de Presión Defensiva")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.dataframe(pressure_stats)
                
                with col2:
                    # Gráfico circular de acciones defensivas
                    fig, ax = plt.subplots()
                    pressure_stats.plot(kind='pie', y='Total Acciones Defensivas', autopct='%1.1f%%', ax=ax)
                    ax.set_title("Distribución de Acciones Defensivas")
                    st.pyplot(fig)
                
                # Mapa de calor de presión
                st.subheader("Mapa de Calor de Presión Defensiva")
                team_pressure = pressure_events[pressure_events["location"].notna()]
                team_pressure[["x", "y"]] = team_pressure["location"].apply(pd.Series)
                
                pitch = Pitch(pitch_type="statsbomb", pitch_color="white", line_color="black")
                fig, ax = pitch.draw(figsize=(10, 7))
                
                for team in pressure_events["team"].unique():
                    team_data = team_pressure[team_pressure["team"] == team]
                    pitch.kdeplot(
                        team_data["x"], team_data["y"], 
                        ax=ax, 
                        cmap='Blues', 
                        shade=True, 
                        levels=20
                    )
                
                st.pyplot(fig)
            else:
                st.warning("No hay eventos de presión o recuperación disponibles.")

        with tab3:
            # Análisis de Tiros y Expected Goals (xG)
            st.header("⚽ Análisis de Tiros y Expected Goals")

            # Filtrar eventos de tiro
            shots = events[events["type"] == "Shot"]
            if not shots.empty:
                # Métricas de tiros
                shot_stats = shots.groupby("team").agg({
                    "type": "count",
                    "shot_outcome": lambda x: (x == "Goal").sum(),
                    "shot_statsbomb_xg": "sum"
                }).rename(columns={
                    "type": "Total Tiros",
                    "shot_outcome": "Goles",
                    "shot_statsbomb_xg": "Expected Goals (xG)"
                })
                
                st.subheader("Resumen de Tiros")
                st.dataframe(shot_stats)
                
                # Visualización de tiros
                st.subheader("Ubicación de Tiros")
                shots[["x", "y"]] = shots["location"].apply(pd.Series)
                
                pitch = Pitch(pitch_type="statsbomb", pitch_color="white", line_color="black")
                fig, ax = pitch.draw(figsize=(10, 7))
                
                for team in shots["team"].unique():
                    team_shots = shots[shots["team"] == team]
                    scatter = pitch.scatter(
                        team_shots["x"], team_shots["y"], 
                        c=team_shots["shot_statsbomb_xg"],  # Color basado en xG
                        cmap='viridis', 
                        ax=ax, 
                        s=team_shots["shot_statsbomb_xg"] * 200,  # Tamaño basado en xG
                        alpha=0.7
                    )
                
                plt.colorbar(scatter, ax=ax, label='Expected Goals (xG)')
                st.pyplot(fig)
            else:
                st.warning("No hay datos de tiros disponibles.")

        with tab4:
            # Análisis Interactivo de Jugadores
            st.header("Análisis de Rendimiento Individual")

            # Selección de jugadores
            player_stats = {}
            for team in events["team"].unique():
                team_events = events[events["team"] == team]
                team_players = team_events["player"].unique()
                
                st.subheader(f"Jugadores de {team}")
                selected_player = st.selectbox(f"Selecciona un jugador de {team}", team_players, key=team)
                
                # Calcular estadísticas del jugador
                player_events = team_events[team_events["player"] == selected_player]
                
                player_stats[selected_player] = {
                    "Total Eventos": len(player_events),
                    "Pases": len(player_events[player_events["type"] == "Pass"]),
                    "Tiros": len(player_events[player_events["type"] == "Shot"]),
                    "Recepciones": len(player_events[player_events["type"] == "Pass Reception"]),
                    "Presiones": len(player_events[player_events["type"] == "Pressure"])
                }

            # Mostrar estadísticas de jugadores
            if player_stats:
                player_df = pd.DataFrame.from_dict(player_stats, orient='index')
                st.dataframe(player_df)

    else:
        st.warning("No hay eventos disponibles para este partido.")
else:
    st.warning("No hay competiciones disponibles.")