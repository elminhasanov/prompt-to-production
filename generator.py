import os
import re

def create_project(ai_output):

    os.makedirs("generated_project", exist_ok=True)

    files = re.split(r"### ", ai_output)[1:]

    for file in files:
        name, content = file.split("\n", 1)
        filepath = os.path.join("generated_project", name.strip())

        with open(filepath, "w") as f:
            f.write(content)
