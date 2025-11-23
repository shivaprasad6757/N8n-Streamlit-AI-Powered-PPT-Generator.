import streamlit as st
import requests
import subprocess

# step 1:Title of the web app
st.title("📝PowerPointPresentation")
st.subheader(":blue[Generate PPT slides using AI 🤖]")


#step 2:Input of the user
user_input = st.text_area("write your content here to generate ppt slides")

#step 3:button to generate ppt
if st.button("Generate PPT"): # To generate ppt
    if user_input: #The user should enter some text
        response = requests.post(url="https://shivan8n12.app.n8n.cloud/webhook-test/3d1e48f5-10e8-404e-b2fb-dfec49f0c806",
                                 json={"user_input":user_input})
        
        if response.status_code == 200: #The  request was successful
            st.write("success") #python-pptx code
            
            with open("generated_code.py", "w", encoding="utf-8") as f1:
                f1.write(response.json()["output"].strip("```python"))

                
            #step 4:run the presentation.py file to generate ppt
            subprocess.run(["python","generated_code.py"]) # The subprocess is process it can python file inside the python file

            with open(r"C:\innomatics\classes web application n8n\PPT Project using Streamlit and N8n\ppt_files\new_ppt.pptx", "rb") as f: #To read the ppt file
                st.download_button(label="Download PPT file", #To download the ppt file
                                   data=f,
                                   file_name="presentation.pptx"
                )