## 📝 Table of Contents

- [알고 있는 metric에 대해 설명해주세요. (ex. RMSE, MAE, recall, precision ...)](#1)
- [정규화를 왜 해야할까요? 정규화의 방법은 무엇이 있나요?](#2)
- [Local Minima와 Global Minima에 대해 설명해주세요.](#3)
- [차원의 저주에 대해 설명해주세요.](#4)
- [dimension reduction 기법으로 보통 어떤 것들이 있나요?](#5)
- [PCA는 차원 축소 기법이면서, 데이터 압축 기법이기도 하고, 노이즈 제거기법이기도 합니다. 왜 그런지 설명해주실 수 있나요?](#6)
- [LSA, LDA, SVD 등의 약자들이 어떤 뜻이고 서로 어떤 관계를 가지는지 설명할 수 있나요?](#7)
- [Markov Chain을 고등학생에게 설명하려면 어떤 방식이 제일 좋을까요?](#8)
- [텍스트 더미에서 주제를 추출해야 합니다. 어떤 방식으로 접근해 나가시겠나요?](#9)
- [SVM은 왜 반대로 차원을 확장시키는 방식으로 동작할까요? SVM은 왜 좋을까요?](#10)
- [다른 좋은 머신 러닝 대비, 오래된 기법인 나이브 베이즈(naive bayes)의 장점을 옹호해보세요.](#11)
- [회귀 / 분류시 알맞은 metric은 무엇일까?](#12)
- [Association Rule의 Support, Confidence, Lift에 대해 설명해주세요.](#13)
- [최적화 기법중 Newton’s Method와 Gradient Descent 방법에 대해 알고 있나요?](#14)
- [머신러닝(machine)적 접근방법과 통계(statistics)적 접근방법의 둘간에 차이에 대한 견해가 있나요?](#15)
- [인공신경망(deep learning이전의 전통적인)이 가지는 일반적인 문제점은 무엇일까요?](#16)
- [지금 나오고 있는 deep learning 계열의 혁신의 근간은 무엇이라고 생각하시나요?](#17)
- [ROC 커브에 대해 설명해주실 수 있으신가요?](#18)
- [여러분이 서버를 100대 가지고 있습니다. 이때 인공신경망보다 Random Forest를 써야하는 이유는 뭘까요?](#19)
- [K-means의 대표적 의미론적 단점은 무엇인가요? (계산량 많다는것 말고)](#20)
- [L1, L2 정규화에 대해 설명해주세요.](#21)
- [Cross Validation은 무엇이고 어떻게 해야하나요?](#22)
- [XGBoost을 아시나요? 왜 이 모델이 캐글에서 유명할까요?](#23)
- [앙상블 방법엔 어떤 것들이 있나요?](#24)
- [feature vector란 무엇일까요?](#25)
- [좋은 모델의 정의는 무엇일까요?](#26)
- [50개의 작은 의사결정 나무는 큰 의사결정 나무보다 괜찮을까요? 왜 그렇게 생각하나요?](#27)
- [스팸 필터에 로지스틱 리그레션을 많이 사용하는 이유는 무엇일까요?](#28)
- [OLS(ordinary least squre) regression의 공식은 무엇인가요?](#29)

---

## #1

#### 알고 있는 metric에 대해 설명해주세요. (ex. RMSE, MAE, recall, precision ...)

#### References

---

## #2

#### 정규화를 왜 해야할까요? 정규화의 방법은 무엇이 있나요?

#### References

---

## #3

#### Local Minima와 Global Minima에 대해 설명해주세요.

#### References

---

## #4

#### 차원의 저주에 대해 설명해주세요.

#### References

---

## #5

#### dimension reduction 기법으로 보통 어떤 것들이 있나요?

#### References

---

## #6

#### PCA는 차원 축소 기법이면서, 데이터 압축 기법이기도 하고, 노이즈 제거기법이기도 합니다. 왜 그런지 설명해주실 수 있나요?

#### References

---

## #7

#### LSA, LDA, SVD 등의 약자들이 어떤 뜻이고 서로 어떤 관계를 가지는지 설명할 수 있나요?

#### References

---

## #8

#### Markov Chain을 고등학생에게 설명하려면 어떤 방식이 제일 좋을까요?

#### References

---

## #9

#### 텍스트 더미에서 주제를 추출해야 합니다. 어떤 방식으로 접근해 나가시겠나요?

#### References

---

## #10

#### SVM은 왜 반대로 차원을 확장시키는 방식으로 동작할까요? SVM은 왜 좋을까요?

#### References

---

## #11

#### 다른 좋은 머신 러닝 대비, 오래된 기법인 나이브 베이즈(naive bayes)의 장점을 옹호해보세요.

#### References

---

## #12

#### 회귀 / 분류시 알맞은 metric은 무엇일까?

#### References

---

## #13

#### Association Rule의 Support, Confidence, Lift에 대해 설명해주세요.

#### References

---

## #14

#### 최적화 기법중 Newton’s Method와 Gradient Descent 방법에 대해 알고 있나요?

#### References

---

## #15

#### 머신러닝(machine)적 접근방법과 통계(statistics)적 접근방법의 둘간에 차이에 대한 견해가 있나요?

머신러닝적 접근방법과 통계적 접근방법의 차이는 두 방법의 주 목적이 다르다는 것이다. 

머신러닝적 접근방법은 모델의 **예측 성공률**을 높이는게 목적이다.  
따라서 모델의 신뢰도나 정교한 가정보다는 다양한 피쳐를 사용하여 (오버피팅을 감안하더라도) 높은 예측률을 달성하고자 한다.

통계적 접근방법은 분포와 가정을 통해 **신뢰 가능하고 정교한** 모델을 만드는게 목적이다.  
따라서 모형을 복잡하지 않고 단순하게 만들고, 어떤 피쳐가 어떤 원인을 주는지 알 수 있도록 한다.

#### References
- [머신러닝과 전통적 통계학의 차이 - Hyunseok Choi](https://medium.com/@hyunseok/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D%EA%B3%BC-%EC%A0%84%ED%86%B5%EC%A0%81-%ED%86%B5%EA%B3%84%ED%95%99%EC%9D%98-%EC%B0%A8%EC%9D%B4-a560f0708db0)
- [Machine Learning과 전통적 통계분석 방법의 차이](https://ek-koh.github.io/data%20analysis/ML-diff/)

---

## #16

#### 인공신경망(deep learning이전의 전통적인)이 가지는 일반적인 문제점은 무엇일까요?

딥러닝 이전의 인공신경망은 선형적으로만 회귀, 분류를 수행하기 때문에 레이어를 깊게 쌓지 못했고, 때문에 XOR 문제 같은 복잡한 문제를 풀지 못하는 문제점이 있었다.

![XOR문제](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/XOR.png)

하지만 선형 구조를 결합하여 XOR 문제를 해결하고, 편미분 체인룰을 사용한 오차역전파 방법으로 모델을 업데이트할 수 있게 되면서, 레이어를 깊게 쌓은 딥러닝 인공신경망이 발전하였다.


#### References
- [1.2 딥러닝 이전: 머신 러닝의 간략한 역사 - 텐서 플로우 블로그](https://tensorflow.blog/%EC%BC%80%EB%9D%BC%EC%8A%A4-%EB%94%A5%EB%9F%AC%EB%8B%9D/1-2-%EB%94%A5%EB%9F%AC%EB%8B%9D-%EC%9D%B4%EC%A0%84-%EB%A8%B8%EC%8B%A0-%EB%9F%AC%EB%8B%9D%EC%9D%98-%EA%B0%84%EB%9E%B5%ED%95%9C-%EC%97%AD%EC%82%AC/)
- [모두를 위한 딥러닝 - Sung Kim](https://www.youtube.com/watch?v=n7DNueHGkqE&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm&index=22)


---

## #17

#### 지금 나오고 있는 deep learning 계열의 혁신의 근간은 무엇이라고 생각하시나요?

현재 좋은 성능을 내는 딥러닝 모델들은 모두 큰 규모의 모델들인데 **하드웨어의 발전**이 이를 가능하게 하였다.

또한 **end-to-end 모델**이 나타나면서 데이터 레이블링, 하이퍼파라미터 찾기, 최적 모델 찾기 등 모든 작업을 기계에게 맡기면서 딥러닝이 크게 발전하였다.

추가적으로 여러 **경량화 기법**들이 발전함에 따라 마스크 탐지 카메라 등의 유용한 모델들을 실생활에서 사용할 수 있게 되었다.

#### References
- [end-to-end 학습의 장단점 - 생각많은 소심남](https://talkingaboutme.tistory.com/entry/MLY-end-to-end-%ED%95%99%EC%8A%B5%EC%9D%98-%EC%9E%A5%EB%8B%A8%EC%A0%90)

---

## #18

#### ROC 커브에 대해 설명해주실 수 있으신가요?
ROC 커브는 **이진분류 모델의 성능**을 나타내는 지표이다.

모델이 참이라고 예측하는 경우는 **FPR** (False Positive Rate, 실제 값이 거짓일 때) 과 **TPR** (True Positive Rate, 실제 값이 참일 때) 두 경우로 나뉜다.  
FPR 과 TPR 을 그래프에서 x 축, y 축으로 동시에 표현한 ROC 커브를 통해 모델이 얼마나 옳은 값을 잘 예측하는지 알 수 있게 된다.

![ROC](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/ROC.png) 

ROC 커브가 좌상단과 가까운 경우 좋은 모델이라고 판단할 수 있다. 모델이 FPR 은 낮게, TPR 은 높게 예측하기 때문이다.

#### References
- [ROC curve - 공돌이의 수학 정리 노트](https://angeloyeo.github.io/2020/08/05/ROC.html)

---

## #19

#### 여러분이 서버를 100대 가지고 있습니다. 이때 인공신경망보다 Random Forest를 써야하는 이유는 뭘까요?

**랜덤 포레스트**는 각 서버를 모델의 특성을 이해하는 단일 결정 트리 (Decision tree) 로 **병렬**적이게 구성할 수 있다.  

반면, **인공신경망**은 하나의 서버 자체가 모델의 특성을 모두 이해하는 end-to-end 구조로 **직렬**적이게 구성된다.

따라서 서버가 100대 있을 때는, 이를 병렬적으로 활용할 수 있는 **랜덤 포레스트**를 사용한다.

#### References
- [Random Forest(랜덤 포레스트) 개념 정리 - Codesigner's Dev Story](https://eunsukimme.github.io/ml/2019/11/26/Random-Forest/)
- [의사결정나무 - ratsgo's blog](https://ratsgo.github.io/machine%20learning/2017/03/26/tree/)
- [출근 루틴, 하루 3문제 - Man-About-Town](https://yongwookha.github.io/MachineLearning/2021-01-29-interview-question)

---

## #20

#### K-means의 대표적 의미론적 단점은 무엇인가요? (계산량 많다는것 말고)

K-means 는 특성이 비슷한 데이터를 같은 그룹으로 묶어주는 클러스터링 알고리즘이다.

K-means 알고리즘의 단점은 다음과 같다.  
1. K 를 몇 개로 설정하냐에 따라 성능이 달라진다.
2. K 개 군집의 중심점을 예측하여야 하는데, 어디를 중심점으로 두냐에 따라 성능이 달라진다.
3. 데이터가 잘 모여있는 경우에 효과적이지, 노이즈가 많은 경우 효과적이지 않다. 



#### References
- [머신러닝 - 7. K-평균 클러스터링(K-means Clustering) - 귀퉁이 서재](https://bkshin.tistory.com/entry/%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D-7-K-%ED%8F%89%EA%B7%A0-%EA%B5%B0%EC%A7%91%ED%99%94-K-means-Clustering)

---

## #21

#### L1, L2 정규화에 대해 설명해주세요.

정규화(**일반화**)의 목적은 모델이 학습 데이터에 오버피팅되지 않고 처음 보는 테스트 데이터에도 좋은 성능을 내도록 만드는 것이다. 

L1 정규화 (라쏘 회귀)
![L1 정규화](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/l1_regularization.png)

L2 정규화 (릿지 회귀)
![L2 정규화](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/l2_regularization.png)

loss 식에 람다 * 모델의 웨이트에 대한 L1 or L2 norm 을 더해줌으로써 모델의 일반화가 가능해진다.

loss 는 데이터 값과 추정 값의 차이로 모델은 loss 를 최소화하는 방향으로 학습하는데, L1 or L2 정규화를 사용하면 loss 가 웨이트의 크기만큼 커지기 때문에 데이터 값에 예측 값이 fit 해지지 않기 때문이다.
 
*norm 은 벡터의 크기를 나타내는 것으로 L1 norm 은 벡터의 절댓값 크기를 나타내고, L2 norm 은 직선 거리 (제곱의 루트) 를 나타낸다.
![norm](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/norm.png)  
위 그림에서 초록선은 L2 norm 을 의미하고, 나머지 선은 L1 norm 을 의미한다.
 
L1 loss
![L1 loss](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/l1_loss.png)  

L2 loss
![L2 loss](https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/l2_loss.png)

#### References
- [딥러닝 용어 정리, L1 Regularization, L2 Regularization 의 이해, 용도와 차이 설명 - 빛나는 나무](https://light-tree.tistory.com/125)
- [L1, L2 Norm, Loss, Regularization? - 생각 정리](https://junklee.tistory.com/29)

---

## #22

#### Cross Validation은 무엇이고 어떻게 해야하나요?

#### References

---

## #23

#### XGBoost을 아시나요? 왜 이 모델이 캐글에서 유명할까요?

#### References

---

## #24

#### 앙상블 방법엔 어떤 것들이 있나요?

#### References

---

## #25

#### feature vector란 무엇일까요?

#### References

---

## #26

#### 좋은 모델의 정의는 무엇일까요?

#### References

---

## #27

#### 50개의 작은 의사결정 나무는 큰 의사결정 나무보다 괜찮을까요? 왜 그렇게 생각하나요?

#### References

---

## #28

#### 스팸 필터에 로지스틱 리그레션을 많이 사용하는 이유는 무엇일까요?

#### References

---

## #29

#### OLS(ordinary least squre) regression의 공식은 무엇인가요?

#### References

---
