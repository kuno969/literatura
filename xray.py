import streamlit as st

st.set_page_config(page_title="Métodos de Diagnóstico por Imágenes", layout="centered")

st.title("🩻 Métodos de Diagnóstico por Imágenes en Medicina")
st.markdown("Haz clic en cada sección para conocer los conceptos principales de los métodos más utilizados en la práctica clínica.")

# Diccionario con la información
metodos = {
    "Resonancia Magnética": {
        "descripcion": "Técnica que utiliza campos magnéticos y ondas de radio para obtener imágenes detalladas de órganos y tejidos internos, sin usar radiación ionizante.",
        "imagen": "images/resonancia.png"
    },
    "Tomografía Computarizada": {
        "descripcion": "Método que combina rayos X y procesamiento computarizado para generar cortes o secciones detalladas del cuerpo humano.",
        "imagen": "images/tomografia.png"
    },
    "Medicina Nuclear": {
        "descripcion": "Uso de pequeñas cantidades de materiales radiactivos para diagnosticar y tratar enfermedades. Se obtienen imágenes funcionales del cuerpo.",
        "imagen": "images/medicina_nuclear.png"
    },
    "Radiología Intervencionista": {
        "descripcion": "Subespecialidad que utiliza imágenes médicas para guiar procedimientos mínimamente invasivos con fines diagnósticos o terapéuticos.",
        "imagen": "images/radiologia_intervencionista.png"
    },
    "Ecografía": {
        "descripcion": "Método que utiliza ondas sonoras de alta frecuencia para visualizar estructuras internas del cuerpo en tiempo real.",
        "imagen": "images/ecografia.png"
    }
}

# Mostrar las secciones
for nombre, datos in metodos.items():
    with st.expander(f"🧭 {nombre}"):
        st.image(datos["imagen"], width=300)
        st.write(datos["descripcion"])
