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
- [베르누이 분포 / 이항 분포 / 카테고리 분포 / 다항 분포 / 가우시안 정규 분포 / t 분포 / 카이제곱 분포 / F 분포 / 베타 분포 / 감마 분포에 대해 설명해주세요. 그리고 분표 간의 연관성도 설명해주세요.](#24)

---

## #1

#### 고유값(eigen value)와 고유벡터(eigen vector)에 대해 설명해주세요. 그리고 왜 중요할까요?

#### References

---

## #2

#### 샘플링(Sampling)과 리샘플링(Resampling)에 대해 설명해주세요. 리샘플링은 무슨 장점이 있을까요?

#### References

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

#### References

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

#### References

---

## #11

#### 중심극한정리는 왜 유용한걸까요?

#### References

---

## #12

#### 엔트로피(entropy)에 대해 설명해주세요. 가능하면 Information Gain도요.

xx

#### References

---

## #13

#### 어떨 때 모수적 방법론을 쓸 수 있고, 어떨 때 비모수적 방법론을 쓸 수 있나요?

#### References

---

## #14

#### “likelihood”와 “probability”의 차이는 무엇일까요?

#### References

---

## #15

#### 통계에서 사용되는 bootstrap의 의미는 무엇인가요.

#### References

---

## #16

#### 모수가 매우 적은 (수십개 이하) 케이스의 경우 어떤 방식으로 예측 모델을 수립할 수 있을까요?

xx

#### References

---

## #17

#### 베이지안과 프리퀀티스트 간의 입장차이를 설명해주실 수 있나요?

#### References

---

## #18

#### 검정력(statistical power)은 무엇일까요?

#### References

---

## #19

#### missing value가 있을 경우 채워야 할까요? 그 이유는 무엇인가요?

#### References

---

## #20

#### 아웃라이어의 판단하는 기준은 무엇인가요?

xx

#### References

---

## #21

#### 필요한 표본의 크기를 어떻게 계산합니까?

#### References

---

## #22

#### Bias를 통제하는 방법은 무엇입니까?

#### References

---

## #23

#### 로그 함수는 어떤 경우 유용합니까? 사례를 들어 설명해주세요.

#### References

---

## #24

#### 베르누이 분포 / 이항 분포 / 카테고리 분포 / 다항 분포 / 가우시안 정규 분포 / t 분포 / 카이제곱 분포 / F 분포 / 베타 분포 / 감마 분포에 대해 설명해주세요. 그리고 분표 간의 연관성도 설명해주세요.

#### References

---
