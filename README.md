# ⚽ Visualizador de Datos de Fútbol con StatsBomb

Esta aplicación web, desarrollada con **Streamlit**, permite visualizar y analizar datos de fútbol mediante la API de **StatsBomb**. Ofrece análisis interactivos y visualizaciones avanzadas para partidos, jugadores y equipos.

---

## 📋 Características Principales

- **Visualización interactiva** de pases por jugador y equipo
- **Análisis defensivo** con mapas de calor de presión y métricas
- Estadísticas detalladas de **tiros** y **Expected Goals (xG)**
- **Análisis de rendimiento individual** de jugadores
- Interfaz intuitiva para seleccionar competiciones, temporadas y partidos

---

## 🛠️ Tecnologías Utilizadas

| Tecnología        | Descripción                              |
|-------------------|------------------------------------------|
| **Python 3.x**    | Lenguaje principal para el backend       |
| **Streamlit**     | Framework para aplicaciones web interactivas |
| **statsbombpy**   | Biblioteca para acceder a la API de StatsBomb |
| **pandas**        | Manipulación y análisis de datos         |
| **matplotlib**    | Generación de gráficos y visualizaciones |
| **mplsoccer**     | Visualización de datos específicos de fútbol |

---

## 🏗️ Estructura de la Aplicación

### 1️⃣ Configuración Inicial
- Conexión con la API de StatsBomb
- Instalación de dependencias y configuración del entorno

### 2️⃣ Selección de Datos
- **Carga dinámica** de competiciones disponibles
- Filtrado interactivo por **temporada** y **partido específico**

### 3️⃣ Análisis por Pestañas

#### 📊 Análisis de Pases
- Visualización de patrones de pases en el campo
- Filtros interactivos por equipo y jugador
- Mapas del campo con flechas que indican la **dirección y frecuencia** de pases

#### 🛡️ Análisis Defensivo
- Métricas y gráficos de **presión defensiva**
- Mapas de calor de **recuperaciones y actividad defensiva**
- Estadísticas por equipo y jugador

#### ⚽ Análisis de Tiros
- Visualización de **Expected Goals (xG)**
- Mapas interactivos de ubicación de tiros y goles
- Métricas de eficiencia y efectividad en el ataque

#### 👤 Rendimiento Individual
- Estadísticas avanzadas por jugador
- Métricas de participación ofensiva y defensiva
- Comparativas entre jugadores seleccionados

---

## 📦 Requisitos de Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/mplatab/analisis_soccer.git
   cd analisis_soccer
   ```

2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```

## 🚀 Cómo Ejecutar la Aplicación

1. Descarga o clona el repositorio
2. Instala las dependencias utilizando requirements.txt
3. Lanza la aplicación con el siguiente comando:
   ```bash
   streamlit run app.py
   ```
4. Accede a la interfaz a través del navegador en:
   `http://localhost:8501`

## 📈 Visualizaciones Incluidas

- Mapas de calor (presión defensiva y actividad)
- Gráficos de pases (dirección y frecuencia)
- Diagramas de tiros (xG y ubicación de tiros)
- Estadísticas tabulares con filtros dinámicos
- Gráficos circulares de acciones defensivas

## 🔍 Procesamiento de Datos

La aplicación realiza las siguientes tareas con la API de StatsBomb:

- Carga de datos de competiciones y eventos
- Procesamiento y filtrado de información específica
- Cálculo de métricas avanzadas como xG y presión
- Generación de visualizaciones interactivas en tiempo real

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para proponer cambios:

1. Abre un issue para discutir tus ideas
2. Realiza un fork del repositorio
3. Envía un Pull Request con tus mejoras