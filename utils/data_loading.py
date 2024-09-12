from PIL import Image

import streamlit as st
import os


@st.cache_data
def load_img_data(logo_img_path, logo_small_img_path):
    
    banner_image = Image.open(logo_img_path)
    icon_image = Image.open(logo_small_img_path)

    return banner_image, icon_image

@st.cache_data
def read_md_files(folder_path, filename):
    quiz_data = []
    filepath = os.path.join(folder_path, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        parts = content.split('\n---\n')
        for part in parts:
            if '## #' in part:
                num = part.split('##')[1].strip()[1:]
                question = part.split('###')[1].strip().split('\n\n')[0]
                answer = "".join(part.split(question)[1:])
                quiz_data.append({"num" : num, "question": f"{num}_{question}", "answer": answer})
    return quiz_data