import streamlit as st
import urllib.parse

st.set_page_config(page_title="Buscador Científico", layout="centered")

st.title("🔍 Buscador de Información Científica")
st.markdown("Construye ecuaciones de búsqueda con operadores booleanos y selecciona una base de datos académica.")

# Entradas
st.subheader("1️⃣ Términos de búsqueda")
term1 = st.text_input("Término 1")
operator1 = st.selectbox("Operador booleano", ["AND", "OR", "NOT"])
term2 = st.text_input("Término 2")
add_third = st.checkbox("¿Agregar un tercer término?")
if add_third:
    operator2 = st.selectbox("Segundo operador booleano", ["AND", "OR", "NOT"])
    term3 = st.text_input("Término 3")
else:
    operator2 = ""
    term3 = ""

# Construir ecuación de búsqueda
query = f'{term1} {operator1} {term2}'
if add_third and term3.strip():
    query += f' {operator2} {term3}'

st.markdown(f"### 🔍 Ecuación de búsqueda generada:\n```\n{query}\n```")

# Bases de datos
st.subheader("2️⃣ Selecciona base de datos")
database = st.selectbox("Base de datos", ["PubMed", "Scopus", "Google Scholar", "Web of Science"])

# Generar URLs de búsqueda
def generate_search_url(database, query):
    encoded_query = urllib.parse.quote(query)
    if database == "PubMed":
        return f"https://pubmed.ncbi.nlm.nih.gov/?term={encoded_query}"
    elif database == "Scopus":
        return f"https://www.scopus.com/results/results.uri?src=s&sid=&sot=b&s=TITLE-ABS-KEY({encoded_query})"
    elif database == "Google Scholar":
        return f"https://scholar.google.com/scholar?q={encoded_query}"
    elif database == "Web of Science":
        return f"https://www.webofscience.com/wos/woscc/basic-search?search_mode=GeneralSearch&q={encoded_query}"
    else:
        return ""

# Mostrar botón y link
if st.button("🔎 Realizar búsqueda"):
    url = generate_search_url(database, query)
    st.success(f"✅ Haz clic en el enlace para abrir la búsqueda en {database}:")
    st.markdown(f"[🔗 Ir a {database}]({url})", unsafe_allow_html=True)
