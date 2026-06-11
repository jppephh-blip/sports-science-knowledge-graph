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

html_file = Path("knowledge_graph.html")

if html_file.exists():
    with open(html_file, "r", encoding="utf-8") as f:
        graph_html = f.read()

    st.components.v1.html(
        graph_html,
        height=800,
        scrolling=True
    )
