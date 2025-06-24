# 📄 Smart Resume Parser for HR Recruiters

A professional NLP-powered web application built with **Python** and **Streamlit**, designed specifically for **HR recruiters** to extract structured, searchable information from unstructured resumes (PDFs).

---

## 🎯 Why HR Recruiters Need This

Recruiters deal with hundreds of resumes daily. Most are in inconsistent formats and difficult to search.  
This tool automatically extracts and organizes the most relevant information from resumes, saving **hours of manual screening time**.

---

## 🔍 Features

✅ Extracts key resume details:
- Full Name  
- Email Address  
- Phone Number  
- LinkedIn Profile  
- Detected Skills  
- Company Names & Experience Dates  
- Education & Certifications (NER-based hints)

✅ Displays results in a structured **dashboard**  
✅ Allows **CSV export** of all parsed candidates  
✅ Works 100% offline — your data stays private  
✅ Built using `spaCy`, `PyMuPDF`, `Streamlit`


---
#  🧠 Tech Stack
Python 3.10+

spaCy (Transformer-based NER)

Streamlit (UI)

PyMuPDF (PDF Parsing)

Regex (Contact Extraction)

Pandas (Dashboard Table)

#  📦 Use Case Ideas
Screening CVs during hiring sprints

Building a candidate skill database

Integrating with HR applicant tracking systems (ATS)

Fast profiling for tech/non-tech roles

📩 Contact
Built by Omar Ayoub
For hiring, feedback, or collaboration — please reach out at omarayoub.nlp@gmail.com
---

## 🚀 How to Run It Locally

1. Clone the repository  
```bash
git clone https://github.com/yourusername/resume-parser.git
cd resume-parser

pip install -r requirements.txt
python -m spacy download en_core_web_trf

streamlit run advanced_resume_parser.py 
