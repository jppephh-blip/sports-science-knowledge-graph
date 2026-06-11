import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Sports Science Knowledge Graph",
    layout="wide"
)

st.title("🏋️ Sports Science Knowledge Graph")
st.markdown("""
Knowledge Graph construido a partir de artículos de Wikipedia utilizando técnicas de NLP (Named Entity Recognition con spaCy).
""")
st.subheader("Ontología del dominio")

st.markdown("""
La ontología se construyó a partir de conceptos clave de las Ciencias del Entrenamiento Deportivo extraídos de artículos de Wikipedia mediante técnicas de NLP.

### Conceptos principales
- Sports Science
- Exercise Physiology
- Strength Training
- Physical Exercise
- Muscular Hypertrophy
- VO2 Max
- Physical Fitness
- Sports Performance

### Relaciones semánticas
- includes
- studies
- increases
- improves
- supports
- causes
- promotes

Estas relaciones representan conexiones conceptuales identificadas durante el proceso de construcción del Knowledge Graph.
""")

st.subheader("Estadísticas del proyecto")

col1, col2, col3 = st.columns(3)

col1.metric("Artículos", 9)
col2.metric("Nodos", 14)
col3.metric("Relaciones", 10)
html_file = Path("knowledge_graph.html")

if html_file.exists():
    with open(html_file, "r", encoding="utf-8") as f:
        graph_html = f.read()

    st.components.v1.html(
        graph_html,
        height=800,
        scrolling=True
    )
