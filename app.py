import streamlit as st
import PyPDF2
from PIL import Image
import os
import base64

# 💫 Custom Background Styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("https://www.transparenttextures.com/patterns/clean-gray-paper.png");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ Show your logo at the top of the page
logo = Image.open("logo.png")
st.image(logo, width=150)

# 🌸 💖 Stylish Welcome Header (Place this here)
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <h1 style="color:#FF69B4; font-size: 40px;">💖 Welcome to <span style='color:#8A2BE2;'>Resume Analyzer</span> 💼</h1>
        <p style="font-size: 18px; color: #555;">Make your resume shine ✨ and land your dream job 💼</p>
        <hr style="height:3px;border:none;color:#FF69B4;background-color:#FF69B4;" />
    </div>
""", unsafe_allow_html=True)

# ✅ Custom title (optional)
st.markdown("""
    <div style="text-align: center;">
        <h1 style='color: #4CAF50;'>🧠 AI Resume Analyzer</h1>
        <h4>🚀 Built for Job Seekers & Freshers | Analyze. Improve. Succeed.</h4>
        <hr style="border-top: 3px solid #bbb;">
    </div>
""", unsafe_allow_html=True)

# ---------- 1. Extract text from uploaded PDF ----------
def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# ---------- 2. Job match scoring ----------
def calculate_match_score(resume_text, job_description):
    resume_words = set(resume_text.lower().split())
    jd_words = set(job_description.lower().split())
    match_count = len(resume_words & jd_words)
    total_keywords = len(jd_words)
    if total_keywords == 0:
        return 0
    return int((match_count / total_keywords) * 100)


# ---------- 3. Suggest best-fit job role ----------
def suggest_role(resume_text):
    text = resume_text.lower()
    if "machine learning" in text or "deep learning" in text:
        return "Machine Learning Engineer"
    elif "data analysis" in text or "sql" in text:
        return "Data Analyst"
    elif "react" in text or "javascript" in text:
        return "Frontend Developer"
    elif "java" in text or "spring boot" in text:
        return "Backend Developer"
    elif "aws" in text or "cloud" in text:
        return "Cloud Engineer"
    else:
        return "Software Developer"


# ---------- 4. Suggestions to improve resume ----------
def improvement_suggestions(resume_text):
    suggestions = []
    if "projects" not in resume_text.lower():
        suggestions.append("✅ Add a Projects section to showcase your work.")
    if "linkedin" not in resume_text.lower():
        suggestions.append("✅ Include your LinkedIn profile link.")
    if "github" not in resume_text.lower():
        suggestions.append("✅ Include your GitHub profile to show code samples.")
    if "objective" not in resume_text.lower():
        suggestions.append("✅ Add a short objective/summary at the top.")
    return suggestions


# ---------- 5. Mistakes to avoid ----------
def common_mistakes(resume_text):
    mistakes = []
    if len(resume_text.split()) < 100:
        mistakes.append("❌ Resume seems too short. Add more details.")
    if "i am" in resume_text.lower():
        mistakes.append("❌ Avoid using personal pronouns like 'I'. Use professional language.")
    if "dummy" in resume_text.lower() or "lorem" in resume_text.lower():
        mistakes.append("❌ Remove placeholder/dummy text like 'Lorem ipsum'.")
    return mistakes


# ---------- 6. Streamlit App UI ----------
st.title("🧠 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])

# Dummy job description keywords
job_description = "python sql data analysis machine learning communication problem solving"

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Extracted Resume Text")
    st.text_area("Resume Content", resume_text, height=300)

    # Job match score
    match_score = calculate_match_score(resume_text, job_description)
    st.subheader("📊 Job Fit Score")
    st.progress(match_score)
    st.write(f"✅ Estimated match with job description: **{match_score}%**")

    # Suggested role
    role = suggest_role(resume_text)
    st.subheader("🧭 Suggested Role")
    st.success(role)

    # Resume improvement suggestions
    st.subheader("📈 Suggestions to Improve Resume")
    improvements = improvement_suggestions(resume_text)
    if improvements:
        for item in improvements:
            st.info(item)
    else:
        st.success("✅ Resume looks well-structured!")

    # Common mistakes
    st.subheader("⚠️ Common Mistakes to Avoid")
    mistakes = common_mistakes(resume_text)
    if mistakes:
        for m in mistakes:
            st.warning(m)
    else:
        st.success("✅ No obvious mistakes found.")

        # ✅ Add this at the very end of app.py
st.markdown("""
    <hr>
    <div style="text-align: center; font-size: 14px; color: #999;">
        Made with ❤️ by <strong>SREE HARSHA</strong> <br>
    </div>
""", unsafe_allow_html=True)
