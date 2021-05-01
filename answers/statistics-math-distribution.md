## 📝 Table of Contents

- [베르누이 분포](#1)
- [이항 분포](#2)
- [카테고리 분포](#3)
- [다항 분포](#4)
- [가우시안 정규 분포](#5)
- [t 분포](#6)
- [카이제곱 분포](#7)
- [F 분포](#8)
- [베타 분포](#9)
- [감마 분포](#10)

---

## #1

#### 베르누이 분포

#### References

---

## #2

#### 이항 분포

#### References

---

## #3

#### 카테고리 분포

#### References

---

## #4

#### 다항 분포

#### References

---

## #5

#### 가우시안 정규 분포

#### References

---

## #6

#### t 분포

t 분포는 정규분포와 같이 중심을 기준으로 좌우 대칭이고 종모양 형태를 갖고 중심은 0으로 고정되어 있는 분포이다.

자유도(degree of freedom, df)에 따라 종의 형태가 조금씩 변화한다.

df는 표본수와 관련이 있는 개념으로, 표본이 많아지면 표준정규분포와 거의 동일한 형태를 보인다.

<!-- $Y \sim t(n)$ --> <img style="transform: translateY(0.1em); background: white;" src="../images/adc/deep-learning/fLtEVp8ASo.svg">이면,
<br>
<!-- $f(y) = \frac{\Gamma\left(\frac{n+1}{2}\right)}{\Gamma\left(\frac{n}{2}\right)\cdot\sqrt{\pi n}}\cdot\left(\frac{n}{y^2+n}\right)^{\frac{n+1}{2}},\;\;\;-\infty < y < \infty$ --> <img style="transform: translateY(0.1em); background: white;" src="../images/adc/deep-learning/etNwUJGoHh.svg">
<br>
<!-- $E[Y] = 0\;\;\;Var[Y] = \frac{n}{n-2}$ --> <img style="transform: translateY(0.1em); background: white;" src="../images/adc/deep-learning/TZLEIjrSEx.svg">

> 감마 함수

<!-- $\Gamma(x) = \int_{0}^{\infty}u^{x-1}e^{-u}du$ --> <img style="transform: translateY(0.1em); background: white;" src="../images/adc/deep-learning/dFlfgEP1px.svg">

#### References

- [8.5 스튜던트 t분포, 카이제곱분포, F분포 - 데이터 사이언스 스쿨](https://datascienceschool.net/02%20mathematics/08.05%20%EC%8A%A4%ED%8A%9C%EB%8D%98%ED%8A%B8%20t%EB%B6%84%ED%8F%AC,%20%EC%B9%B4%EC%9D%B4%EC%A0%9C%EA%B3%B1%EB%B6%84%ED%8F%AC,%20F%EB%B6%84%ED%8F%AC.html)
- [2.4 t-분포(t-distribution, Student's t-distribution) - Must Learning with R](https://wikidocs.net/34009)

---

## #7

#### 카이제곱 분포

정규 분포의 제곱합은 <!-- $\chi^2$ --> <img style="transform: translateY(0.1em); background: white;" src="../images/adc/deep-learning/HDjWnZkXVW.svg"> 분포를 따른다.
<br>
<!-- $Z \sim N(0, 1)\;\;\;\Rightarrow\;\;\;Z^2 \sim \chi^2(df=1)\;\;\;\Rightarrow\;\;\;\sum_{i=1}^{n}Z^2_i \sim \chi^2(df=n)$ --> <img style="transform: translateY(0.1em); background: white;" src="../images/adc/deep-learning/4FR6NRzuCY.svg">

#### References

- [8.5 스튜던트 t분포, 카이제곱분포, F분포 - 데이터 사이언스 스쿨](https://datascienceschool.net/02%20mathematics/08.05%20%EC%8A%A4%ED%8A%9C%EB%8D%98%ED%8A%B8%20t%EB%B6%84%ED%8F%AC,%20%EC%B9%B4%EC%9D%B4%EC%A0%9C%EA%B3%B1%EB%B6%84%ED%8F%AC,%20F%EB%B6%84%ED%8F%AC.html)
- [2.5 카이제곱 분포와 F분포 - Must Learning with R](https://wikidocs.net/34010)

---

## #8

#### F 분포

F 분포는 독립적인 <!-- $\chi^2$ --> <img style="transform: translateY(0.1em); background: white;" src="../images/adc/deep-learning/WGpBUWxpfr.svg"> 변수의 비가 따르는 분포이다.
<br>
<!-- $Q_1 \sim \chi^2(n_1),\;\;\;Q_2 \sim \chi^2(n_2)\;\;\;\Rightarrow\;\;\;\frac{Q_1/n_1}{Q_2/n_2} \sim F(n_1, n_2)$ --> <img style="transform: translateY(0.1em); background: white;" src="../images/adc/deep-learning/1ushumHHBo.svg">

#### References

- [8.5 스튜던트 t분포, 카이제곱분포, F분포 - 데이터 사이언스 스쿨](https://datascienceschool.net/02%20mathematics/08.05%20%EC%8A%A4%ED%8A%9C%EB%8D%98%ED%8A%B8%20t%EB%B6%84%ED%8F%AC,%20%EC%B9%B4%EC%9D%B4%EC%A0%9C%EA%B3%B1%EB%B6%84%ED%8F%AC,%20F%EB%B6%84%ED%8F%AC.html)
- [2.5 카이제곱 분포와 F분포 - Must Learning with R](https://wikidocs.net/34010)

---

## #9

#### 베타 분포

#### References

---

## #10

#### 감마 분포

#### References

---
