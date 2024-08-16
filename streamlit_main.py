import os
import streamlit as st
import re
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

# CSS 스타일을 정의합니다.
css = """
<style>
    .responsive-img {
        max-width: 100%;
        height: auto;
    }
    @media (max-width: 600px) {
        .responsive-img {
            width: 100%;
        }
    }
</style>
"""

# Streamlit 애플리케이션
# MD 파일 이름과 한글 표시 이름을 매핑하는 딕셔너리 (키와 값을 바꿈)
md_file_names = {
    "통계-수학": "1-statistics-math.md",
    "머신 러닝": "2-machine-learning.md",
    "딥 러닝": "3-deep-learning.md",
    "Python": "4-python.md",
    "네트워크": "5-network.md",
    "운영체제": "6-operating-system.md",
    "자료구조": "7-data-structure.md",
    "알고리즘": "8-algorithm.md",
    "통계-수학 분포": "statistics-math-distribution.md"
}



# MD 파일이 있는 폴더 경로
folder_path = 'answers'

# MD 파일 목록 가져오기
md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
md_files = sorted(md_files)

# 페이지가 로드될 때 CSS를 한 번만 삽입합니다.
st.markdown(css, unsafe_allow_html=True)

# 사이드바에 MD 파일 선택 라디오 버튼 추가
with st.sidebar:
    selected_file_name = st.radio(
        "주제를 선택하세요",
        options=list(md_file_names.keys()),
        format_func=lambda x: x
    )
    
    # 선택된 한글 이름을 파일 이름으로 변환
    selected_file = md_file_names[selected_file_name]

# 선택한 파일에서 퀴즈 데이터 읽기
if selected_file:
    quiz_data = read_md_files(folder_path, selected_file)
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
    # 정답 텍스트를 처리합니다.
    formatted_answer = "### 정답:\n"
    
    # 정규 표현식을 사용하여 이미지 태그를 찾습니다.
    img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    parts = re.split(img_pattern, correct_answer)
    
    for i, part in enumerate(parts):
        if i % 3 == 0:
            # 일반 텍스트
            formatted_answer += part
        elif i % 3 == 1:
            # 이미지 대체 텍스트 (사용하지 않음)
            pass
        else:
            # 이미지 URL
            formatted_answer += f'<img src="{part}" alt="이미지" class="responsive-img">'
    
    # 형식이 지정된 답변을 표시합니다.
    st.markdown(formatted_answer, unsafe_allow_html=True)
