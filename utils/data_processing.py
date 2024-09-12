import re

def format_answer(correct_answer):
    formatted_answer = "### 정답:\n"
    
    img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    parts = re.split(img_pattern, correct_answer)
    
    for i, part in enumerate(parts):
        if i % 3 == 0:
            formatted_answer += part
        elif i % 3 == 1:
            pass
        else:
            formatted_answer += f'<img src="{part}" alt="이미지" class="responsive-img">'
    
    return formatted_answer