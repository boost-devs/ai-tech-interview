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

#### 누적 분포 함수와 확률 밀도 함수는 무엇일까요? 수식과 함께 표현해주세요.

확률 변수 <!-- $X$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=X">가 임의의 실수 집합 <!-- $B$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=B">에 포함되는 사건의 확률이 다음과 같이 어떤 음이 아닌 함수 <!-- $f$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f">의 적분으로 주어진다고 합시다.

<!-- $$
P(X \in B) = \int_{B} f(x) dx
$$ -->

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=P(X%20%5Cin%20B)%20%3D%20%5Cint_%7BB%7D%20f(x)%20dx%0D"></div>

<br/>

이 때의 <!-- $X$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=X">를 연속확률변수라고 하며, 함수 <!-- $f(x)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=f(x)">를 `확률 밀도 함수(Probability Density Function, PDF)`라고 합니다. 단, 실수 집합 <!-- $B$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=B">가 실수 전체일 경우 실수 전체에 대한 확률밀도함수의 적분은 1을 만족해야 합니다.

<!-- $$
P(X \in R) = \int_{R} f(x) dx = 1
$$ -->

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=P(X%20%5Cin%20R)%20%3D%20%5Cint_%7BR%7D%20f(x)%20dx%20%3D%201%0D"></div>

<br/>

`누적 분포 함수(Cumulative Distribution Function, CDF)`는 확률변수가 특정 값보다 작거나 같을 확률을 나타내는 함수입니다. 특정 값을 <!-- $a$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=a">라고 할 때, 누적 분포 함수는 다음과 같이 나타낼 수 있습니다.

<!-- $$
F(a) = P(X ≤ a) = \int^a_{-\inf} f(x) dx
$$ -->

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=F(a)%20%3D%20P(X%20%E2%89%A4%20a)%20%3D%20%5Cint%5Ea_%7B-%5Cinf%7D%20f(x)%20dx%0D"></div>

<br/>

확률 밀도 함수와 누적 분포 함수는 `미분과 적분의 관계`를 갖고 있습니다. 확률 밀도 함수를 음의 무한대에서 특정값 <!-- $a$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=a">까지 적분을 하면, <!-- $a$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=a">에 대한 누적 분포 함수를 얻을 수 있습니다. 반대로 누적 분포 함수를 미분하면 확률 밀도 함수를 얻을 수 있습니다.


#### References

- [확률및통계 홍영훈 교수님 정말 감사드립니다🙇‍♀️](https://sites.google.com/site/hong0108/)
- [확률 분포 함수와 확률 밀도 함수의 의미 - groovallstar.log](https://velog.io/@groovallstar/%ED%99%95%EB%A5%A0-%EB%B6%84%ED%8F%AC-%ED%95%A8%EC%88%98%EC%99%80-%ED%99%95%EB%A5%A0-%EB%B0%80%EB%8F%84-%ED%95%A8%EC%88%98%EC%9D%98-%EC%9D%98%EB%AF%B8)

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

`p-value`를 알기 위해서는 먼저 1종 오류를 알아야 합니다. 여기서 1종 오류란 "귀무가설이 참인데 기각한 경우"을 말합니다. 귀무가설이란 기존의 주장을 말하며, 이와 반대로 새로운 주장을 대립가설이라고 합니다.

예를 들어, 어느 제약회사에서 치료약 A를 개발하였습니다. 제약회사에서 귀무가설로 "치료약 A가 효과가 없다"라고 설정했다고 합시다. 반대로 대립가설은 "치료약 A는 효과가 있다"로 설정할 수 있습니다. 회사에서는 귀무가설을 기각하고 대립가설을 채택하였습니다. 치료약 A는 판매되었고 높은 매출을 기록합니다. 그런데 알고보니 치료약 A가 효과가 없다는 것이 밝혀졌습니다. 참인 귀무가설을 기각했기에 이는 1종 오류가 일어났다고 볼 수 있습니다.

`p-value`는 1종 오류를 범할 확률을 말합니다. 예를 들어, p-value가 5%라면, 100번 중 5번 1종 오류가 발생한다는 말입니다. 다시 말해, 95%의 신뢰도로 귀무가설을 기각합니다.

#### References

- [p-value의 의미 - 공돌이의 수학정리노트](https://angeloyeo.github.io/2020/03/29/p_value.html)
- [p-value란 무엇인가 - 진화하자 어디에도 소속되지 않기](https://adnoctum.tistory.com/332)
- [통계, 기본 개념을 정리해보자 - 이지훈](https://brunch.co.kr/@jihoonleeh9l6/34)

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

#### 엔트로피(Entropy)에 대해 설명해주세요. 가능하면 정보이득(Information Gain)도요.

> 엔트로피는 entropy로, 정보이득은 information gain으로 모두 영어로 표기합니다.

`entropy`는 주어진 데이터의 혼잡도를 의미하며, entropy는 다음과 같이 데이터가 어떤 클래스에 속할 확률에 대한 기댓값으로 표현할 수 있습니다.

<!-- $$
E = - \sum^k_{i=1} p_i \log_2 (p_i)
$$ -->

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math=E%20%3D%20-%20%5Csum%5Ek_%7Bi%3D1%7D%20p_i%20%5Clog_2%20(p_i)%0D"></div>

entropy는 데이터가 서로 다른 클래스에 속하면 높고, 같은 클래스에 속하면 낮습니다. 다시 말하면 특정 클래스에 속할 확률이 높고 나머지 클래스에 속할 확률이 낮다면 entropy가 낮고, 모든 각각의 클래스에 속할 확률이 비슷하다면 entropy는 낮습니다.

`information gain`은 어떤 속성을 선택함으로 인해 데이터가 잘 필터링되는지를 말하며, 1에서 엔트로피를 뺀 값으로 표현됩니다. 이 값은 의사결정트리가 분할을 할 때의 기준으로 사용되며, 높은 information gain을 기준으로 분할합니다.

#### References

- [10.1 엔트로피 - 데이터 사이언스 스쿨](https://datascienceschool.net/02%20mathematics/10.01%20%EC%97%94%ED%8A%B8%EB%A1%9C%ED%94%BC.html)
- [[인공지능] 엔트로피(Entropy) 와 정보이득(Information Gain) 계산 - 꾸준희](https://eehoeskrap.tistory.com/13)
- [파이썬 머신러닝 완벽 가이드 - 권철민](http://www.yes24.com/Product/Goods/87044746?OzSrank=2)

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

> 모수는 모집단의 수가 아닌, 평균, 표준편차 등의 모집단의 특징을 말합니다. 여기서는 모집단의 수로 잘못 쓰인 것으로 보이며, 데이터가 적은 경우라 가정하고 답변을 작성하였습니다.

표본이 매우 작은 경우 표본평균의 분포가 정규분포를 따른다고 가정할 수 없으므로 비모수적 방법을 채택하여 예측 모델을 수립할 수 있습니다. 하지만 중심극한정리에 의해 표본의 크기가 30보다 클 경우 표본평균이 정규분포를 따른다고 가정할 수 있으므로, 이 경우에는 무수적 방법을 사용합니다.

#### References

- [모수, 큰 수의 법칙, 그리고 중심극한정리 - Kyoyoung Chu](https://chukycheese.github.io/data%20science/parameter-clt/)
- [퍼널에서 모수 용어 질문요? - 인프런, cco](https://www.inflearn.com/questions/34568)
- [[통계이론] 모수적 방법 vs 비모수적 방법](https://zzanhtt.tistory.com/18)

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

`이상치(outlier)`는 전체 데이터의 패턴에서 벗어난 이상한 값을 가진 데이터를 말합니다. 이상치는 모델의 성능에 영향을 미치므로 이를 탐지하는 것은 정말 중요합니다.

이상치를 탐지하는 방법 중 하나로 IQR(Inter Quantile Range) 기법이 있습니다. IQR 기법을 사용하기 위해서는 우선 데이터를 오름차순으로 정렬하고 25%, 50%, 75%, 100%로 4등분을 합니다. 이 75% 지점과 25% 지점의 값의 차이를 IQR이라고 합니다. 이 IQR에 1.5를 곱한 값을 75% 지점의 값에 더하여 최대값을, 25% 지점의 값에서 빼서 최소값을 계산합니다. 이 때 최소값보다 작거나 최대값보다 큰 값을 이상치라고 판단합니다.

또 다른 탐지 방법으로는 Z-score를 계산하는 방식이 있습니다. Z-score는 데이터가 평균에서 얼마나 떨어져 있는지를 나타내는 지표로, 임계값을 설정하여 Z-score이 이 값보다 크다면 이상치로 판단합니다. 하지만 Z-score 방식은 데이터가 가우시안 분포를 따른다고 가정하기 때문에 데이터가 가우시안 분포가 아닐 경우 별도의 변환이 필요합니다.

#### References

- [A Brief Overview of Outlier Detection Techniques - Towards Data Science](https://towardsdatascience.com/a-brief-overview-of-outlier-detection-techniques-1e0b2c19e561)
- [IQR 방식을 이용한 이상치 데이터(Outlier) 제거 - Hwi's ML doc](https://hwi-doc.tistory.com/entry/IQR-%EB%B0%A9%EC%8B%9D%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%9D%B4%EC%83%81%EC%B9%98-%EB%8D%B0%EC%9D%B4%ED%84%B0Outlier-%EC%A0%9C%EA%B1%B0)
- [[데이터전처리] Outlier(이상치/이상값/특이값/특이치 등) 탐지 방법(detection method) : 2. Z-score 방식 with - Clary K](https://claryk.tistory.com/5)

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
