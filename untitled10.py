import streamlit as st
import base64
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Cargar el dataset
pf = pd.read_csv("spotify_songs_dataset.csv")
image_path = "fondo_morado.png"  

# Codificar la imagen en base64
with open(image_path, "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode()

# Aplicar estilo de fondo a la aplicación
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{base64_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Configuración inicial para la página y subpágina actual
if "page" not in st.session_state:
    st.session_state.page = "inicio"

if "subpage" not in st.session_state:
    st.session_state.subpage = None

# Función para cambiar la página principal
def cambiar_pagina(nueva_pagina):
    st.session_state.page = nueva_pagina
    if nueva_pagina != "categoría_2":
        st.session_state.subpage = None  # Resetear la subpágina solo si no estamos en "categoría_2"

# Función para cambiar la subpágina dentro de "Tipos"
def cambiar_subpagina(nueva_subpagina):
    st.session_state.subpage = nueva_subpagina

# Título de la aplicación
st.title("Aplicación Genérica")

# Mostrar botones solo si estamos en la página de inicio
if st.session_state.page == "inicio":
    st.header("Seleccione una opción")
    
    # Utilizar columnas para alinear los botones horizontalmente
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Opción 1"):
            cambiar_pagina("categoría_1")
    with col2:
        if st.button("Opción 2"):
            cambiar_pagina("categoría_2")
    
    with col3:
        if st.button("Opción 3"):
            cambiar_pagina("categoría_3")

# Mostrar contenido según la página seleccionada
elif st.session_state.page == "categoría_1":
    st.header("Contenido de Opción 1")
    st.write("Aquí se mostrarán los datos relacionados con la Opción 1.")
    st.write(pf)
    
    if st.button("Volver atrás"):
        cambiar_pagina("inicio")

elif st.session_state.page == "categoría_2":
    # Manejar las subpáginas de la categoría "Opción 2"
    if st.session_state.subpage is None:
        st.header("Seleccione una subcategoría")
        
        # Mostrar botones para las subcategorías
        if st.button("Grafico De contenido Explicito"):
            cambiar_subpagina("subcategoria_a")

        if st.button("Distribucion de idioma de canciones"):
            cambiar_subpagina("subcategoria_b")  
        if st.button("Tendencia De lanzamiento de canciones"):
            cambiar_subpagina("subcategoria_c")
        if st.button("Duración Promedio por Género"):
            cambiar_subpagina("subcategoria_d")
        if st.button("Subcategoría E"):
            cambiar_subpagina("subcategoria_e")
        
        if st.button("Volver atrás"):
            cambiar_pagina("inicio")
    
    # Manejo de subpáginas específicas
    else:
        if st.session_state.subpage == "subcategoria_a":
            st.header("Subcategoría A")
            st.write("Aquí se mostrarán los datos de la Subcategoría A.")
            data_filtrada = pf.dropna(subset=['genre', 'explicit_content'])
            contenido_explicito = data_filtrada.groupby(['genre', 'explicit_content']).size().unstack(fill_value=0)
            
            fig, ax = plt.subplots(figsize=(12, 8))
            contenido_explicito.plot(kind='bar', stacked=True, ax=ax)
            ax.set_title('Proporción de Canciones con Contenido Explícito por Género')
            ax.set_xlabel('Género')
            ax.set_ylabel('Número de Canciones')
            ax.legend(title='Contenido Explícito', labels=['No', 'Sí'])
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig)
            
        elif st.session_state.subpage == "subcategoria_b":
            st.header("Subcategoría B")
            st.write("Aquí se mostrarán los datos de la Subcategoría B.")
            contador_lenguaje = pf["language"].value_counts()
            fig, ax = plt.subplots(figsize=(10, 8))
            ax.pie(contador_lenguaje, labels=contador_lenguaje.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
            ax.set_title('Distribución de Canciones por Idioma')
            st.pyplot(fig)
        
        elif st.session_state.subpage == "subcategoria_c":
            st.header("Subcategoría C")
            st.write("Aquí se mostrarán los datos de la Subcategoría C.")
            
           
            pf['release_date'] = pd.to_datetime(pf['release_date'], errors='coerce')
            pf_filtrado = pf.dropna(subset=['release_date'])
            pf_filtrado['year'] = pf_filtrado['release_date'].dt.year

            
            generos = pf_filtrado['genre'].dropna().unique()
            genero_seleccionado = st.selectbox('Selecciona un género musical:', options=generos)

            
            pf_filtrado_genero = pf_filtrado[pf_filtrado['genre'] == genero_seleccionado]

            
            min_year = int(pf_filtrado_genero['year'].min())
            max_year = int(pf_filtrado_genero['year'].max())
            rango_años = st.slider('Selecciona el rango de años:', min_year, max_year, (min_year, max_year))

           
            pf_filtrado_rango = pf_filtrado_genero[(pf_filtrado_genero['year'] >= rango_años[0]) & (pf_filtrado_genero['year'] <= rango_años[1])]

            
            releases_by_year = pf_filtrado_rango.groupby('year').size()
            
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(releases_by_year.index, releases_by_year.values, marker='o')
            ax.set_title(f"Tendencia de Lanzamientos de Canciones en {genero_seleccionado} ({rango_años[0]}-{rango_años[1]})")
            ax.set_xlabel("Año")
            ax.set_ylabel("Número de Canciones")
            ax.grid(True)
            st.pyplot(fig)

        elif st.session_state.subpage == "subcategoria_d":
            st.header("Subcategoría D: Duración Promedio de Canciones por Género") 
            pf_filtrado_duracion = pf.dropna(subset=['genre', 'duration'])
            pf_filtrado_duracion['duration_min'] = pf_filtrado_duracion['duration'] / 60
            duracion_promedio = pf_filtrado_duracion.groupby('genre')['duration_min'].mean()
            canciones_por_genero = pf_filtrado_duracion['genre'].value_counts()
            generos_populares = canciones_por_genero.head(10).index
            duracion_promedio_populares = duracion_promedio[duracion_promedio.index.isin(generos_populares)]
            plt.figure(figsize=(14, 10))
            duracion_promedio_populares.sort_values().plot(kind='bar', color='skyblue')
            plt.title('Duración Promedio de Canciones por Género (Top 10 Géneros con Más Canciones)', fontsize=14)
            plt.xlabel('Género', fontsize=12)
            plt.ylabel('Duración Promedio (minutos)', fontsize=12)
            plt.xticks(rotation=45, ha='right')   
            st.pyplot(plt)        
        elif st.session_state.subpage == "subcategoria_e":
            st.header("Subcategoría E")
            st.write("Aquí se mostrarán los datos de la Subcategoría E.") 

            pf_numericos = pf[pd.to_numeric(df['collaboration'], errors='coerce').notna()]
            pf_numericos
            st.title("Visualización de Colaboraciones")
            opcion_colaboracion = st.selectbox("Selecciona el tipo de colaboración", ("Con colaboración", "Sin colaboración")) 

        if st.button("Volver atrás"):
            cambiar_pagina("inicio")

elif st.session_state.page == "categoría_3":
    st.header("Contenido de Opción 3")
    st.write("Aquí se mostrarán los datos relacionados con la Opción 3.")
    
    if st.button("Volver atrás"):
        cambiar_pagina("inicio")






















