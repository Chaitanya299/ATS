import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() 
genai.configure(api_key=os.getenv("AIzaSyBUN2l7sgPUb8rN8pmO8JjKXwsoLIqO9KUst"))

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response as per below structure
{{"JD Match": "%", "MissingKeywords": [], "Profile Summary": "", "areas to focus":""}}
"""

## streamlit app

with st.sidebar:
    st.title("Updated ATS for screening resume")
    st.subheader("About")
    st.write("Welcome to the Gemini Pro Applicant Tracking System (ATS)! This system is developed using the powerful Gemini Pro model to streamline the hiring process by analyzing job descriptions and resumes. It provides valuable insights such as job description match, missing keywords, and profile summary.")
    
    st.markdown("""
    - [Streamlit](https://streamlit.io/)
    - [Gemini Pro](https://deepmind.google/technologies/gemini/#introduction)
    - [makersuit API Key](https://makersuite.google.com/)
                
    """)
    
    add_vertical_space(5)
    st.write("By~chaitu.")
    
    


st.title("Smart Application Tracking System") 
st.text("Improve Your Resume ATS")

col1, col2 = st.columns(2, gap="medium")


with col1:
    st.write("") 
    st.text_area("Paste the Job Description", height=300)  
    st.write("") 


with col2:
    st.write("")  
    st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf under 200 MB")
    st.write("")  
submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        st.subheader(response)