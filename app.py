
from pathlib import Path

import joblib
import streamlit as st

MODEL_PATH = Path("models/fraud_detector.joblib")

st.set_page_config(
    page_title="JobShield | Job Posting Detector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model not found. Run python train_model.py first."
        )
    return joblib.load(MODEL_PATH)


st.markdown("""
<style>
.block-container {
    max-width: 1050px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero {
    padding: 2rem;
    border-radius: 20px;
    background: linear-gradient(120deg, #10233f, #245b78);
    color: white;
    margin-bottom: 1.5rem;
}
.hero h1 { color: white; margin-bottom: .5rem; }
.hero p { color: #e0edf7; font-size: 1.05rem; }
div.stButton > button, div.stFormSubmitButton > button {
    border-radius: 10px;
    min-height: 2.8rem;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
    <h1>🛡️ JobShield</h1>
    <p>AI-powered screening for suspicious job postings.</p>
    <p>Analyze job descriptions, review model signals, and make
    more informed decisions before applying.</p>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1.5, 1])

with left:
    st.subheader("Analyze a job posting")
    st.write("Enter the details below. Only the job title or description is required.")

    with st.form("job_form"):
        title = st.text_input("Job title", placeholder="e.g. Junior Python Developer")
        company = st.text_input("Company name (optional)")
        company_profile = st.text_area(
            "Company profile (optional)", height=90
        )
        description = st.text_area(
            "Job description",
            height=190,
            placeholder="Paste the complete job description here...",
        )
        requirements = st.text_area("Requirements (optional)", height=100)
        benefits = st.text_area("Benefits (optional)", height=90)

        submitted = st.form_submit_button(
            "🔎 Analyze posting", use_container_width=True
        )

with right:
    st.subheader("Before you apply")
    st.markdown("""
    **Watch for common warning signs:**
    - Requests for upfront payment or registration fees
    - Unrealistic salary promises
    - Pressure to accept immediately
    - Unverifiable company contact details
    - Requests for sensitive information too early
    """)
    st.info(
        "JobShield is a screening aid. It cannot verify an employer "
        "or guarantee that a job is genuine."
    )

if submitted:
    combined_text = " ".join([
        title, company, company_profile, description,
        requirements, benefits
    ]).strip()

    if not combined_text:
        st.warning("Enter a job title or job description first.")
    else:
        try:
            model = load_model()
            prediction = int(model.predict([combined_text])[0])
            probabilities = model.predict_proba([combined_text])[0]
            fraud_score = float(
                probabilities[list(model.classes_).index(1)]
            )

            st.divider()
            st.subheader("Analysis results")

            score_col, result_col = st.columns([1, 2])

            with score_col:
                st.metric("Model fraud score", f"{fraud_score:.1%}")
                st.progress(fraud_score)

            with result_col:
                if prediction == 1:
                    st.error(
                        "⚠️ Potentially suspicious posting",
                        icon="🚨",
                    )
                    st.write(
                        "The model identified patterns associated with "
                        "fraudulent postings. Verify the employer independently."
                    )
                else:
                    st.success(
                        "No strong fraud signal detected",
                        icon="✅",
                    )
                    st.write(
                        "The model classified this posting as likely "
                        "legitimate. This does not guarantee that it is safe."
                    )

            st.caption(
                "The score is the model's estimated class probability, "
                "not a verified probability of fraud. Predictions can be wrong."
            )

            with st.expander("Important verification steps"):
                st.markdown("""
                1. Find the vacancy on the employer's official website.
                2. Verify the recruiter's email domain and contact details.
                3. Never pay a fee to obtain a job.
                4. Do not share banking details, passwords, or OTPs.
                5. Research the company independently before accepting an offer.
                """)

        except FileNotFoundError as error:
            st.error(str(error))
        except Exception as error:
            st.error(f"Analysis failed: {error}")
            st.caption("Check the VS Code terminal for more details.")

st.divider()
st.caption(
    "JobShield • Student AI/ML project using TF-IDF and Logistic Regression"
)
