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

#### References

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

#### References

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

#### References

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

#### References

---

## #11

#### 뉴럴넷의 가장 큰 단점은 무엇인가? 이를 위해 나온 One-Shot Learning은 무엇인가?

#### References

---

## #12

#### 요즘 Sigmoid 보다 ReLU를 많이 쓰는데 그 이유는?

<div align='center'>
<img src='../images/penguin/activation-function.png' height='240px'/>
</div>

<br/>

우선 Sigmoid와 ReLU 함수의 모양을 보자. Sigmoid는 값이 큰 양수일수록 1에, 큰 음수일수록 0에 가까워진다. 반면 ReLU는 값이 양수이면 원래 값을 그대로 가져가고, 음수이면 0이다.

요즘 Sigmoid보다 ReLU를 많이 쓰는 가장 큰 이유는 **기울기 소실 문제(Gradient Vanishing)** 때문이다. 기울기는 연쇄 법칙(Chain Rule)에 의해 국소적 미분값을 누적 곱을 시키는데, Sigmoid의 경우 기울기가 항상 0과 1사이의 값이므로 이 값을 연쇄적으로 곱하게 되면 0에 수렴할 수 밖에 없다. 반면 ReLU는 값이 양수일 때, 기울기가 1이므로 연쇄 곱이 1보다 작아지는 것을 어느 정도 막아줄 수 있다.

다만, ReLU는 값이 음수이면, 기울기가 0이기 때문에 일부 뉴런이 죽을 수 있다는 단점이 존재한다. 이를 보완한 활성화 함수로 Leakly ReLU가 있다.

#### References

- [ML — Sigmoid 대신 ReLU? 상황에 맞는 활성화 함수 사용하기 - Minkyeong Kim](https://medium.com/@kmkgabia/ml-sigmoid-%EB%8C%80%EC%8B%A0-relu-%EC%83%81%ED%99%A9%EC%97%90-%EB%A7%9E%EB%8A%94-%ED%99%9C%EC%84%B1%ED%99%94-%ED%95%A8%EC%88%98-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0-c65f620ad6fd)
- [[히스] Gradient Vanishing 해결을 위한 ReLU 와 ResNet - boostcamp-ai-tech-4/peer-session](https://github.com/boostcamp-ai-tech-4/peer-session/issues/52)
- [딥러닝에서 사용하는 활성화함수 - reniew's blog](https://reniew.github.io/12/)

---

## #12-1

#### Non-Linearity라는 말의 의미와 그 필요성은?

비선형(non-linearity)의 뜻을 알기 위해서는 우선 선형(linearity)가 무엇인지 알아야 한다. 어떤 모델이 선형적(linearity)라고 한다면 그 모델은 변수 <!-- $x_1, x_2, ... , x_n$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x_1%2C%20x_2%2C%20...%20%2C%20x_n">과 가중치 <!-- $w_1, w_2, ... , w_n$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=w_1%2C%20w_2%2C%20...%20%2C%20w_n">으로 <!-- $y = w_1*x_1 + w_2*x_2 + ... + w_n*x_n$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=y%20%3D%20w_1*x_1%20%2B%20w_2*x_2%20%2B%20...%20%2B%20w_n*x_n">으로 표현할 수 있다. 그 외에 이렇게 표현할 수 없는 모든 모델을 비선형 관계에 있는 모델이라고 한다.

딥러닝에서 이런 비선형 관계는 활성화 함수(activation function)을 도입함으로써 표현할 수 있다. 그럼 비선형 관계 즉, 활성화 함수가 왜 필요할까? 바로 활성화 함수를 사용해 여러 층을 쌓아서 더 복잡한 표현을 하기 위해서이다. 활성화 함수가 <!-- $h(x) = cx$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=h(x)%20%3D%20cx">인 선형 함수 라고 생각해보자. 이 때 <!-- $n$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=n">개의 층을 쌓았다고 할 때, 모델은 <!-- $y = h^n(x) = c^nx$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=y%20%3D%20h%5En(x)%20%3D%20c%5Enx">로 나타낼 수 있다. <!-- $c^n=k$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=c%5En%3Dk">라는 상수로 치환하면 결국 1층을 가진 신경망과 동일하다. 그렇기 때문에 비선형인 활성화 함수가 필요한 것이다.

#### References

- [[밑바닥 딥러닝] 신경망 - 코딩하는펭귄의 저장소](https://cooding-penguin.netlify.app/dl-from-scratch/neural-network/#%EB%B9%84%EC%84%A0%ED%98%95-%ED%95%A8%EC%88%98)

---

## #12-2

#### ReLU로 어떻게 곡선 함수를 근사하나?

#### References

- [활성화 함수(Activation function) 설명 (Sigmoid, ReLU, LeakyReLU, tanh) - 별보는두더지](https://mole-starseeker.tistory.com/m/39)
- [Q2) Sigmoid 보다 ReLu를 많이 쓰는 이유? - JINSOL KIM](https://gaussian37.github.io/math-question-q2/)

---

## #12-3

#### ReLU의 문제점은?

#### References

- [Neural Network - Machine Learning Blog](https://nmhkahn.github.io/NN)
- [What are the disadvantages of using the ReLu when using Neural Networks? - Quora](https://www.quora.com/What-are-the-disadvantages-of-using-the-ReLu-when-using-Neural-Networks)

---

## #12-4

#### Bias는 왜 있는걸까?

#### References

- [Glossary of Deep Learning: Bias - Jaron Collis](https://medium.com/deeper-learning/glossary-of-deep-learning-bias-cf49d9c895e2)
- [What is the role of the bias in neural networks? - stackoverflow](https://stackoverflow.com/questions/2480650/what-is-the-role-of-the-bias-in-neural-networks)

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

#### References

---

## #14-1

#### GD가 Local Minima 문제를 피하는 방법은?

#### References

---

## #14-2

#### 찾은 해가 Global Minimum인지 아닌지 알 수 있는 방법은?

#### References

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

- [Batch Normalization - Steve-Lee's Deep Insight](https://deepinsight.tistory.com/116)

---

## #16-1

#### Dropout의 효과는?

#### References

- [3.13. 드롭아웃(dropout) - Dive into Deep Learningfg](https://ko.d2l.ai/chapter_deep-learning-basics/dropout.html)

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

#### References

---

## #18-1

#### 어느 정도 돌아가는 녀석을 작성하기까지 몇시간 정도 걸릴까?

#### References

---

## #18-2

#### Back Propagation은 몇줄인가?

#### References

---

## #18-3

#### CNN으로 바꾼다면 얼마나 추가될까?

#### References

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
