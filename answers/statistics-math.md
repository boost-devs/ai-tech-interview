## 📝 Table of Contents

- [고유값(eigen value)와 고유벡터(eigen vector)에 대해 설명해주세요. 그리고 왜 중요할까요?](#1)
- [샘플링(Sampling)과 리샘플링(Resampling)에 대해 설명해주세요. 리샘플링은 무슨 장점이 있을까요?](#2)
- [확률 모형과 확률 변수는 무엇일까요?](#3)
- [누적 분포 함수와 확률 밀도 함수는 무엇일까요? 수식과 함께 표현해주세요](#4)
- [조건부 확률은 무엇일까요?](#5)
- [공분산과 상관계수는 무엇일까요? 수식과 함께 표현해주세요](#6)
- [신뢰 구간의 정의는 무엇인가요?](#7)
- [p-value를 모르는 사람에게 설명한다면 어떻게 설명하실 건가요?](#8)
- [R square의 의미는 무엇인가요?](#9)
- [평균(mean)과 중앙값(median)중에 어떤 케이스에서 뭐를 써야할까요?](#10)
- [중심극한정리는 왜 유용한걸까요?](#11)
- [엔트로피(entropy)에 대해 설명해주세요. 가능하면 Information Gain도요.](#12)
- [어떨 때 모수적 방법론을 쓸 수 있고, 어떨 때 비모수적 방법론을 쓸 수 있나요?](#13)
- [“likelihood”와 “probability”의 차이는 무엇일까요?](#14)
- [통계에서 사용되는 bootstrap의 의미는 무엇인가요.](#15)
- [모수가 매우 적은 (수십개 이하) 케이스의 경우 어떤 방식으로 예측 모델을 수립할 수 있을까요?](#16)
- [베이지안과 프리퀀티스트 간의 입장차이를 설명해주실 수 있나요?](#17)
- [검정력(statistical power)은 무엇일까요?](#18)
- [missing value가 있을 경우 채워야 할까요? 그 이유는 무엇인가요?](#19)
- [아웃라이어의 판단하는 기준은 무엇인가요?](#20)
- [필요한 표본의 크기를 어떻게 계산합니까?](#21)
- [Bias를 통제하는 방법은 무엇입니까?](#22)
- [로그 함수는 어떤 경우 유용합니까? 사례를 들어 설명해주세요.](#23)
- [베르누이 분포 / 이항 분포 / 카테고리 분포 / 다항 분포 / 가우시안 정규 분포 / t 분포 / 카이제곱 분포 / F 분포 / 베타 분포 / 감마 분포에 대해 설명해주세요. 그리고 분포 간의 연관성도 설명해주세요.](#24)

---

## #1

#### 고유값(eigen value)와 고유벡터(eigen vector)에 대해 설명해주세요. 그리고 왜 중요할까요?

#### References

---

## #2

#### 샘플링(Sampling)과 리샘플링(Resampling)에 대해 설명해주세요. 리샘플링은 무슨 장점이 있을까요?

샘플링이란 **표본추출**을 의미하는 것으로, 모집단 전체에 대한 추정치(estimate)를 얻기 위해 임의의 sample을 뽑아내는 것이다.
모집단 전체에 대한 조사는 불가능하기 때문에 sample을 이용하여 모집단에 대한 추론(inference)을 하게되는 것이다.
하지만 표본은 모집단을 닮은 모집단의 mirror image 같은 존재이지만, 모집단 그 자체일수는 없다.
따라서 표본에는 반드시 모집단의 원래 패턴에서 놓친 부분, 즉 **noise가 존재할 수 밖에 없다.**

리샘플링은 **모집단의 분포 형태를 알 수 없을 때 주로 사용하는 방법**이다.
즉, 모분포를 알 수 없으므로 일반적인 통계적 공식들을 사용하기 힘들 때, 현재 갖고 있는 데이터를 이용하여 모분포와 비슷할 것으로 추정되는 분포를 만들어 보자는 것이다.
리샘플링은 **가지고 있는 샘플에서 다시 샘플 부분집합을 뽑아서 통계량의 변동성(variability of statistics)을 확인하는 것**이라고 할 수 있다.
즉, 같은 샘플을 여러 번 사용해서 성능을 측정하는 방식이다. 가장 많이 사용되는 방법이며 종류로는 K-fold 교차 검증, 부트스트래핑이 있다.

리샘플링은 표본을 추출하면서 원래 데이터 셋을 복원하기 때문에 이를 통해서 모집단의 분포에 어떤 가정도 필요 없이 표본만으로 추론이 가능하다는 장점이 있다.

#### References
- [(데이터과학 인터뷰 질문)(2) 샘플링과 리샘플링, 1편](https://cnp-0717.tistory.com/7?category=838077)
- [샘플링과 리샘플링의 차이는 무엇일까?](https://kejdev.github.io/posts/sampling-resampling/)
- [resampling을 이용한 방법 (bootstrapping)](https://adnoctum.tistory.com/296)
- [샘플링과 리샘플링](https://trampled-worm.tistory.com/91)

---

## #3

#### 확률 모형과 확률 변수는 무엇일까요?

#### References

---

## #4

#### 누적 분포 함수와 확률 밀도 함수는 무엇일까요? 수식과 함께 표현해주세요


#### References

---

## #5

#### 조건부 확률은 무엇일까요?

#### References

---

## #6

#### 공분산과 상관계수는 무엇일까요? 수식과 함께 표현해주세요

공분산은 확률변수 X의 편차(평균으로부터 얼마나 떨어져 있는지)와 확률변수 Y의 편차를 곱한 것의 평균값이다.

<img src="https://t1.daumcdn.net/cfile/tistory/99E2B9415C3444B807" width=300>

공분산은 두 변수 간에 양의 상관관계가 있는지, 음의 상관관계가 있는지 정도를 알려준다. 하지만 상관관계가 얼마나 큰지는 제대로 반영하지 못한다.

공분산의 문제는 확률변수의 단위 크기에 영향을 많이 받는다는 것이다. 이를 보완할 수 있는 것이 바로 상관계수이다.

상관계수는 확률변수의 절대적 크기에 영향을 받지 않도록 공분산을 단위화시킨 것이다. 즉, 공분산에 각 확률변수의 분산을 나눠주었다.

<img src="https://t1.daumcdn.net/cfile/tistory/99F3564B5C3449F90F" width=400>

상관계수는 양의 상관관계가 있는지 음의 상관관계가 있는지 알려줄 뿐만 아니라, 그 상관성이 얼마나 큰지도 알려준다. 1 또는 -1에 가까울수록 상관성이 큰 것이고, 0에 가까울수록 상관성이 작은 것이다.

#### References

- [공분산과 상관계수의 이해.txt](https://bskyvision.com/398)
- [공분산(Covariance)과 상관계수(Correlation)](https://destrudo.tistory.com/15)

---

## #7

#### 신뢰 구간의 정의는 무엇인가요?

#### References

---

## #8

#### p-value를 모르는 사람에게 설명한다면 어떻게 설명하실 건가요?

#### References

---

## #9

#### R square의 의미는 무엇인가요?

#### References

---

## #10

#### 평균(mean)과 중앙값(median)중에 어떤 케이스에서 뭐를 써야할까요?

- 평균(mean): 모든 관측값의 합을 자료의 개수로 나눈 것
- 중앙값(median): 전체 관측값을 크기 순서로 배열했을 때 가운데 위치하는 값

평균은 전체 관측값이 골고루 반영되므로 대표값으로서 가치가 있다. 평균 근처에 표본이 몰려 있는 상황에서 대표값으로 유용하지만 극단적인 값에 영향을 많이 받는다.

중앙값에서는 관측값을 크기 순서로 배열할 때 관측값의 위치가 중요하고, 가운데 위치한 관측값 이외의 관측값들의 크기는 중요하지 않다. 따라서 평균과는 달리 중앙값은 관측값들의 변화에 민감하지 않고 특히 아주 큰 관측값이나 아주 작은 관측값(즉, outlier)에 영향을 받지 않는다. 중앙값이 유용한 경우는 표본의 편차, 혹은 왜곡이 심하게 나타나는 경우이다.

#### References

- [평균(average, mean) vs. 중간값(median) | 통계상의 오류가능성](https://leedakyeong.tistory.com/entry/%ED%8F%89%EA%B7%A0-%EC%A4%91%EC%95%99%EA%B0%92-%EC%B5%9C%EB%B9%88%EA%B0%92-%EB%B9%84%EA%B5%90-Mean-VS-Median-VS-Mode)
- [[기초통계] 평균 중앙값 최빈값 비교 (Mean VS Median VS Mode)](https://blog.naver.com/ricemankr/220796823014)

---

## #11

#### 중심극한정리는 왜 유용한걸까요?

#### References

---

## #12

#### 엔트로피(entropy)에 대해 설명해주세요. 가능하면 Information Gain도요.

#### References

---

## #13

#### 어떨 때 모수적 방법론을 쓸 수 있고, 어떨 때 비모수적 방법론을 쓸 수 있나요?

#### References

---

## #14

#### “likelihood”와 “probability”의 차이는 무엇일까요?

- 확률(Probability): 어떤 시행(trial, experiment)에서 특정 결과(sample)가 나올 가능성. 즉, **시행 전 모든 경우의 수의 가능성은 정해져 있으며 그 총합은 1(100%)이다.**
- 가능도(Likelihood): 어떤 시행(trial, experiment)을 충분히 수행한 뒤 그 결과(sample)를 토대로 경우의 수의 가능성을 도출하는 것. 아무리 충분히 수행해도 어디까지나 추론(inference)이기 때문에 **가능성의 합이 1이 되지 않을수도 있다.**

#### References

- [가능도(Likelihood)와 확률(Probability)의 차이](https://swjman.tistory.com/104)

---

## #15

#### 통계에서 사용되는 bootstrap의 의미는 무엇인가요.

#### References

---

## #16

#### 모수가 매우 적은 (수십개 이하) 케이스의 경우 어떤 방식으로 예측 모델을 수립할 수 있을까요?

#### References

---

## #17

#### 베이지안과 프리퀀티스트 간의 입장차이를 설명해주실 수 있나요?

#### References

---

## #18

#### 검정력(statistical power)은 무엇일까요?

||귀무가설 H0 참|귀무가설 H0 거짓|
|:---:|:---:|:---:|
|귀무가설 H0 채택|옳은 결정(1-α)|제 2종 오류(β)|
|귀무가설 H0 기각|제 1종 오류(α)|옳은 결정(1-β)|

검정력은 대립가설 H1이 참인 경우 귀무가설 H0를 기각(대립가설 H1을 채택)할 확률이다.

#### References

- [검정력(power)의 의미 및 수식](https://m.blog.naver.com/PostView.nhn?blogId=hancury&logNo=220854934914&proxyReferer=https:%2F%2Fwww.google.com%2F)
- [통계적 검정: 검정력(power)과 Type 1, 2 Error(1, 2 종 오류)](https://niceguy1575.tistory.com/entry/%ED%86%B5%EA%B3%84%EC%A0%81-%EA%B2%80%EC%A0%95-%EA%B2%80%EC%A0%95%EB%A0%A5power%EA%B3%BC-Type-1-2-Error1-2-%EC%A2%85-%EC%98%A4%EB%A5%98)

---

## #19

#### missing value가 있을 경우 채워야 할까요? 그 이유는 무엇인가요?

#### References

---

## #20

#### 아웃라이어의 판단하는 기준은 무엇인가요?

#### References

---

## #21

#### 필요한 표본의 크기를 어떻게 계산합니까?

#### References

---

## #22

#### Bias를 통제하는 방법은 무엇입니까?

Bias는 데이터 내에 있는 모든 정보를 고려하지 않음으로 인해, 지속적으로 잘못된 것들을 학습하는 경향을 의미한다. 이는 underfitting과 관계되어 있다.

반대로 Variance는 데이터 내에 있는 에러나 노이즈까지 잘 잡아내는 highly flexible models에 데이터를 fitting 시킴으로써, 실제 현상과 관계 없는 random한 것들까지 학습하는 알고리즘의 경향을 의미한다. 이는 overfitting과 관계되어 있다.

편향(Bias)과 분산(Variance)은 한 쪽이 증가하면 다른 한 쪽이 감소하고, 한쪽이 감소하면 다른 한쪽이 증가하는 tradeoff 관계를 가진다.

<img src="https://lh5.googleusercontent.com/lAbzDl1HYiYHAEuGnaUw2GdCyQzkZvjWisgNY-ZRYqvRG-X-U7f7cL_UunIF7v5q0BbUSw4CZ-1-xMXs8mvE8fbGa7ghFeEGzuwJ6wiIs64nUgJxkDNEC2JrSTUHEjViRZLdA23NLqI" width=400>

Bias를 통제하기 위한 방법으로는
- (neuron이나 계층의 갯수 같은) 모델의 크기 증가
- 오류평가시 얻은 지식을 기반으로 입력 특성 수정
- 정규화를 줄이거나 제거
- 모델 구조를 수정
- 학습 데이터 추가

등의 방법이 있다.

#### References

- [쉽게 이해해보는 bias-variance tradeoff](https://bywords.tistory.com/entry/%EB%B2%88%EC%97%AD-%EC%9C%A0%EC%B9%98%EC%9B%90%EC%83%9D%EB%8F%84-%EC%9D%B4%ED%95%B4%ED%95%A0-%EC%88%98-%EC%9E%88%EB%8A%94-biasvariance-tradeoff)
- [Bias and Variance (편향과 분산)](https://opentutorials.org/module/3653/22071)
- [[MLY] avoidable bias를 줄이는 방법들](https://talkingaboutme.tistory.com/entry/MLY-avoidable-bias%EB%A5%BC-%EC%A4%84%EC%9D%B4%EB%8A%94-%EB%B0%A9%EB%B2%95%EB%93%A4?category=538748)

---

## #23

#### 로그 함수는 어떤 경우 유용합니까? 사례를 들어 설명해주세요.

#### References

---

## #24

#### 베르누이 분포 / 이항 분포 / 카테고리 분포 / 다항 분포 / 가우시안 정규 분포 / t 분포 / 카이제곱 분포 / F 분포 / 베타 분포 / 감마 분포에 대해 설명해주세요. 그리고 분포 간의 연관성도 설명해주세요.

#### References

---
