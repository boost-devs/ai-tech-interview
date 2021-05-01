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

**cost function**  
모델은 데이터에 대해 현재 예측을 얼마나 잘하고 있는지 알아야 학습 방향을 어느 방향으로 얼마나 개선할지 판단할 수 있다.  

이 때, 예측 값과 데이터 값의 차이에 대한 함수를 **cost function**(MSE, CrossEntropy 등) 이라고 한다.  

**cost function** 을 최소화함으로써 모델을 적절한 표현력을 갖추도록 학습시킬 수 있다.


**activation function**  
모델의 한 레이어는 선형 함수와 비선형 함수 **activation function**(Sigmoid, ReLU 등) 이 결합된 비선형 모델로 존재한다.

이러한 비선형 함수들이 왜 활성화 함수라고 불리는걸까?  
활성화 함수를 통해 모델의 웨이트에서 중요한 부분은 높은 값을 띄게 되고 (활성화) 중요하지 않은 부분은 낮은 값을 띄거나 0이 (비활성화) 되기 때문이다.

활성화 과정을 통해 모델은 복잡한 데이터에 대해 더 좋은 예측을 할 수 있게 되고, 여러 레이어를 쌓는 과정도 가능하게 되었다.

#### References
- [5. 결과 값을 비교하는 방식(Cost function) - 대소니](https://daeson.tistory.com/166)
- [Activation Functions에 대해 알아보자 - Steve-Lee's Deep Insight](https://deepinsight.tistory.com/113 )

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

**Sigmoid**

![sigmoid_formula](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/sigmoid_formula.png)

![sigmoid](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/sigmoid.png)

sigmoid 함수는 입력을 0~1 사이의 값으로 바꿔준다.

입력 값이 크거나 작을 때 기울기가 0에 가까워지는 `saturation` 문제가 있다.   
이는 `gradient vanishing` 문제를 야기하므로 요즘에는 활성화 함수로서 잘 사용되지 않는다.

또한 값이 `zero-centered` 가 아니기 때문에 입력값의 부호에 그대로 영향을 받으므로 경사하강법 과정에서 정확한 방향으로 가지 못하고 지그재그로 움직이는 문제가 있다.

**Tanh**

![tanh](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/tanh.png)

tanh 함수는 입력을 -1~1 사이의 값으로 바꿔준다.

sigmoid 함수와 마찬가지로 `saturation` 문제가 있다.


**ReLU** 

![ReLU](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/relu.png)

ReLU 함수는 입력이 양수면 그대로, 음수면 0을 출력한다. 

> f(x) = max(0, x)

계산 효율과 성능에서 뛰어난 성능을 보여 가장 많이 사용되는 활성화 함수이다.

양의 입력에 대해서는 `saturation` 문제가 발생하지 않는다.

음의 입력 값에 대해서는 어떤 업데이트도 되지 않는 `Dead ReLU` 문제가 발생한다.


**LeakyReLU** 

![LeakyReLU](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/leakyrelu.png)

> f(x) = max(0.01x, x)

`ReLU` 와 마찬가지로 좋은 성능을 유지하면서 음수 입력이 0이 아니게 됨에 따라 `Dead ReLU` 문제를 해결하였다.

#### References
- [Activation Functions에 대해 알아보자 - Steve-Lee's Deep Insight](https://deepinsight.tistory.com/113 )
- [[신경망] 6. 활성화 함수 (Activation Function) - 분석벌레의 공부방](https://analysisbugs.tistory.com/55)
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

딥러닝에서 가중치를 잘 초기화하는 것은 기울기 소실이나 local minima 등의 문제를 야기할 수 있기 때문에 중요하다.

**LeCun Initialization**  
딥러닝의 대가 LeCun 교수님이 제시한 초기화 방법으로 정규 분포와 균등 분포를 따르는 방법이 있다.

정규 분포를 따르는 방법  
![lecun_normal](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/lecun_normal.png)


균등 분포를 따르는 방법
![lecun_uniform](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/lecun_uniform.png)

**Xavier Initialization**
LeCun 방법과 비슷하지만 들어오는 노드 수와 나가는 노드 수에 의존하고, 적절한 상수값도 발견하여 사용한 방법이다.

정규 분포를 따르는 방법  
![xavier_normal](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/xavier_normal.png)


균등 분포를 따르는 방법
![xavier_uniform](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/xavier_uniform.png)

sigmoid 나 tanh 함수와는 좋은 결과를 보여주지만 ReLU 함수와 사용할 경우 0에 수렴하는 문제가 발생한다.  
따라서 `sigmoid` 나 `tanh` 함수와 주로 많이 사용한다.

**He Initialization**
`ReLU` 와 함께 많이 사용되는 방법으로, LeCun 방법과 같지만 상수를 다르게 하였다.

정규 분포를 따르는 방법  
![he_normal](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/he_normal.png)


균등 분포를 따르는 방법
![he_uniform](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/he_uniform.png)


#### References
- [가중치 초기화 (Weight Initialization) - reniew's blog](https://reniew.github.io/13/)

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
사람은 처음 보는 물건 (새 레이블) 에 대해 조금만 봐도 다른 것과 이 물건을 구분해낼 수 있다.  
하지만 뉴럴넷은 이 물건을 구분해내기 위해서는 이 물건에 대한 많은 데이터를 학습해야한다.

`One-shot Learning` 은 뉴럴넷도 새로운 레이블을 지닌 데이터가 적을 때 (one-shot 에서는 한 개) 에도 모델이 좋은 성능을 내도록 사용되는 방법이다.

기존에 다른 레이블의 많은 데이터를 학습한 모델은 데이터의 특성을 잘 이해하고 있다.  
이 모델에 새로운 레이블의 데이터 하나를 주면 모델은 이 레이블에 대해서도 이해를 하게 된다.  
따라서 `One-shot Learning` 으로 인해 적은 데이터를 가진 레이블에 대해 좋은 성능을 낼 수 있게 된다.

#### References
- [One-shot learning (siamese network) - sji](https://aimaster.tistory.com/48)
- [One shot learning, Siamese Network 이해 - Deep Play](https://3months.tistory.com/507)

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
모델은 데이터에 대해 예측값을 만들고 정답과 비교하며 업데이트되면서 학습이 된다.  
그런데 학습 데이터에 대해서는 좋은 성능을 낸다 하더라도 본 적 없는 데이터에 대해서는 잘 대응하지 못하는 **오버피팅** 문제가 생긴다면 좋은 모델이 아니다.

이를 막기 위해 학습된 모델이 처음 보는 데이터에도 강건하게 성능을 내는지 판단하기 위한 수단으로 test 세트를 따로 만든다.

#### References
- [test와 validation - ML Basics](https://wikidocs.net/31019)

---

## #15-1

#### Validation 세트가 따로 있는 이유는?
모델을 학습시키고 test 데이터를 통해 모델의 일반화 성능을 파악하고, 다시 모델에 새로운 시도를 하고 test 데이터를 통해 모델의 성능을 파악한다고 생각해보자.

이 경우, 모델은 결국 test 데이터에도 오버피팅이 되어 다시 처음 보는 데이터를 주면 좋은 성능을 보장할 수 없게 된다.  

이 문제를 막기 위해 validation 세트를 사용한다.  
validation 세트를 통해 모델의 성능을 평가하고 하이퍼파라미터 등을 수정하는 것이다.

즉, train 데이터로 모델을 학습시키고 valid 데이터로 학습된 모델의 성능 평가를 하고 더 좋은 방향으로 모델을 수정한다. 그리고 최종적으로 만들어진 모델로 test 데이터를 통해 최종 성능을 평가한다.

#### References
- [test와 validation - ML Basics](https://wikidocs.net/31019)

---

## #15-2

#### Test 세트가 오염되었다는 말의 뜻은?
test 데이터는 한 번도 학습에서 본 적 없는 데이터여야 한다.  
그런데 train 데이터가 test 데이터와 흡사하거나 포함되기까지한다면 test 데이터는 더이상 학습된 모델의 성능 평가를 객관적으로 하지 못한다.

이렇듯 test 데이터가 train 데이터와 유사하거나 포함된 경우에 test 세트가 오염되었다고 말한다.

#### References
- [7. Data Leakage - 분리수거장](https://m.blog.naver.com/hongjg3229/221811766581)

---

## #15-3

#### Regularization이란 무엇인가?
모델의 오버피팅을 막고 처음 보는 데이터에도 잘 예측하도록 만드는 방법을 Regularization(일반화)라고 한다.

대표적인 방법으로 dropout, [L1-L2 Regularization](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/answers/machine-learning.md#21) 등이 있다.



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
TF 나 Pytorch 를 몇 번 사용해본 사람이라면 도큐먼트 참고도 하고 적당히 구글링도 하면, MNIST 분류기의 `데이터 다운로드, 데이터셋, 데이터로더, 모델 세팅, 학습, 추론` 를 구현하는데 2시간이 걸리지 않을 것이라 생각한다.

강력한 성능을 내는 모델도 이러한 프레임워크를 사용하면 빠른 시간 내에 구현해낼 수 있음에 감사하고, 추상화가 잘 된 함수들일지라도 안에서는 어떤 동작을 하는지 알고 사용해야한다.

#### References

---

## #19-1

#### CNN이 아닌 MLP로 해도 잘 될까?
Convolution 레이어는 receptive field 를 통해 이미지의 위치 정보까지 고려할 수 있다는 장점이 있다. 

반면 MLP 는 모두 Fully connected 구조이므로 이미지의 특징을 이해하는데 픽셀마다 위치를 고려할 수 없게된다.

따라서 MNIST 분류기에서 MLP 를 사용하면 CNN 을 사용했을 때보다 성능이 낮다.

#### References

---

## #19-2

#### 마지막 레이어 부분에 대해서 설명 한다면?
MNIST 분류기는 Convolution 레이어를 깊게 쌓으며 숫자 이미지의 작은 특징부터 큰 특징까지 파악한다.

마지막 레이어, `Fully connected 레이어`는 이미지 데이터의 특징을 취합하여 10개의 숫자 중 적절한 숫자로 분류하는 역할을 한다.

만약 더 많은 레이블에 대해 분류해야 한다면 마지막 레이어의 out dimension 을 그에 맞게 설정하면 된다.

#### References

---

## #19-3

#### 학습은 BCE loss로 하되 상황을 MSE loss로 보고 싶다면?
무슨말일까요...

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
