LOGO_SMALL_IMG_PATH = './static/image/77604750.png'
BANER_IMG_PATH = './static/image/logo.png'

# MD 파일이 있는 폴더 경로
MD_DIR_PATH = 'answers'

# CSS 스타일을 정의합니다.
DEFAULT_CSS = """
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

# MD 파일 이름과 한글 표시 이름을 매핑하는 딕셔너리 (키와 값을 바꿈)
MD_FILE_NAMES = {
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