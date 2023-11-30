import streamlit as st
import requests

def extract_skills_from_document(access_token, document_text):
    url = 'https://emsiservices.com/skills/versions/latest/extract'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {"text": document_text}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def extract_skill_names(api_response):
    skill_names = []
    if 'data' in api_response:
        for skill in api_response['data']:
            if 'skill' in skill and 'name' in skill['skill']:
                skill_names.append(skill['skill']['name'])
    return skill_names

def main():
    st.title("Skill Extractor App")

    # Text area for user input
    document_text = st.text_area("Paste your document (resume, job description, etc.) here:", height=300)

    # Button to extract skills
    if st.button("Extract Skills"):
        # Use a pre-obtained access token
        access_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjNDNjZCRjIzMjBGNkY4RDQ2QzJERDhCMjI0MEVGMTFENTZEQkY3MUYiLCJ0eXAiOiJKV1QiLCJ4NXQiOiJQR2FfSXlEMi1OUnNMZGl5SkE3eEhWYmI5eDgifQ.eyJuYmYiOjE3MDEzNjg5MDUsImV4cCI6MTcwMTM3MjUwNSwiaXNzIjoiaHR0cHM6Ly9hdXRoLmVtc2ljbG91ZC5jb20iLCJhdWQiOlsiZW1zaV9vcGVuIiwiaHR0cHM6Ly9hdXRoLmVtc2ljbG91ZC5jb20vcmVzb3VyY2VzIl0sImNsaWVudF9pZCI6Inl2eTJpNXh0NWRsb3o4djIiLCJlbWFpbCI6Im1lbWJlcnNoaXBzLm9udXJ5aWxtYXpAZ21haWwuY29tIiwiY29tcGFueSI6IklOVEVMIiwibmFtZSI6Ik9OVVIiLCJpYXQiOjE3MDEzNjg5MDUsInNjb3BlIjpbImVtc2lfb3BlbiJdfQ.MmmgVxMf2QpwXv4S7aK9dnocLEE7md15cnecsHXH1Pqxt7ebEB1qIbnsHOiH6HOpJrMvmTWzt6U5vHVZuTgvfHlgdcDiPvNmFAS4EKxVaMB7alEigW_JSEkgU-TgzWbVdaEvwZMJ92rnBrOvScl8UZv8NU0YuFY--2RjUKi6yVoFbcbZ_7OXd4_PH4v9itjoMtw8eaqLbPoZJmlMmr5KWPFHBHPXxphMvFYpAbcDixAxFvSLJ5rOJ74dswkhWTRteTWfhiQgPDEK1JxDICaM2HFpbnYrr-Iyn4w5DMznaMuwKupbrLrS4PLF0LwVqOlVl_Fmhe6oGUE0mYUEzwPSQQ"


        # Call the skill extraction function
        extracted_skills = extract_skills_from_document(access_token, document_text)
        skill_names = extract_skill_names(extracted_skills)

        # Display the extracted skills
        st.subheader("Extracted Skills:")
        st.write(skill_names)

if __name__ == "__main__":
    main()
