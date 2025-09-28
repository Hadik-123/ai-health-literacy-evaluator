import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
import streamlit as st
from evaluator.readability import compute_readability
def classify_readability(fre_score: float) -> str:
    if fre_score >= 70:
        return "🟢 Easy to Read (6th–8th grade level)"
    elif fre_score >= 50:
        return "🟡 Moderate (High school level)"
    else:
        return "🔴 Difficult (College level or higher)"

st.set_page_config(page_title="AI Health-Literacy Evaluator", layout="wide")
# ✅ Custom Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&family=Inter:wght@400;500;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins', sans-serif;
        color: #EDF2F4;
        background-color: #0B132B;
    }
    .stTextArea textarea {
        background-color: #1C2541;
        color: #EDF2F4;
        border-radius: 10px;
        border: 1px solid #3A506B;
    }
    .stButton>button {
        background: linear-gradient(90deg, #00B4D8, #48CAE4);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #48CAE4, #00B4D8);
        transform: scale(1.05);
    }
    .stAlert {
        background-color: #1C2541;
        border-left: 5px solid #48CAE4;
    }
    .metric-card {
        background-color: #1C2541;
        padding: 1rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        margin-bottom: 1rem;
    }
    h1, h2, h3 {
        color: #00B4D8 !important;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)
# ✅ UI Layout
st.title("🧠 AI Health-Literacy Evaluator")
st.caption("Evaluate readability and quality of AI-generated patient education materials.")

tab1, tab2 = st.tabs(["💬 Evaluate Text", "📊 Results"])

with tab1:
    txt = st.text_area(
        "Paste AI-generated patient text:",
        height=250,
        placeholder="Paste your medical explainer text here..."
    )
    evaluate_btn = st.button("🚀 Evaluate Readability")

if evaluate_btn and txt.strip():
    res = compute_readability(txt)
    st.session_state["res"] = res
    st.success("✅ Evaluation complete! View results below.")

with tab2:
    if "res" in st.session_state:
        st.subheader("📊 Readability Metrics")
        cols = st.columns(2)
        metrics = st.session_state["res"]

        # ✅ Extract Flesch Reading Ease
        fre = metrics.get("flesch_reading_ease", None)
        if fre is not None:
            level = classify_readability(fre)
            st.markdown(f"<h3 style='margin-top:1rem;'>Overall Classification: {level}</h3>", unsafe_allow_html=True)
            st.caption("This classification is based on the Flesch Reading Ease score.")

        # ✅ Display metrics
        for i, (key, val) in enumerate(metrics.items()):
            with cols[i % 2]:
                st.markdown(f"""
                <div class='metric-card'>
                    <h3>{key.replace('_',' ').title()}</h3>
                    <p style='font-size:1.5rem;font-weight:700;'>{val}</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.info("Paste text in the first tab and click **Evaluate** to see results.")
