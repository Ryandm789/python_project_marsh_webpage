from PIL import Image
import requests
import streamlit as st
#from streamlit_lottie import st_lottie


st.set_page_config(page_title= "My Webpage", page_icon=":tada:", layout="wide")



# ---- LOAD ASSETS ----
img_contact_form1 = Image.open("images/pexels-josh-sorenson-1714202.png")
img_contact_form2 = Image.open("images/pexels-luis-gomes-546819.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Ryan D. Marsh :wave:")
    st.title("A Senior BI & DATA Operations Analyst Manag.")
    st.write("""I am passionate about new tech and products that push the limitations in the world of analytics. 
I find enjoyment in driving business decisions with backend data facts that ingnites innovation.""")
    st.write("Continuing to push limitations is the only way to see improvement.")
    st.write("[Learn More>](http:pythonprojectmarshwebpage-bufsnzzsiazubozecly4iwcom)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns((1,2))
    with left_column:
        st.header("What am I passionate about?")
        st.write(""" In the dynamic world of BI and Data Analytics, the fusion of healthcare and military sectors ignites a passionate pursuit of knowledge,
where data becomes the compass guiding us to optimize patient care and enhance national security, transforming lives and safeguarding our future.
- Business Intelligence Analytics
- Business Data Analysis
- Business AdHoc Querying/Reporting
- Data Analytics: Descriptive, Diagnostic, Predictive & Prescriptive analysis
- Data pipeline: Data Extraction, Data Transformation, Data Loading, Data Orchestration guidelines
- Visualization tools and program languages supporting organization approach and goals""") 
        image_column, right_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form2)

# ---- Projects ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form1)
    with text_column:
        st.subheader("Professional Websites")
        st.write("""Current position, certifications, listed projects, responsibilities and accomplishments""")
        st.markdown("""[Click LinkedIn Profile...] (https://www.linkedin.com/in/ryan-d-marsh-msha-cssbb-csbi-298435125/)
                    (https://github.com/Ryandm789/python_project_marsh_webpage/tree/main)""")
        
# ---- Contact ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

