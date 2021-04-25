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

- 딥러닝은 무엇인가요? 딥러닝과 머신러닝의 차이는?
- Cost Function과 Activation Function은 무엇인가요?
- Tensorflow, PyTorch 특징과 차이가 뭘까요?
- Data Normalization은 무엇이고 왜 필요한가요?
- 알고있는 Activation Function에 대해 알려주세요. (Sigmoid, ReLU, LeakyReLU, Tanh 등)
- 오버피팅일 경우 어떻게 대처해야 할까요?
- 하이퍼 파라미터는 무엇인가요?
- Weight Initialization 방법에 대해 말해주세요. 그리고 무엇을 많이 사용하나요?
- 볼츠만 머신은 무엇인가요?
- TF, PyTorch 등을 사용할 때 디버깅 노하우는?
- 뉴럴넷의 가장 큰 단점은 무엇인가? 이를 위해 나온 One-Shot Learning은 무엇인가?
- 요즘 Sigmoid 보다 ReLU를 많이 쓰는데 그 이유는?
  - Non-Linearity라는 말의 의미와 그 필요성은?
  - ReLU로 어떻게 곡선 함수를 근사하나?
  - ReLU의 문제점은?
  - Bias는 왜 있는걸까?
- Gradient Descent에 대해서 쉽게 설명한다면?
  - 왜 꼭 Gradient를 써야 할까? 그 그래프에서 가로축과 세로축 각각은 무엇인가? 실제 상황에서는 그 그래프가 어떻게 그려질까?
  - GD 중에 때때로 Loss가 증가하는 이유는?
  - Back Propagation에 대해서 쉽게 설명 한다면?
- Local Minima 문제에도 불구하고 딥러닝이 잘 되는 이유는?
  - GD가 Local Minima 문제를 피하는 방법은?
  - 찾은 해가 Global Minimum인지 아닌지 알 수 있는 방법은?
- Training 세트와 Test 세트를 분리하는 이유는?
  - Validation 세트가 따로 있는 이유는?
  - Test 세트가 오염되었다는 말의 뜻은?
  - Regularization이란 무엇인가?
- Batch Normalization의 효과는?
  - Dropout의 효과는?
  - BN 적용해서 학습 이후 실제 사용시에 주의할 점은? 코드로는?
  - GAN에서 Generator 쪽에도 BN을 적용해도 될까?
- SGD, RMSprop, Adam에 대해서 아는대로 설명한다면?
  - SGD에서 Stochastic의 의미는?
  - 미니배치를 작게 할때의 장단점은?
  - 모멘텀의 수식을 적어 본다면?
- 간단한 MNIST 분류기를 MLP+CPU 버전으로 numpy로 만든다면 몇줄일까?
  - 어느 정도 돌아가는 녀석을 작성하기까지 몇시간 정도 걸릴까?
  - Back Propagation은 몇줄인가?
  - CNN으로 바꾼다면 얼마나 추가될까?
- 간단한 MNIST 분류기를 TF, PyTorch 등으로 작성하는데 몇시간이 필요한가?
  - CNN이 아닌 MLP로 해도 잘 될까?
  - 마지막 레이어 부분에 대해서 설명 한다면?
  - 학습은 BCE loss로 하되 상황을 MSE loss로 보고 싶다면?
- 딥러닝할 때 GPU를 쓰면 좋은 이유는?
  - 학습 중인데 GPU를 100% 사용하지 않고 있다. 이유는?
  - GPU를 두개 다 쓰고 싶다. 방법은?
  - 학습시 필요한 GPU 메모리는 어떻게 계산하는가?

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
