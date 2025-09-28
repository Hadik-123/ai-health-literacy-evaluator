import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
import streamlit as st
from evaluator.readability import compute_readability

st.set_page_config(page_title="AI Health-Literacy Evaluator", layout="wide")
st.title("AI Health-Literacy & Quality Evaluator (MVP)")

left, right = st.columns(2)
with left:
    txt = st.text_area("Paste AI-generated patient text", height=260, placeholder="Paste content (e.g., DBS explainer)…")
    if st.button("Evaluate") and txt.strip():
        res = compute_readability(txt)
        st.session_state["res"] = res

with right:
    if "res" in st.session_state:
        st.subheader("Readability Metrics")
        st.json(st.session_state["res"])
    else:
        st.info("Results will appear here.")
