import streamlit as st
import base64
import pandas as pd
import matplotlib.pyplot as plt


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
    pf
    
    if st.button("Volver atrás"):
        cambiar_pagina("inicio")

elif st.session_state.page == "categoría_2":
    # Manejar las subpáginas de la categoría "Opción 2"
    if st.session_state.subpage is None:
        st.header("Seleccione una subcategoría")
        
        # Mostrar botones para las subcategorías
        if st.button("Grafico De contenido Explicito"):
            cambiar_subpagina("subcategoria_a")

        if st.button("Subcategoría B"):
            cambiar_subpagina("subcategoria_b")  
        if st.button("Subcategoría C"):
            cambiar_subpagina("subcategoria_c")
        if st.button("Subcategoría D"):
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
            contenido_explicito = pf["explicit_content"].value_counts()
            contenido_explicito.plot(kind='bar', color=['lightblue', 'orange'])
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.set_xticklabels(['No Explícito', 'Explícito'], rotation=0, ax=ax)
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
        elif st.session_state.subpage == "subcategoria_d":
            st.header("Subcategoría D")
            st.write("Aquí se mostrarán los datos de la Subcategoría D.")
        elif st.session_state.subpage == "subcategoria_e":
            st.header("Subcategoría E")
            st.write("Aquí se mostrarán los datos de la Subcategoría E.")
        
        # Botón para volver a la lista de subcategorías sin salir de "categoría_2"
        if st.button("Volver a subcategorías"):
            st.session_state.subpage = None

elif st.session_state.page == "categoría_3":
    st.header("Contenido de Opción 3")
    st.write("Aquí se puede explorar la Opción 3 de forma libre.")
    
    if st.button("Volver atrás"):
        cambiar_pagina("inicio")



















