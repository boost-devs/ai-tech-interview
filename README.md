<div align="center"> 
    <img src="logo.png" alt="logo"/>
</div>

## [👉 Discussions](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/discussions)

스터디 방식, 스터디 기록, QnA는 모두 Discussions에서 작성됩니다!

---

## Table of Contents

- [Part 1. Data Science](#part-1-data-science)
  - [Statistics/Math](#-statisticsmath)
  - [Machine Learning](#-machine-learning)
  - [Deep Learning](#-deep-learning)
- [Part 2. Language](#part-2-language)
  - [Python](#-python)
- [Part 3. CS](#part-3-cs)
  - [Network](#-network)
  - [Operating System](#-operating-system)
  - [Algorithm](#-algorithm)
- [References](#references)

---

## Part 1. Data Science

### [📈 Statistics/Math](./answers/statistics-math.md)

- 고유값(eigen value)와 고유벡터(eigen vector)에 대해 설명해주세요. 그리고 왜 중요할까요?
- 샘플링(Sampling)과 리샘플링(Resampling)에 대해 설명해주세요. 리샘플링은 무슨 장점이 있을까요?
- 확률 모형과 확률 변수는 무엇일까요?
- 누적 분포 함수와 확률 밀도 함수는 무엇일까요? 수식과 함께 표현해주세요.
- 조건부 확률은 무엇일까요?
- 공분산과 상관계수는 무엇일까요? 수식과 함께 표현해주세요.
- 신뢰 구간의 정의는 무엇인가요?
- p-value를 모르는 사람에게 설명한다면 어떻게 설명하실 건가요?
- R square의 의미는 무엇인가요?
- 평균(mean)과 중앙값(median)중에 어떤 케이스에서 뭐를 써야할까요?
- 중심극한정리는 왜 유용한걸까요?
- 엔트로피(entropy)에 대해 설명해주세요. 가능하면 Information Gain도요.
- 어떨 때 모수적 방법론을 쓸 수 있고, 어떨 때 비모수적 방법론을 쓸 수 있나요?
- “likelihood”와 “probability”의 차이는 무엇일까요?
- 통계에서 사용되는 bootstrap의 의미는 무엇인가요.
- 모수가 매우 적은 (수십개 이하) 케이스의 경우 어떤 방식으로 예측 모델을 수립할 수 있을까요?
- 베이지안과 프리퀀티스트 간의 입장차이를 설명해주실 수 있나요?
- 검정력(statistical power)은 무엇일까요?
- missing value가 있을 경우 채워야 할까요? 그 이유는 무엇인가요?
- 아웃라이어의 판단하는 기준은 무엇인가요?
- 필요한 표본의 크기를 어떻게 계산합니까?
- Bias를 통제하는 방법은 무엇입니까?
- 로그 함수는 어떤 경우 유용합니까? 사례를 들어 설명해주세요.
- 베르누이 분포 / 이항 분포 / 카테고리 분포 / 다항 분포 / 가우시안 정규 분포 / t 분포 / 카이제곱 분포 / F 분포 / 베타 분포 / 감마 분포에 대해 설명해주세요. 그리고 분포 간의 연관성도 설명해주세요.
- 출장을 위해 비행기를 타려고 합니다. 당신은 우산을 가져가야 하는지 알고 싶어 출장지에 사는 친구 3명에게 무작위로 전화를 하고 비가 오는 경우를 독립적으로 질문해주세요. 각 친구는 2/3로 진실을 말하고 1/3으로 거짓을 말합니다. 3명의 친구가 모두 “그렇습니다. 비가 내리고 있습니다”라고 말했습니다. 실제로 비가 내릴 확률은 얼마입니까?

<a href='#table-of-contents'><strong><small>목차로 돌아가기</small></strong></a>

<br/>

### [🤖 Machine Learning](./answers/machine-learning.md)

- 알고 있는 metric에 대해 설명해주세요. (ex. RMSE, MAE, recall, precision ...)
- 정규화를 왜 해야할까요? 정규화의 방법은 무엇이 있나요?
- Local Minima와 Global Minima에 대해 설명해주세요.
- 차원의 저주에 대해 설명해주세요.
- dimension reduction기법으로 보통 어떤 것들이 있나요?
- PCA는 차원 축소 기법이면서, 데이터 압축 기법이기도 하고, 노이즈 제거기법이기도 합니다. 왜 그런지 설명해주실 수 있나요?
- LSA, LDA, SVD 등의 약자들이 어떤 뜻이고 서로 어떤 관계를 가지는지 설명할 수 있나요?
- Markov Chain을 고등학생에게 설명하려면 어떤 방식이 제일 좋을까요?
- 텍스트 더미에서 주제를 추출해야 합니다. 어떤 방식으로 접근해 나가시겠나요?
- SVM은 왜 반대로 차원을 확장시키는 방식으로 동작할까요? SVM은 왜 좋을까요?
- 다른 좋은 머신 러닝 대비, 오래된 기법인 나이브 베이즈(naive bayes)의 장점을 옹호해보세요.
- 회귀 / 분류시 알맞은 metric은 무엇일까?
- Association Rule의 Support, Confidence, Lift에 대해 설명해주세요.
- 최적화 기법중 Newton’s Method와 Gradient Descent 방법에 대해 알고 있나요?
- 머신러닝(machine)적 접근방법과 통계(statistics)적 접근방법의 둘간에 차이에 대한 견해가 있나요?
- 인공신경망(deep learning이전의 전통적인)이 가지는 일반적인 문제점은 무엇일까요?
- 지금 나오고 있는 deep learning 계열의 혁신의 근간은 무엇이라고 생각하시나요?
- ROC 커브에 대해 설명해주실 수 있으신가요?
- 여러분이 서버를 100대 가지고 있습니다. 이때 인공신경망보다 Random Forest를 써야하는 이유는 뭘까요?
- K-means의 대표적 의미론적 단점은 무엇인가요? (계산량 많다는것 말고)
- L1, L2 정규화에 대해 설명해주세요.
- Cross Validation은 무엇이고 어떻게 해야하나요?
- XGBoost을 아시나요? 왜 이 모델이 캐글에서 유명할까요?
- 앙상블 방법엔 어떤 것들이 있나요?
- feature vector란 무엇일까요?
- 좋은 모델의 정의는 무엇일까요?
- 50개의 작은 의사결정 나무는 큰 의사결정 나무보다 괜찮을까요? 왜 그렇게 생각하나요?
- 스팸 필터에 로지스틱 리그레션을 많이 사용하는 이유는 무엇일까요?
- OLS(ordinary least squre) regression의 공식은 무엇인가요?

<a href='#table-of-contents'><strong><small>목차로 돌아가기</small></strong></a>

<br/>

### [🧠 Deep Learning](./answers/deep-learning.md)

<a href='#table-of-contents'><strong><small>목차로 돌아가기</small></strong></a>

---

## Part 2. Language

### [🐍 Python](./answers/python.md)

<a href='#table-of-contents'><strong><small>목차로 돌아가기</small></strong></a>

---

## Part 3. CS

### [🌐 Network](./answers/network.md)

<a href='#table-of-contents'><strong><small>목차로 돌아가기</small></strong></a>

<br/>

### [🖥️ Operating System](./answers/operating-system.md)

<a href='#table-of-contents'><strong><small>목차로 돌아가기</small></strong></a>

<br/>

### [🔻 Algorithm](./answers/algorithm.md)

<a href='#table-of-contents'><strong><small>목차로 돌아가기</small></strong></a>

---

## References

- [zzsza님의 Datascience-Interview-Questions](https://github.com/zzsza/Datascience-Interview-Questions)
- [DopplerHQ님의 awesome-interview-questions](https://github.com/DopplerHQ/awesome-interview-questions)
- [JaeYeopHan님의 Interview_Question_for_Beginner](https://github.com/JaeYeopHan/Interview_Question_for_Beginner)
- [WeareSoft님의 tech-interview](https://github.com/WeareSoft/tech-interview)
