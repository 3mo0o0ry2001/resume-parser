# advanced_resume_parser.py

import fitz  # PyMuPDF
import re
import spacy
import streamlit as st
import pandas as pd
from datetime import datetime

# Load spaCy transformer model
try:
    nlp = spacy.load("en_core_web_trf")
except:
    st.error("Model en_core_web_trf not found. Run: python -m spacy download en_core_web_trf")
    st.stop()

# Sample skills database (expand as needed)
SKILLS_DB = [
    "python", "sql", "excel", "communication", "nlp", "machine learning",
    "deep learning", "data analysis", "pandas", "numpy", "scikit-learn", "tensorflow",
    "keras", "fastapi", "docker", "git", "linux"
]

# PDF text extraction
def extract_text_from_pdf(uploaded_file):
    text = ""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

# Named Entity Recognition (NER)
def extract_entities(text):
    doc = nlp(text)
    people = set()
    orgs = set()
    dates = set()
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            people.add(ent.text)
        elif ent.label_ == "ORG":
            orgs.add(ent.text)
        elif ent.label_ == "DATE":
            dates.add(ent.text)
    return {
        "names": list(people),
        "organizations": list(orgs),
        "dates": list(dates)
    }

# Contact info extraction
def extract_email(text):
    match = re.search(r"\b[\w.-]+?@[\w.-]+?\.\w{2,4}\b", text)
    return match.group() if match else "Not found"

def extract_phone(text):
    match = re.search(r"\+?\d[\d\s\-]{8,}\d", text)
    return match.group() if match else "Not found"

def extract_linkedin(text):
    match = re.search(r"https?://(www\.)?linkedin\.com/in/[\w\-]+", text)
    return match.group() if match else "Not found"

# Skill matching
def extract_skills(text):
    found = []
    text_lower = text.lower()
    for skill in SKILLS_DB:
        if skill.lower() in text_lower:
            found.append(skill)
    return found if found else ["No skills matched"]

# Streamlit UI with dashboard
parsed_data = []

def main():
    st.set_page_config(page_title="Smart Resume Parser", layout="wide")
    st.title("📄 Smart Resume Parser for Recruiters")
    st.markdown("""
        Upload a candidate's resume in PDF format, and this tool will extract structured information
        like name, email, phone number, LinkedIn, skills, work experience hints, and education clues.
    """)

    uploaded = st.file_uploader("Upload Resume (PDF Only)", type="pdf")

    if uploaded:
        with st.spinner("Reading and analyzing the resume..."):
            text = extract_text_from_pdf(uploaded)
            entities = extract_entities(text)
            email = extract_email(text)
            phone = extract_phone(text)
            linkedin = extract_linkedin(text)
            skills = extract_skills(text)

            parsed_data.append({
                "Name": entities['names'][0] if entities['names'] else "Not found",
                "Email": email,
                "Phone": phone,
                "LinkedIn": linkedin,
                "Skills": ", ".join(skills),
                "Organizations": ", ".join(entities['organizations']),
                "Dates": ", ".join(entities['dates'])
            })

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📌 Contact Information")
            st.write(f"**Name:** {parsed_data[-1]['Name']}")
            st.write(f"**Email:** {parsed_data[-1]['Email']}")
            st.write(f"**Phone:** {parsed_data[-1]['Phone']}")
            st.write(f"**LinkedIn:** {parsed_data[-1]['LinkedIn']}")

        with col2:
            st.subheader("💼 Skills Matched")
            st.write(parsed_data[-1]['Skills'])

        st.subheader("🏢 Experience & 🎓 Education (NER-based hints)")
        st.write("**Organizations Mentioned:**", parsed_data[-1]['Organizations'] or "None")
        st.write("**Dates Detected:**", parsed_data[-1]['Dates'] or "None")

        st.success("✅ Resume processed successfully.")

    st.markdown("---")
    st.subheader("📊 Dashboard - Summary of Parsed Resumes")
    if parsed_data:
        df = pd.DataFrame(parsed_data)
        st.dataframe(df, use_container_width=True)
        with st.expander("📥 Export to CSV"):
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV", csv, "parsed_resumes.csv", "text/csv")
    else:
        st.info("Upload one or more resumes to generate the dashboard.")

if __name__ == "__main__":
    main()
