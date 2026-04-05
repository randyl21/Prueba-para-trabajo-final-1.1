# Importación de librerías necesarias
import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuración de página
st.set_page_config(
    page_title="Dashboard prueba del tf",
    page_icon="📊",
    layout="wide"
)

# 2. Caché y carga de datos
@st.cache_data
def cargar_datos():
    # Usamos el archivo de referencia de Oliver
    df_Online_Gaming = pd.read_csv("Dataset/17. Online Gaming.csv")

    return df_Online_Gaming

df_Online_Gaming = cargar_datos()

    # 3. Título principal
st.title("Prueba del tf")
st.markdown("insertar titulo del tf xdxd **Streamlit** y **Plotly**.")

# 4. Configuración de la Barra Lateral (Sidebar)
st.sidebar.header("Filtros de Búsqueda")

# Lista de ciudades únicas para el filtro
Locaciones_disponibles = df_Online_Gaming ['Location'].unique()
Locaciones_seleccionadas = st.sidebar.multiselect(
    "Selecciona Locaciones", 
    options=Locaciones_disponibles, 
    default=Locaciones_disponibles[:5] # Por defecto 5 ciudades
)