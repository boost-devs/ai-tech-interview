import os
import streamlit as st
import re
from utils.data_loading import load_img_data, read_md_files
from utils.data_processing import format_answer
from config.constants import MD_DIR_PATH, LOGO_SMALL_IMG_PATH, BANER_IMG_PATH, DEFAULT_CSS, MD_FILE_NAMES


st.set_page_config(
    page_title="AI TECH INTERVIEW",
    page_icon=LOGO_SMALL_IMG_PATH,
    layout="wide",
)

banner_image, icon_image = load_img_data(BANER_IMG_PATH, LOGO_SMALL_IMG_PATH)

# 로고 표시
st.logo(banner_image, icon_image=icon_image)

# 페이지가 로드될 때 CSS를 한 번만 삽입합니다.
st.markdown(DEFAULT_CSS, unsafe_allow_html=True)

# 사이드바에 MD 파일 선택 라디오 버튼 추가
with st.sidebar:
    selected_file_name = st.radio(
        "주제를 선택하세요",
        options=list(MD_FILE_NAMES.keys()),
        format_func=lambda x: x
    )
    
    # 선택된 한글 이름을 파일 이름으로 변환
    selected_file = MD_FILE_NAMES[selected_file_name]

# 선택한 파일에서 퀴즈 데이터 읽기
if selected_file:
    quiz_data = read_md_files(MD_DIR_PATH, selected_file)
    questions = [q['question'] for q in quiz_data]

    # 문제 선택
    selected_question = st.selectbox("문제를 선택하세요", questions)
    st.write("\n\n\n\n"+selected_question)
    # 선택한 문제에 해당하는 정답 찾기
    for q in quiz_data:
        if q['question'] == selected_question:
            correct_answer = q['answer']
            break

# 정답 버튼
if st.button("정답 확인"):
    formatted_answer = format_answer(correct_answer)
    st.markdown(formatted_answer, unsafe_allow_html=True)
