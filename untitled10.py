import streamlit as st
import base64

# Cargar la imagen de fondo
image_path = "fondo_morado.png"  # Asegúrate de tener la imagen en el directorio correcto

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
st.title("Aplicación de Categorías")

# Mostrar botones solo si estamos en la página de inicio
if st.session_state.page == "inicio":
    st.header("Seleccione una categoría")
    
    # Utilizar columnas para alinear los botones horizontalmente
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Mejor Valorada\nEn esta categoría podemos filtrar por calificación de los usuarios."):
            cambiar_pagina("categoría_1")
    
    with col2:
        if st.button("Tipo\nEn esta categoría podemos filtrar por categoría de aplicación y sus funciones."):
            cambiar_pagina("categoría_2")
    
    with col3:
        if st.button("Navegación Libre"):
            cambiar_pagina("categoría_3")

# Mostrar contenido según la página seleccionada
elif st.session_state.page == "categoría_1":
    st.header("Aquí se mostrarán las aplicaciones mejores valoradas.")
    
    if st.button("Volver atrás"):
        cambiar_pagina("inicio")

elif st.session_state.page == "categoría_2":
    # Manejar las subpáginas de la categoría "Tipos"
    if st.session_state.subpage is None:
        st.header("Seleccione el tipo de aplicación")
        
        # Mostrar botones para las subcategorías
        if st.button("Videojuego/Entretenimiento"):
            cambiar_subpagina("videojuego")
        if st.button("Social"):
            cambiar_subpagina("social")
        if st.button("Productividad"):
            cambiar_subpagina("productividad")
        if st.button("Educación"):
            cambiar_subpagina("educación")
        if st.button("Cuidados"):
            cambiar_subpagina("cuidados")
        
        if st.button("Volver atrás"):
            cambiar_pagina("inicio")
    
    # Manejo de subpáginas específicas
    else:
        if st.session_state.subpage == "videojuego":
            st.header("Video


















