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

# Configuración inicial para la página
if "page" not in st.session_state:
    st.session_state.page = "inicio"

# Función para cambiar la página
def cambiar_pagina(nueva_pagina):
    st.session_state.page = nueva_pagina

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
    st.header("Seleccione el tipo de aplicación")

    # Crear botones para cada tipo de aplicación con navegación a subpáginas
    tipo_col1, tipo_col2, tipo_col3, tipo_col4, tipo_col5 = st.columns(5)
    
    with tipo_col1:
        if st.button("Videojuego/Entretenimiento"):
            cambiar_pagina("videojuego")
    
    with tipo_col2:
        if st.button("Social"):
            cambiar_pagina("social")
    
    with tipo_col3:
        if st.button("Productividad"):
            cambiar_pagina("productividad")
    
    with tipo_col4:
        if st.button("Educación"):
            cambiar_pagina("educación")
    
    with tipo_col5:
        if st.button("Cuidados"):
            cambiar_pagina("cuidados")
    
    if st.button("Volver atrás"):
        cambiar_pagina("inicio")

# Subpáginas para cada tipo de aplicación
elif st.session_state.page == "videojuego":
    st.header("Videojuego/Entretenimiento")
    st.write("Aquí se mostrarán las aplicaciones de Videojuego/Entretenimiento.")
    
    if st.button("Volver atrás"):
        cambiar_pagina("categoría_2")

elif st.session_state.page == "social":
    st.header("Social")
    st.write("Aquí se mostrarán las aplicaciones de la categoría Social.")
    
    if st.button("Volver atrás"):
        cambiar_pagina("categoría_2")

elif st.session_state.page == "productividad":
    st.header("Productividad")
    st.write("Aquí se mostrarán las aplicaciones de Productividad.")
    
    if st.button("Volver atrás"):
        cambiar_pagina("categoría_2")

elif st.session_state.page == "educación":
    st.header("Educación")
    st.write("Aquí se mostrarán las aplicaciones de Educación.")
    
    if st.button("Volver atrás"):
        cambiar_pagina("categoría_2")

elif st.session_state.page == "cuidados":
    st.header("Cuidados")
    st.write("Aquí se mostrarán las aplicaciones de Cuidados.")
    
    if st.button("Volver atrás"):
        cambiar_pagina("categoría_2")

elif st.session_state.page == "categoría_3":
    st.header("Categoría 3: Navegación Libre")
    
    if st.button("Volver atrás"):
        cambiar_pagina("inicio")
















