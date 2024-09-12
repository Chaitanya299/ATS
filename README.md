#Resume application tracking system using google gemini

##Overview
Welcome to the Gemini Pro Applicant Tracking System (ATS)! This system is developed using the powerful Gemini Pro model to streamline the hiring process by analyzing job descriptions and resumes. It provides valuable insights such as job description match, missing keywords, and profile summary.

##credits 
Original project is done by prajwal K 

##Requirements
* Python 3.10 (or higher)
* Gemini Pro model api key (Note: Ensure you have the necessary credentials and permissions to access the Gemini Pro API)

##Description
This project is built upon streamlit api which is an web application, which acts as the user interface and gemini pro API to screen the applicant as per the job description.

PDF reader - PyPDF2 which is a pdf to text reader which collects the applicants data.
Gemini pro - LLM project by Google DeepMind helps us score the applicant from a precurated prompt.

##App functionality

##Resume Analysis
* Read in the resume text and extract relevant information such as skills, experience, and education
* Tokenize the text and remove stop words
* Calculate the frequency of each word and phrase

###Job Description Analysis
* Read in the job description text and extract relevant information such as required skills, experience, and qualifications
* Tokenize the text and remove stop words
* Calculate the frequency of each word and phrase

###Match Percentage Calculation
* Compare the frequency of words and phrases in the resume and job description
* Calculate a match percentage based on the similarity between the two

###Missing Keywords Identification
* Identify keywords in the job description that are not present in the resume
* Return a list of missing keywords

###Profile Summary Generation
* Use the extracted information from the resume to generate a concise profile summary

###Areas to Focus On
* Identify areas where the candidate's skills and experience do not align with the job requirements
* Return a list of areas to focus on for improvement

##Usage

1. Run the application:
streamlit run app.py

2. Access the application through your web browser at http://localhost:5000.
3. Input the job description and candidate's resume in the provided fields.
4. Click the "Submit" button to initiate the analysis.
5. Review the results, including the job description match, missing keywords, and profile summary.
