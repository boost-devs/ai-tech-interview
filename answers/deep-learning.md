## 📝 Table of Contents

- [딥러닝은 무엇인가요? 딥러닝과 머신러닝의 차이는?](#1)
- [Cost Function과 Activation Function은 무엇인가요?](#2)
- [Tensorflow, PyTorch 특징과 차이가 뭘까요?](#3)
- [Data Normalization은 무엇이고 왜 필요한가요?](#4)
- [알고있는 Activation Function에 대해 알려주세요. (Sigmoid, ReLU, LeakyReLU, Tanh 등)](#5)
- [오버피팅일 경우 어떻게 대처해야 할까요?](#6)
- [하이퍼 파라미터는 무엇인가요?](#7)
- [Weight Initialization 방법에 대해 말해주세요. 그리고 무엇을 많이 사용하나요?](#8)
- [볼츠만 머신은 무엇인가요?](#9)
- [TF, PyTorch 등을 사용할 때 디버깅 노하우는?](#10)
- [뉴럴넷의 가장 큰 단점은 무엇인가? 이를 위해 나온 One-Shot Learning은 무엇인가?](#11)
- [요즘 Sigmoid 보다 ReLU를 많이 쓰는데 그 이유는?](#12)
  - [Non-Linearity라는 말의 의미와 그 필요성은?](#12-1)
  - [ReLU로 어떻게 곡선 함수를 근사하나?](#12-2)
  - [ReLU의 문제점은?](#12-3)
  - [Bias는 왜 있는걸까?](#12-4)
- [Gradient Descent에 대해서 쉽게 설명한다면?](#13)
  - [왜 꼭 Gradient를 써야 할까? 그 그래프에서 가로축과 세로축 각각은 무엇인가? 실제 상황에서는 그 그래프가 어떻게 그려질까?](#13-1)
  - [GD 중에 때때로 Loss가 증가하는 이유는?](#13-2)
  - [Back Propagation에 대해서 쉽게 설명 한다면?](#13-3)
- [Local Minima 문제에도 불구하고 딥러닝이 잘 되는 이유는?](#14)
  - [GD가 Local Minima 문제를 피하는 방법은?](#14-1)
  - [찾은 해가 Global Minimum인지 아닌지 알 수 있는 방법은?](#14-2)
- [Training 세트와 Test 세트를 분리하는 이유는?](#15)
  - [Validation 세트가 따로 있는 이유는?](#15-1)
  - [Test 세트가 오염되었다는 말의 뜻은?](#15-2)
  - [Regularization이란 무엇인가?](#15-3)
- [Batch Normalization의 효과는?](#16)
  - [Dropout의 효과는?](#16-1)
  - [BN 적용해서 학습 이후 실제 사용시에 주의할 점은? 코드로는?](#16-2)
  - [GAN에서 Generator 쪽에도 BN을 적용해도 될까?](#16-3)
- [SGD, RMSprop, Adam에 대해서 아는대로 설명한다면?](#17)
  - [SGD에서 Stochastic의 의미는?](#17-1)
  - [미니배치를 작게 할때의 장단점은?](#17-2)
  - [모멘텀의 수식을 적어 본다면?](#17-3)
- [간단한 MNIST 분류기를 MLP+CPU 버전으로 numpy로 만든다면 몇줄일까?](#18)
  - [어느 정도 돌아가는 녀석을 작성하기까지 몇시간 정도 걸릴까?](#18-1)
  - [Back Propagation은 몇줄인가?](#18-2)
  - [CNN으로 바꾼다면 얼마나 추가될까?](#18-3)
- [간단한 MNIST 분류기를 TF, PyTorch 등으로 작성하는데 몇시간이 필요한가?](#19)
  - [CNN이 아닌 MLP로 해도 잘 될까?](#19-1)
  - [마지막 레이어 부분에 대해서 설명 한다면?](#19-2)
  - [학습은 BCE loss로 하되 상황을 MSE loss로 보고 싶다면?](#19-3)
- [딥러닝할 때 GPU를 쓰면 좋은 이유는?](#20)
  - [학습 중인데 GPU를 100% 사용하지 않고 있다. 이유는?](#20-1)
  - [GPU를 두개 다 쓰고 싶다. 방법은?](#20-2)
  - [학습시 필요한 GPU 메모리는 어떻게 계산하는가?](#20-3)

---

## #1

#### 딥러닝은 무엇인가요? 딥러닝과 머신러닝의 차이는?

**딥러닝이란** 여러 층을 가진 인공신경망(Artificial Neural Network, ANN)을 사용하여 머신러닝 학습을 수행하는 것으로, 심층학습이라고도 부른다.

> 딥러닝은 엄밀히 말하자면 머신러닝에 포함되는 개념이다. 따라서 전통적인 머신러닝 기법과 딥러닝 기법의 차이를 설명하고자 한다.  

> 인공신경망, 퍼셉트론에 대한 내용은 [reference](http://tcpschool.com/deep2018/deep2018_deeplearning_intro)를 참고

**머신러닝과 딥러닝의 가장 큰 차이점**은 다음과 같다. 기존 머신러닝에서는 학습하려는 데이터의 여러 특징 중에서 `어떤 특징을 추출할지 사람이 직접 분석하고 판단`해야하는 반면, 딥러닝에서는 기계가 `자동으로 학습하려는 데이터에서 특징을 추출`하여 학습하게 된다. 따라서 특징 추출에 사람이 개입(feature engineering)하면 머신러닝, 개입하지 않으면 딥러닝이다.
또한, 딥러닝은 머신러닝보다 큰 데이터셋과 긴 학습시간이 필요하다.

> **추가내용) AI, ML, DL**  

![ai_ml_dl](/images/sally/2021-05-01-02-44-22.png)

**인공지능이란** 인간이 가지고 있는 인식, 판단 등의 지적 능력을 모델링하여 컴퓨터에서 구현하는 것이다. 머신러닝, 딥러닝 외에도 다양한 분야가 인공지능 내에 포함된다.  

**머신러닝이란** 데이터를 기반으로 패턴을 학습하고 결과를 예측하는 알고리즘 기법이다. 머신러닝은 조건이 복잡하고 규칙이 다양한 경우에, 데이터를 기반으로 일정한/숨겨진 패턴을 찾아내서 문제를 해결한다. 머신러닝의 단점은 데이터에 매우 의존적이라는 것이다. 즉, 좋은 품질의 데이터를 갖추지 못하면 머신러닝 수행결과도 좋지 않다는 것이다.  

머신러닝은 아래와 같이 분류된다.  

- 지도학습
  - 분류, 회귀, 추천시스템, 시각/음성 인지(DL), 텍스트분석/NLP(DL)
- 비지도학습
  - 클러스터링, 차원축소, 강화학습

#### References

- [딥러닝, 데이터로 세상을 파악하다(1) - LG CNS](https://blog.lgcns.com/2212)
- [CH01)01.머신러닝의 개념 - 파이썬 머신러닝 완벽가이드(도서)](http://m.yes24.com/goods/detail/69752484)
- [9)딥러닝이란? - TCP SCHOOLS.com](http://tcpschool.com/deep2018/deep2018_deeplearning_intro)

---

## #2

#### Cost Function과 Activation Function은 무엇인가요?

#### References

---

## #3

#### Tensorflow, PyTorch 특징과 차이가 뭘까요?

#### References

---

## #4

#### Data Normalization은 무엇이고 왜 필요한가요?

**Data Normalization(데이터 정규화)이란** feature들의 분포(scale)을 조절하여 균일하게 만드는 방법이다. 데이터 정규화가 필요한 이유는 데이터 feature 간 scale 차이가 심하게 날 때, 큰 범위를 가지는 feature(ex. 가격)가 작은 범위를 가지는 feature(ex. 나이)보다 더 강하게 모델에 반영될 수 있기 때문이다.  
즉, 데이터 정규화는 모든 데이터 포인트가 동일한 정도의 스케일(중요도)로 반영되도록 하는 역할을 수행하며, 아래와 같은 장점을 얻을 수 있다.  

- 학습속도가 개선된다.
- 노이즈가 작아지므로 오버피팅을 억제시킨다.
- 데이터를 덜 치우치게 만드므로, 좋은 성능을 보인다.

![data normalization](/images/sally/2021-05-01-16-15-42.png)

> **추가내용) Regularization, Normalization, Standardization**

**Regularization(정규화, 규제)** 란 모델에 제약(penalty)를 주어 모델의 복잡성을 낮추고, 이를 통해 오버피팅을 방지하는 방법이다. 제약을 사용하면 학습 정확도(train accuracy)는 조금 낮아질 수 있지만, 테스트 정확도(test accuracy)를 높일 수 있다. 정규화에는 `Drop out, Early Stopping, Weight decay, Prameter Norm Penalty`와 같은 방법이 존재한다.  
- 자세한 Regularization 방법은 [reference](https://bsm8734.github.io/posts/bc-d012-3-dlbasic-optimization-regularization/) 참고

**Normalization, Standardization**은 모두 데이터의 범위(scale)을 축소하는 방법이다.(re-scaling) 데이터의 범위 재조정이 필요한 이유는 `데이터의 범위가 너무 넓은 곳에 퍼져있을 때(scale이 크다면), 데이터셋이 outlier를 지나치게 반영`하여 오버피팅이 될 가능성이 높기 때문이다. 두 방법은 scale 조절 방식에 차이가 존재한다.  

**Normalization(정규화)** 방법에는 Batch Normalization, Min-Max Normalization 등이 있다.

- `Batch Normalization`: 적용시키려는 레이어의 통계량, 분포를 정규화시키는 방법이다.
- `Min-Max Normalization`: 모든 데이터 중에서 가장 작은 값을 0, 가장 큰 값을 1로 두고, 나머지 값들은 비율을 맞춰서 모두 0과 1 사이의 값으로 스케일링하는 방법이다. 모든 feature들의 스케일이 동일하지만, 이상치(outlier)를 잘 처리하지 못한다. 식은 아래와 같다.
  <!-- $x= {{x - x_{min}} \over {x_{max} - x_{min}}}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x%3D%20%7B%7Bx%20-%20x_%7Bmin%7D%7D%20%5Cover%20%7Bx_%7Bmax%7D%20-%20x_%7Bmin%7D%7D%7D">

**Standardization(표준화)** 란 표준화 확률변수를 구하는 방법이다. 이는 `z-score를 구하는 방법`을 의미한다. z-score normalization이라 불리기도 한다.

- `Z-score`: 관측값이 평균 기준으로 얼마나 떨어져있는지 나타낼 때 사용한다. 각 데이터에서 데이터 전체의 평균을 빼고, 이를 표준편차로 나누는 방식이다. 이상치(outlier)를 잘 처리하지만, 정확히 동일한 척도로 정규화 된 데이터를 생성하지는 않는다. 식은 아래와 같다.
  <!-- $z-score = {x-{\mu} \over {\sigma}}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=z-score%20%3D%20%7Bx-%7B%5Cmu%7D%20%5Cover%20%7B%5Csigma%7D%7D">  


#### References

- [딥러닝 기초 Optimization_Regularization - Sally blog](https://bsm8734.github.io/posts/bc-d012-3-dlbasic-optimization-regularization/)
- [머신 러닝_Normalization, Standardization, Regularization 비교 - 프로그래밍 학습 블로그](https://m.blog.naver.com/qbxlvnf11/221476122182)
- [정규화(Normalization) 쉽게 이해하기 - 아무튼 워라벨](http://hleecaster.com/ml-normalization-concept/)
- [정규화(Normalization)의 목적과 방법들 - Deep Learning with Writing](https://mole-starseeker.tistory.com/31)
- [데이터 일반화 vs 표준화 (Normalization and Standardization of Data) - 컴퓨터와 수학, 몽상 조금](https://skyil.tistory.com/50)

---

## #5

#### 알고있는 Activation Function에 대해 알려주세요. (Sigmoid, ReLU, LeakyReLU, Tanh 등)

#### References

---

## #6

#### 오버피팅일 경우 어떻게 대처해야 할까요?

#### References

---

## #7

#### 하이퍼 파라미터는 무엇인가요?

하이퍼 파라미터(Hyper-parameter)는 모델링할 때, **사용자가 직접 세팅해주는 값**을 뜻한다. 하이퍼 파라미터는 정해진 최적의 값이 없으며, 사용자의 선험적 지식을 기반으로 설정(휴리스틱)한다. 하이퍼 파라미터 튜닝 기법에는 Manual Search, Grid Search, Random Search, Bayesian Optimization 등이 있다. 딥러닝에서의 하이퍼 파라미터는 아래의 그림을 참고한다.  

![hyper-parameter](/images/sally/2021-05-01-16-23-27.png)

> **추가내용) 파라미터 vs. 하이퍼 파라미터**  

파라미터와 하이퍼 파라미터를 구분하는 기준은 사용자가 직접 설정하느냐 아니냐이다. **사용자가 직접 설정하면 하이퍼 파라미터, 모델 혹은 데이터에 의해 결정되면 파라미터**이다.
딥러닝에서 하이퍼 파라미터는 `학습률, 배치 크기, 은닉층의 개수` 등이 있고, 파라미터는 `가중치, 편향` 등이 있다.  
![parameter_vs_hyperParameter](/images/sally/2021-05-01-16-27-17.png)  

#### References

- [13.파라미터(Parameter)와 하이퍼 파라미터(Hyper parameter) - 귀퉁이 서재](https://bkshin.tistory.com/entry/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-13-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0Parameter%EC%99%80-%ED%95%98%EC%9D%B4%ED%8D%BC-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0Hyper-parameter)
- [하이퍼파라미터(Hyperparameter) - 도리의 디지털라이프](http://blog.skby.net/%ED%95%98%EC%9D%B4%ED%8D%BC%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-hyperparameter/)

---

## #8

#### Weight Initialization 방법에 대해 말해주세요. 그리고 무엇을 많이 사용하나요?

#### References

---

## #9

#### 볼츠만 머신은 무엇인가요?

#### References

---

## #10

#### TF, PyTorch 등을 사용할 때 디버깅 노하우는?

오류가 발생하는 곳, 중요한 데이터가 바뀌는 지점을 디버깅 포인트로 두고, 확인하는 방법이 있다. 또, IDE에서 다양한 디버깅 extension을 지원하기 때문에 이를 잘 활용하면 좋은 인사이트를 얻을 수 있다. 예를들어, vs code의 jupyter extension을 사용하면 데이터 프레임, 변수값등을 보기 쉽게 정렬하여 확인할 수 있다.  

> 디버깅 노하우도 중요하지만, 오류에 대한 대처방식을 익히면 좋다. 디버깅 하지 않고 오류에 대처할 수 있으므로, 디버깅 시간을 아껴준다. 예를들어, 딥러닝 학습을 위한 코드를 작성할 때, 가장 많이 발생하는 오류는 CUDA out of memory와 shape 오류이다.(개인적인 의견) out of memory와 같은 오류는 배치 사이즈를 줄인다거나, 입력 데이터의 사이즈를 줄이는 방식으로 해결할 수 있다. shape 오류는 디버깅을 통해서 현재 입력 데이터의 shape, type등을 확인하고, 함수의 파라미터가 요구하는 shape, type에 맞게 변형하는 과정이 필요하다.  

> 추가적으로 딥러닝 디버깅 툴은 아니지만, logging tool로서 tensorboard, wandb 등이 매우 유용하게 사용될 수 있다.

#### References

---

## #11

#### 뉴럴넷의 가장 큰 단점은 무엇인가? 이를 위해 나온 One-Shot Learning은 무엇인가?

#### References

---

## #12

#### 요즘 Sigmoid 보다 ReLU를 많이 쓰는데 그 이유는?

#### References

---

## #12-1

#### Non-Linearity라는 말의 의미와 그 필요성은?

#### References

---

## #12-2

#### ReLU로 어떻게 곡선 함수를 근사하나?

#### References

---

## #12-3

#### ReLU의 문제점은?

#### References

---

## #12-4

#### Bias는 왜 있는걸까?

#### References

---

## #13

#### Gradient Descent에 대해서 쉽게 설명한다면?

#### References

---

## #13-1

#### 왜 꼭 Gradient를 써야 할까? 그 그래프에서 가로축과 세로축 각각은 무엇인가? 실제 상황에서는 그 그래프가 어떻게 그려질까?

#### References

---

## #13-2

#### GD 중에 때때로 Loss가 증가하는 이유는?

#### References

---

## #13-3

#### Back Propagation에 대해서 쉽게 설명 한다면?

#### References

---

## #14

#### Local Minima 문제에도 불구하고 딥러닝이 잘 되는 이유는?

local minima 문제가 사실은 고차원(High Dimensional)의 공간에서는 발생하기 힘든, 매우 희귀한 경우이기 때문이다. 실제 딥러닝 모델에서는 weight가 수도없이 많으며, 그 수많은 weight가 모두 local minima에 빠져야 weight update가 정지되기 때문에 local minima는 큰 문제가 되지 않는다.  

![high-dim-minima](/images/sally/2021-05-01-17-08-37.png)

> **추가자료) Local minima**  

Local minima 문제는 에러를 최소화시키는 최적의 파라미터를 찾는 문제에 있어서 아래 그림처럼 파라미터 공간에 수많은 지역적인 홀(hole)들이 존재하여 이러한 local minima에 빠질 경우 전역적인 해(global minimum)를 찾기 힘들게 되는 문제를 일컫는다.  

<img src="/images/sally/2021-05-01-16-53-57.png" width="70%">  

> **Critical point, Saddle point, Local minima**

![minima-maxima-saddle_point](/images/sally/2021-05-01-17-14-39.png)

용어에 대해서 먼저 언급하면 아래와 같다.

- critical point: 일차 미분이 0인 지점
- local minimum: 모든 방향에서 극소값을 만족하는 점
- global minimum: 모든 방향에서 극대값을 만족하는 점
- saddle point: 어느 방향에서 보면 극대값이지만 다른 방향에서 보면 극소값이 되는 점

> **Local Minima 문제에도 불구하고 딥러닝이 잘 되는, 더 구체적인 이유**

고차원의 공간에서 모든 축의 방향으로 오목한 형태가 형성될 확률은 거의 0에 가깝다. 따라서, 고차원의 공간에서 대부분의 critical point는 local minima가 아니라 saddle point다. 그리고, 고차원의 공간에서 설령 local minima가 발생한다 하더라도 이는 global minimum이거나 또는 global minimum과 거의 유사한 수준의 에러 값을 갖는다. 왜냐하면, critical point에 포함된 위로 볼록인 방향 축의 비율이 크면 클수록 높은 에러를 가지기 때문이다.(실험적 결과) local minima는 위로 볼록인 경우가 하나도 없는 경우이기 때문에 결과적으로 매우 낮은 에러를 갖게 될 것이다.  

#### References

- [NeuralNetwork (3) Optimazation2 - Cornor's Blog](https://wjddyd66.github.io/dl/NeuralNetwork-(3)-Optimazation2/)
- [Local Minima 문제에 대한 새로운 시각 - 다크 프로그래머](https://darkpgmr.tistory.com/148)
- [05-1.심층 신경망 학습-활성화 함수, 가중치 초기화 - EXCELSIOR](https://excelsior-cjh.tistory.com/177)

---

## #14-1

#### GD(Gradient Descent)가 Local Minima 문제를 피하는 방법은?

Local minima 문제를 피하는 방법으로는 **Momentum, Nesterov Accelerated Gradient(NAG), Adagrad, Adadelta, RMSprop, Adam** 등이 있다.

**Momentum**이란 관성을 의미하며, 이전 gradient의 방향성을 담고있는 `momentum` 인자를 통해 흐르던 방향을 어느 정도 유지시켜 local minima에 빠지지 않게 만든다. 즉, 관성을 이용하여, 학습 속도를 더 빠르게 하고, 변곡점을 잘 넘어갈 수 있도록 해주는 역할을 수행한다.  
<img src="/images/sally/2021-05-01-18-37-27.png" width="50%">  

**Nesterov Accelerated Gradient(NAG)** 는 모멘텀과 비슷한 역할을 수행하는 `Look-ahead gradient `인자를 포함하여, <!-- $a$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=a"> 라는 `accumulate gradient`가 gradient를 감소시키는 역할을 한다.  
<img src="/images/sally/2021-05-01-18-41-38.png" width="45%">

- **Momentum vs. NAG**  
  ![momemtum vs. NAD](/images/sally/2021-05-01-18-44-16.png)  

**Adagrad**란 뉴럴넷의 파라미터가 많이 바뀌었는지 적게 바뀌었는지 확인하고, 적게 변한건 더 크게 변하게 하고, 크게 변한건 더 작게 변화시키는 방법이다. Adagrad는 `sum of gradient squares`(<!-- $G_t$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=G_t">)를 사용하는데, 이는 그래디언트가 얼만큼 변했는지를 제곱해서 더하는 것이므로 계속 커진다는 문제가 발생한다. <!-- $G_t$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=G_t">가 계속 커지면 분모가 점점 무한대에 가까워지게 되어, <!-- $W$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=W"> 업데이트가 되지 않게 되어, 뒤로 갈수록 학습이 점점 안되는 문제점이 발생한다.

<img src="/images/sally/2021-05-01-18-47-55.png" width="60%">  

**Adadelta**는 `Exponential Moving Average(EMA)`를 사용하여, Adagrad의 <!-- $G_t$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=G_t">가 계속 커지는 현상을 막을 수 있다. EMA는 현재 타임스텝으로부터 `윈도우 사이즈만큼의 파라미터 변화(그래디언트 제곱의 변화)를 반영`하는 역할을 하는데, 이전의 값을 모두 저장하는 것이 아닌, `이전 변화량에 특정 비율을 곱해 더한 인자`를 따로 두는 방식이다. Adadelta는 learning rate가 없다.

<img src="/images/sally/2021-05-01-21-41-54.png" width="70%">

> **Momentum**의 더 자세한 내용은 [모멘텀의 수식을 적어 본다면?](#17-3) 참고  
> **SGD, RMSprop, Adam**에 대한 설명은 [SGD, RMSprop, Adam에 대해서 아는대로 설명한다면?](#17) 참고  

#### References

- [딥러닝 기초 Optimization-Gradient Descent Methods - Sally blog](https://bsm8734.github.io/posts/bc-d012-2-dlbasic-optimization-gradient-descent-methods/)
- [NeuralNetwork (3) Optimazation2 - Cornor's Blog](https://wjddyd66.github.io/dl/NeuralNetwork-(3)-Optimazation2/)

---

## #14-2

#### 찾은 해가 Global Minimum인지 아닌지 알 수 있는 방법은?

Gradient Descent 방식에서 lacal minima에 도달함은 증명되어있으나, global minima에 도달하는 것은 보장되지 않았다. 또한, 현재 도달한 지점이 global minima인지 알 수 없다. 딥러닝에서 다루는 문제가 convexity를 만족하지 않기 때문이다. 대신, local minima를 찾는다면, 그 지점이 곧 global minima일 가능성이 크다. [Local Minima 문제에도 불구하고 딥러닝이 잘 되는 이유는?](#14)에서 언급했듯, saddle point가 아닌 완전한 local minimum이 발생하는 경우는 희귀하다. 딥러닝과 같은 고차원 구조에서는 대부분 local minima가 아니라 saddle point일 가능성이 높다. 따라서, 실제 local minima가 존재한다면 그 지점을 global minimum으로 봐도 무방할 것이다.

#### References

- [Local Minima 문제에 대한 새로운 시각 - 다크 프로그래머](https://darkpgmr.tistory.com/148)
- [0021 Gradient Descent & Momentum - Deepest Documentation](https://deepestdocs.readthedocs.io/en/latest/002_deep_learning_part_1/0021/)

---

## #15

#### Training 세트와 Test 세트를 분리하는 이유는?

#### References

---

## #15-1

#### Validation 세트가 따로 있는 이유는?

#### References

---

## #15-2

#### Test 세트가 오염되었다는 말의 뜻은?

#### References

---

## #15-3

#### Regularization이란 무엇인가?

#### References

---

## #16

#### Batch Normalization의 효과는?

#### References

---

## #16-1

#### Dropout의 효과는?

#### References

---

## #16-2

#### BN 적용해서 학습 이후 실제 사용시에 주의할 점은? 코드로는?

#### References

---

## #16-3

#### GAN에서 Generator 쪽에도 BN을 적용해도 될까?

#### References

---

## #17

#### SGD, RMSprop, Adam에 대해서 아는대로 설명한다면?

#### References

---

## #17-1

#### SGD에서 Stochastic의 의미는?

#### References

---

## #17-2

#### 미니배치를 작게 할때의 장단점은?

#### References

---

## #17-3

#### 모멘텀의 수식을 적어 본다면?

#### References

---

## #18

#### 간단한 MNIST 분류기를 MLP+CPU 버전으로 numpy로 만든다면 몇줄일까?

2-layer 신경망을 구현한다고 했을 때, 100줄 이내로 만들 수 있다.

#### References

- [deeplearning_from_scratch - youbeebee](https://github.com/youbeebee/deeplearning_from_scratch/blob/master/ch4.%EC%8B%A0%EA%B2%BD%EB%A7%9D%20%ED%95%99%EC%8A%B5/4.5.%ED%95%99%EC%8A%B5%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0.py)
- [4장.신경망 학습 - 파이썬 머신러닝 완벽가이드(도서)](http://m.yes24.com/goods/detail/69752484)

---

## #18-1

#### 어느 정도 돌아가는 녀석을 작성하기까지 몇시간 정도 걸릴까?

간단한 MNIST 분류기를 MLP+CPU 버전으로 numpy로 만든, 참고 코드([deeplearning_from_scratch - youbeebee](https://github.com/youbeebee/deeplearning_from_scratch/blob/master/ch4.%EC%8B%A0%EA%B2%BD%EB%A7%9D%20%ED%95%99%EC%8A%B5/4.5.%ED%95%99%EC%8A%B5%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0.py))의 경우, 15 에폭 기준 0.9 이상의 정확도가 나온다고 한다. 이 100줄 가량의 코드를 작성하는데 걸리는 시간은 사람마다 다르겠지만, 구조를 정확히 알고있다면 오래걸려도 30분 내에는 작성할 수 있을 것이라 생각한다. 그러나 pretrain되지 않은 모델의 경우, 학습시간이 꽤 오래걸린다고 한다.

#### References

- [3.6.2.신경망의 추론 처리 - 파이썬 머신러닝 완벽가이드(도서)](http://m.yes24.com/goods/detail/69752484)

---

## #18-2

#### Back Propagation은 몇줄인가?

참고 코드(경사하강법 적용) 기준으로 10줄이면 구현할 수 있다. `gradient_descent` 함수를 각 레이어별로 적용하면 미분값을 적용시킬 수 있다.

```python
# 가중치 매개변수의 기울기를 구함
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)  # x와 형상이 같은 배열을 생성

    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h) 계산
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h) 계산
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val  # 값 복원

    return grad

for key in ('W1', 'b1', 'W2', 'b2'):
    network.params[key] -= learning_rate * grad[key]
```

#### References

- [deeplearning_from_scratch - youbeebee](https://github.com/youbeebee/deeplearning_from_scratch/blob/master/ch4.%EC%8B%A0%EA%B2%BD%EB%A7%9D%20%ED%95%99%EC%8A%B5/4.4.%EA%B8%B0%EC%9A%B8%EA%B8%B0.py)
- [4.5.신경망학습_학습 알고리즘 구현하기 - 파이썬 머신러닝 완벽가이드(도서)](http://m.yes24.com/goods/detail/69752484)

---

## #18-3

#### CNN으로 바꾼다면 얼마나 추가될까?

filter의 수, 크기, padding, stride 등에 대한 내용과 pooling layer등 레이어에 관한 정의가 추가되므로 약 50줄 정도 추가된다.  

MLP 버전과 CNN 버전의 참고코드는 아래와 같다.  
- [MLP 참고 코드](https://github.com/youbeebee/deeplearning_from_scratch/blob/master/ch4.%EC%8B%A0%EA%B2%BD%EB%A7%9D%20%ED%95%99%EC%8A%B5/4.5.%ED%95%99%EC%8A%B5%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0.py)
- [CNN 참고 코드](https://github.com/youbeebee/deeplearning_from_scratch/blob/master/ch7.CNN/7.5.CNN%20%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0.py)

#### References

- [deeplearning_from_scratch - youbeebee](https://github.com/youbeebee/deeplearning_from_scratch/blob/master/ch7.CNN/7.5.CNN%20%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0.py)
- [4.5.신경망 학습, 7.5.CNN 구현하기 - 파이썬 머신러닝 완벽가이드(도서)](http://m.yes24.com/goods/detail/69752484)

---

## #19

#### 간단한 MNIST 분류기를 TF, PyTorch 등으로 작성하는데 몇시간이 필요한가?

#### References

---

## #19-1

#### CNN이 아닌 MLP로 해도 잘 될까?

#### References

---

## #19-2

#### 마지막 레이어 부분에 대해서 설명 한다면?

#### References

---

## #19-3

#### 학습은 BCE loss로 하되 상황을 MSE loss로 보고 싶다면?

#### References

---

## #20

#### 딥러닝할 때 GPU를 쓰면 좋은 이유는?

#### References

---

## #20-1

#### 학습 중인데 GPU를 100% 사용하지 않고 있다. 이유는?

#### References

---

## #20-2

#### GPU를 두개 다 쓰고 싶다. 방법은?

#### References

---

## #20-3

#### 학습시 필요한 GPU 메모리는 어떻게 계산하는가?

#### References

---
