import streamlit as st
import os

# ----------------------------------
# Streamlit UI
# ----------------------------------
st.set_page_config(page_title="Prompt-to-Production", layout="wide")
st.title("Prompt-to-Production")
st.write("Generate production-ready FastAPI backends from a single prompt.")

prompt = st.text_area("Describe the backend you want")

# ----------------------------------
# Generator function
# ----------------------------------
def create_project(ai_output):
    """
    Takes formatted AI output (dummy or real)
    and creates files inside 'generated_project'
    """
    os.makedirs("generated_project", exist_ok=True)

    # Split files by ### filename
    files = ai_output.split("### ")[1:]  # skip any text before first ###
    for file in files:
        name, content = file.split("\n", 1)
        filepath = os.path.join("generated_project", name.strip())
        with open(filepath, "w") as f:
            f.write(content)

# ----------------------------------
# Button Action
# ----------------------------------
if st.button("Generate Backend"):

    # ----------------------------------
    # DUMMY AI OUTPUT
    # ----------------------------------
    output = f"""
### main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {{"message": "Hello World - generated for: {prompt}"}}

### requirements.txt
fastapi==0.110.0
uvicorn==0.29.0

### Dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

### README.md
# Prompt-to-Production Demo
Generated project based on user input:
{prompt}

This project demonstrates:
- Modular FastAPI backend
- Docker-ready environment
- Production-oriented folder structure
- README auto-generated
"""

    # Create files in local folder
    create_project(output)

    # Display code to user
    st.code(output)

    # Success message
    st.success("Project created in /generated_project 🚀")
