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
