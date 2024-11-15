# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ANxMVyiZYPhA8hC2cqhGPCoPLnXcH1ah
"""
import streamlit as st
import base64

# Ruta de la imagen (reemplaza con el nombre de tu archivo)
image_path = "portada.png"  # Asegúrate de que la imagen esté en la misma carpeta o proporciona la ruta completa

# Codificar la imagen en base64 directamente
with open(image_path, "rb") as img_file:
    base64_image = base64.b64encode(img_file.read()).decode()

# Aplicar la imagen como fondo usando CSS
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

# Contenido de la aplicación
st.title('Aplicación con Fondo de Imagen')
st.write('¡Bienvenido a mi aplicación con fondo personalizado!')









