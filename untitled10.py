import streamlit as st
import base64
import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
pf = pd.read_csv("spotify_songs_dataset.csv")

# Ruta de la imagen para el fondo
image_path = "fondo_morado.png"

# Codificar la imagen en base64
with open(image_path, "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode()

# Estilo de fondo para la aplicación
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

# Configuración inicial de las páginas y subpáginas
if "page" not in st.session_state:
    st.session_state.page = "inicio"

if "subpage" not in st.session_state:
    st.session_state.subpage = None

# Función para cambiar la página
def cambiar_pagina(nueva_pagina):
    st.session_state.page = nueva_pagina
    if nueva_pagina != "categoría_2":
        st.session_state.subpage = None  # Resetear subpáginas cuando no estamos en categoría_2

# Función para cambiar la subpágina dentro de "Tipos"
def cambiar_subpagina(nueva_subpagina):
    st.session_state.subpage = nueva_subpagina

# Título de la aplicación
st.title("Aplicación Genérica")

# Página de inicio con opciones
if st.session_state.page == "inicio":
    st.header("Seleccione una opción")

    # Disposición de botones en columnas
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

# Página "Categoría 1"
elif st.session_state.page == "categoría_1":
    st.header("Contenido de Opción 1")
    st.write("Aquí se mostrarán los datos relacionados con la Opción 1.")
    st.write(pf)  # Muestra el DataFrame

    if st.button("Volver atrás"):
        cambiar_pagina("inicio")

# Página "Categoría 2"
elif st.session_state.page == "categoría_2":
    if st.session_state.subpage is None:
        st.header("Seleccione una subcategoría")

        # Botones de subcategorías
        if st.button("Gráfico de contenido Explícito"):
            cambiar_subpagina("subcategoria_a")

        if st.button("Distribución de idioma de canciones"):
            cambiar_subpagina("subcategoria_b")

        if st.button("Tendencia de lanzamiento de canciones"):
            cambiar_subpagina("subcategoria_c")

        if st.button("Subcategoría D"):
            cambiar_subpagina("subcategoria_d")

        if st.button("Subcategoría E"):
            cambiar_subpagina("subcategoria_e")

        if st.button("Volver atrás"):
            cambiar_pagina("inicio")

    # Manejo de subpáginas
    else:
        if st.session_state.subpage == "subcategoria_a":
            st.header("Subcategoría A")
            st.write("Gráfico de canciones con contenido explícito por género.")
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
            st.write("Distribución de canciones por idioma.")
            contador_lenguaje = pf["language"].value_counts()
            fig, ax = plt.subplots(figsize=(10, 8))
            ax.pie(contador_lenguaje, labels=contador_lenguaje.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
            ax.set_title('Distribución de Canciones por Idioma')
            st.pyplot(fig)

        elif st.session_state.subpage == "subcategoria_c":
            st.header("Subcategoría C")
            st.write("Selección de género musical y visualización de canciones.")
            
            # Mostrar lista de géneros disponibles
            generos = pf['genre'].unique()
            genero_seleccionado = st.selectbox("Selecciona un género:", generos)

            # Filtrar y mostrar las canciones del género seleccionado
            canciones_genero = pf[pf['genre'] == genero_seleccionado]
            
            if not canciones_genero.empty:
                st.write(f"Mostrando canciones del género: {genero_seleccionado}")
                st.write(canciones_genero[['song_name', 'artist', 'explicit_content']])
            else:
                st.write("No hay canciones para este género.")

        elif st.session_state.subpage == "subcategoria_d":
            st.header("Subcategoría D")
            st.write("Información sobre la Subcategoría D.")

        elif st.session_state.subpage == "subcategoria_e":
            st.header("Subcategoría E")
            st.write("Información sobre la Subcategoría E.")

        # Botón para volver a subcategorías
        if st.button("Volver a subcategorías"):
            st.session_state.subpage = None

# Página "Categoría 3"
elif st.session_state.page == "categoría_3":
    st.header("Contenido de Opción 3")
    st.write("Contenido libre de la Opción 3.")
    
    if st.button("Volver atrás"):
        cambiar_pagina("inicio")



















