# ⚽ Visualizador de Datos de Fútbol con StatsBomb

Esta aplicación web, desarrollada con Streamlit, permite visualizar y analizar datos de fútbol utilizando la API de StatsBomb. La aplicación ofrece un análisis completo y detallado de partidos de fútbol, con múltiples visualizaciones y estadísticas.

## 📋 Características Principales

- Visualización interactiva de pases por jugador y equipo
- Análisis defensivo con mapas de calor de presión
- Estadísticas detalladas de tiros y Expected Goals (xG)
- Análisis del rendimiento individual de jugadores
- Interfaz intuitiva para selección de competiciones, temporadas y partidos

## 🛠️ Tecnologías Utilizadas

- Python 3.x
- Streamlit
- statsbombpy
- pandas
- matplotlib
- mplsoccer

## 🏗️ Estructura de la Aplicación

### 1. Configuración Inicial
```

### 2. Selección de Datos
- Carga de competiciones disponibles
- Filtrado de temporadas
- Selección de partidos específicos

### 3. Análisis por Pestañas

#### 📊 Pestaña 1: Análisis de Pases
- Visualización de pases por equipo y jugador
- Mapa del campo con flechas indicando dirección de pases
- Filtros interactivos por equipo y jugador

#### 🛡️ Pestaña 2: Análisis Defensivo
- Métricas de presión defensiva
- Gráficos circulares de acciones defensivas
- Mapas de calor de presión

#### ⚽ Pestaña 3: Análisis de Tiros
- Estadísticas de tiros y goles
- Visualización de Expected Goals (xG)
- Mapas de ubicación de tiros

#### 👤 Pestaña 4: Rendimiento Individual
- Estadísticas detalladas por jugador
- Métricas individuales de rendimiento
- Comparación entre jugadores

## 📦 Requisitos de Instalación
```

## 🚀 Cómo Ejecutar la Aplicación

1. Clona el repositorio
2. Instala las dependencias
3. Ejecuta la aplicación:
```bash
streamlit run app.py
```

## 📊 Funcionalidades Detalladas

### Análisis de Pases
- Visualización de patrones de pase
- Filtrado por equipo y jugador
- Representación gráfica en campo de fútbol

### Análisis Defensivo
- Tracking de presión y recuperaciones
- Estadísticas defensivas por equipo
- Mapas de calor de actividad defensiva

### Análisis de Tiros
- Métricas de eficiencia de tiro
- Cálculo de Expected Goals (xG)
- Visualización espacial de tiros

### Rendimiento Individual
- Estadísticas completas por jugador
- Métricas de participación en el juego
- Comparativas entre jugadores

## 🔍 Procesamiento de Datos

La aplicación utiliza la API de StatsBomb para:
- Cargar datos de competiciones
- Procesar eventos de partidos
- Calcular estadísticas avanzadas
- Generar visualizaciones interactivas

## 📈 Visualizaciones

- Mapas de calor
- Gráficos de pases
- Diagramas de tiros
- Estadísticas tabulares
- Gráficos circulares

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de crear un pull request.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.
```