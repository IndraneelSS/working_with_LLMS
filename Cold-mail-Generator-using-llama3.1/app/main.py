import streamlit as st

st.title("📧 Cold Mail Generator")
url_input = st.text_input("Enter a URL:", value="https://www.amazon.jobs/en/jobs/2751331/language-data-scientist-ii?cmpid=SPLICX0248M&utm_source=linkedin.com&utm_campaign=cxro&utm_medium=social_media&utm_content=job_posting&ss=paid")
submit_button = st.button("Submit")


if submit_button:
    st.code("Hello Hiring Manager, I am from AtilQ",language = 'markdown')