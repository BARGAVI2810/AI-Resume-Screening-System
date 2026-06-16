import streamlit as st
import PyPDF2
import pandas as pd
import matplotlib.pyplot as plt
import re
import os

# ------------------------------------
# Page Settings
# ------------------------------------

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Screening System")

st.write(
    "Upload a resume and analyze it based on the selected job role."
)

# ------------------------------------
# Create History File
# ------------------------------------

if not os.path.exists("data"):
    os.makedirs("data")

if not os.path.exists("data/history.csv"):
    history_df = pd.DataFrame(
        columns=["Name", "Email", "Role", "Score"]
    )
    history_df.to_csv(
        "data/history.csv",
        index=False
    )

# ------------------------------------
# Job Role Selection
# ------------------------------------

job_role = st.selectbox(
    "Select Job Role",
    [
        "Data Analyst",
        "AI Engineer",
        "Java Developer"
    ]
)

# ------------------------------------
# Required Skills
# ------------------------------------

if job_role == "Data Analyst":

    required_skills = [
        "python",
        "sql",
        "power bi",
        "tableau",
        "excel"
    ]

elif job_role == "AI Engineer":

    required_skills = [
        "python",
        "machine learning",
        "deep learning",
        "tensorflow",
        "sql"
    ]

else:

    required_skills = [
        "java",
        "spring",
        "mysql",
        "html",
        "css"
    ]

# ------------------------------------
# Upload Resume
# ------------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# ------------------------------------
# Process Resume
# ------------------------------------

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    # --------------------------------
    # Extract Name
    # --------------------------------

    lines = text.split("\n")

    name = "Not Found"

    for line in lines:

        line = line.strip()

        if len(line) > 2 and len(line.split()) <= 4:
            name = line
            break

    # --------------------------------
    # Extract Email
    # --------------------------------

    email_match = re.search(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    email = (
        email_match.group()
        if email_match
        else "Not Found"
    )

    # --------------------------------
    # Candidate Info
    # --------------------------------

    st.subheader("👤 Candidate Information")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Name:** {name}")

    with col2:
        st.write(f"**Email:** {email}")

    # --------------------------------
    # Resume Content
    # --------------------------------

    st.subheader("📄 Resume Content")

    st.text_area(
        "Extracted Resume Text",
        text,
        height=250
    )

    # --------------------------------
    # Skill Analysis
    # --------------------------------

    score = 0

    missing = []

    for skill in required_skills:

        if skill.lower() in text.lower():

            score += (
                100 / len(required_skills)
            )

        else:

            missing.append(skill)

    score = round(score)

    # --------------------------------
    # Resume Score
    # --------------------------------

    st.subheader("📊 Resume Score")

    st.progress(score / 100)

    st.success(
        f"Resume Score: {score}%"
    )

    # --------------------------------
    # Rating
    # --------------------------------

    if score >= 80:

        st.success(
            "🔥 Strong Candidate"
        )

    elif score >= 60:

        st.warning(
            "👍 Good Resume"
        )

    else:

        st.error(
            "⚠ Needs Improvement"
        )

    # --------------------------------
    # Missing Skills
    # --------------------------------

    st.subheader("❌ Missing Skills")

    if len(missing) == 0:

        st.success(
            "No Missing Skills Found"
        )

    else:

        for skill in missing:

            st.write(
                f"• {skill}"
            )

    # --------------------------------
    # Suggestions
    # --------------------------------

    suggestions = {

        "python":
        "Practice Python projects",

        "sql":
        "Learn SQL queries",

        "power bi":
        "Build Power BI dashboards",

        "tableau":
        "Learn Tableau visualization",

        "excel":
        "Practice Excel analytics",

        "machine learning":
        "Study ML algorithms",

        "deep learning":
        "Learn Neural Networks",

        "tensorflow":
        "Build TensorFlow projects",

        "java":
        "Build Java projects",

        "spring":
        "Learn Spring Boot",

        "mysql":
        "Practice MySQL database projects",

        "html":
        "Build Responsive Web Pages",

        "css":
        "Learn CSS styling"
    }

    st.subheader("💡 Suggestions")

    for skill in missing:

        if skill in suggestions:

            st.write(
                f"✅ {skill}: {suggestions[skill]}"
            )

    # --------------------------------
    # Statistics
    # --------------------------------

    matched = (
        len(required_skills)
        - len(missing)
    )

    st.subheader("📈 Statistics")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Matched Skills",
            f"{matched}/{len(required_skills)}"
        )

    with col2:

        st.metric(
            "Resume Score",
            f"{score}%"
        )

    # --------------------------------
    # Pie Chart
    # --------------------------------

    st.subheader(
        "📊 Skill Match Chart"
    )

    fig, ax = plt.subplots()

    ax.pie(
        [matched, len(missing)],
        labels=["Matched", "Missing"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

    # --------------------------------
    # Save History
    # --------------------------------

    history = pd.read_csv(
        "data/history.csv"
    )

    new_record = pd.DataFrame(
        [[
            name,
            email,
            job_role,
            score
        ]],
        columns=[
            "Name",
            "Email",
            "Role",
            "Score"
        ]
    )

    history = pd.concat(
        [history, new_record],
        ignore_index=True
    )

    history.to_csv(
        "data/history.csv",
        index=False
    )

    # --------------------------------
    # Show History
    # --------------------------------

    st.subheader(
        "📋 Candidate History"
    )

    st.dataframe(history)