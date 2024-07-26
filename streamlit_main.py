import os
import streamlit as st

def read_md_files(folder_path, filename):
    quiz_data = []
    filepath = os.path.join(folder_path, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
        parts = content.split('---')
        for part in parts:
            if '## #' in part:
                num = part.split('##')[1].strip()[1:]
                question = part.split('###')[1].strip().split('\n\n')[0]
                answer = "".join(part.split(question)[1:])
                quiz_data.append({"num" : num, "question": f"{num}_{question}", "answer": answer})
    return quiz_data


# Streamlit 애플리케이션
# st.title("퀴즈 애플리케이션")

# MD 파일이 있는 폴더 경로
folder_path = 'answers'

# MD 파일 목록 가져오기
md_files = [f for f in os.listdir(folder_path) if f.endswith('.md')]
md_files = sorted(md_files)

# MD 파일 선택
selected_file = st.selectbox("MD 파일을 선택하세요", md_files)

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
        st.markdown(f"### 정답:\n{correct_answer}")
