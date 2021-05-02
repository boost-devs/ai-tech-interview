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

우선 베르누이 시행이란 결과가 두 가지 중 하나만 나오는 것을 말한다. 베르누이 확률변수는 시행결과가 0 또는 1이 나오므로 이산확률변수이다.

- `pmf` : <!-- $Bern(x;\theta) = \theta^x(1-\theta)^{1-x}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=Bern(x%3B%5Ctheta)%20%3D%20%5Ctheta%5Ex(1-%5Ctheta)%5E%7B1-x%7D">
- `expectation` : <!-- $E[X] = \theta$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=E%5BX%5D%20%3D%20%5Ctheta">
- `variance` : <!-- $Var[X] = \theta ( 1-\theta)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=Var%5BX%5D%20%3D%20%5Ctheta%20(%201-%5Ctheta)">

#### References

- [확률분포 : 베르누이분포, 이항분포, 카테고리분포, 다항분포 - Fall in Machine-Learning](https://imjuno.tistory.com/entry/basicdistribution)
- [8.2 베르누이분포와 이항분포 - 데이터 사이언스 스쿨](https://datascienceschool.net/02%20mathematics/08.02%20%EB%B2%A0%EB%A5%B4%EB%88%84%EC%9D%B4%EB%B6%84%ED%8F%AC%EC%99%80%20%EC%9D%B4%ED%95%AD%EB%B6%84%ED%8F%AC.html)

---

## #2

#### 이항 분포

베르누이 시행을 N번 시행한 것을 말한다. 예를 들어, 동전 던지기를 10번 던져서 앞면이 나온 횟수를 확률 변수로 둔다. 마찬가지로 시행 결과가 횟수로 나오므로 이산확률변수이다.

- `pmf` : <!-- $Bin(x;N, \theta) = \left(\begin{array}{c}N\\ x\end{array}\right) \theta^N (1-\theta)^{N-x}$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=Bin(x%3BN%2C%20%5Ctheta)%20%3D%20%5Cleft(%5Cbegin%7Barray%7D%7Bc%7DN%5C%5C%20x%5Cend%7Barray%7D%5Cright)%20%5Ctheta%5EN%20(1-%5Ctheta)%5E%7BN-x%7D">
- `expectation` : <!-- $E[X] = N\theta$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=E%5BX%5D%20%3D%20N%5Ctheta">
- `variance` : <!-- $Var[X] = N\theta ( 1-\theta)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=Var%5BX%5D%20%3D%20N%5Ctheta%20(%201-%5Ctheta)">

#### References

- [확률분포 : 베르누이분포, 이항분포, 카테고리분포, 다항분포 - Fall in Machine-Learning](https://imjuno.tistory.com/entry/basicdistribution)
- [8.2 베르누이분포와 이항분포 - 데이터 사이언스 스쿨](https://datascienceschool.net/02%20mathematics/08.02%20%EB%B2%A0%EB%A5%B4%EB%88%84%EC%9D%B4%EB%B6%84%ED%8F%AC%EC%99%80%20%EC%9D%B4%ED%95%AD%EB%B6%84%ED%8F%AC.html)

---

## #3

#### 카테고리 분포

카테고리 분포(Categorical distribution)는 베르누이 분포를 확장한 개념이다. 즉 카테고리 시행(여러개의 카테고리 중 하나를 선택하는 실험)의 결과는 카테고리 분포를 따르게 된다. 카테고리 분포를 누적하면 다항분포를 얻게 된다.

카테고리 확률변수는 one-hot vector로 표현할 수 있다. 예를 들어, 주사위의 경우 K=6인 카테고리 분포를 따른다고 표기할 수 있다. 눈이 2인 주사위면이 나왔다고 할때, 이때 카테고리 RV = [0,1,0,0,0,0]이 된다. RV안의 각 원소들은 베르누이 분포를 따르고, 각각 자신들만의 모수를 갖는다.

카테고리가 K개일 때, 카테고리 분포의 확률질량함수는 아래와 같다.

<img src="/images/sally/2021-05-01-23-49-44.png" width="50%">  

<img src="/images/sally/2021-05-01-23-46-12.png" width="50%">  

> RV = Random Variable = 확률변수

#### References

- [카테고리 분포와 다항분포 - 계량투자 실험실](https://gem763.github.io/probability%20theory/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC-%EB%B6%84%ED%8F%AC%EC%99%80-%EB%8B%A4%ED%95%AD%EB%B6%84%ED%8F%AC.html)
- [갈아먹는 통계 기초1.확률 분포 정리 - 갈아먹는 머신러닝](https://yeomko.tistory.com/33)

---

## #4

#### 다항 분포

성공확률이 θ인 베르누이 시행을 n번 반복했을 때의 성공횟수가 이항분포를 따르는 것처럼, 성공확률이 <!-- $\theta=(\theta_1 ... \theta_k)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=%5Ctheta%3D(%5Ctheta_1%20...%20%5Ctheta_k)">인 카테고리 시행을 n번 반복했을 때의 각 카테고리별 성공횟수는 다항분포(Multinomial distribution)을 따르게 된다.  

<img src="/images/sally/2021-05-01-23-33-36.png" width="50%">  

다항분포의 수식은 아래와 같다.  

<img src="/images/sally/2021-05-01-23-43-27.png" width="60%">

> 예를들어, 주사위를 10번 던졌을 때, 1이 1번, 2가 2번, 3이 1번, 4가2번, 5가 3번, 6이 1번 나오는 확률을 계산하고자 한다. 이를 벡터로 나타내면 (1, 2, 1, 2, 3, 1)이 된다. 6번을 던졌을 때 x벡터처럼 나올 조합을 계산해야하며, 수식은 아래와 같다.  

<img src="/images/sally/2021-05-01-23-52-20.png" width="40%">  

#### References

- [카테고리 분포와 다항분포 - 계량투자 실험실](https://gem763.github.io/probability%20theory/%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC-%EB%B6%84%ED%8F%AC%EC%99%80-%EB%8B%A4%ED%95%AD%EB%B6%84%ED%8F%AC.html)
- [갈아먹는 통계 기초1.확률 분포 정리 - 갈아먹는 머신러닝](https://yeomko.tistory.com/33)

---

## #5

#### 가우시안 정규 분포

평균을 중심으로 좌우가 대칭인 종 모양을 그리는 정규분포이다. 정규 분포의 확률 밀도 함수와 그 그래프는 아래와 같다.  
<img src="/images/sally/2021-05-01-23-57-40.png" width="80%">  
<img src="/images/sally/2021-05-01-23-57-57.png" width="60%">  

정규 분포 식에서 변수는 <!-- $x$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=x">이다. σ와 μ는 그래프를 종모양으로 만드는데 사용된다. μ는 확률 변수 X의 평균이고 σ는확률 변수 X의 표준 편차이다. 종 모양의 그래프는 평균을 기준으로 좌우 대칭을 이룬다. 표준 편차가 높을 수록 그래프는 완만한 곡선 형태를 띄게 된다. 

#### References

- [갈아먹는 통계 기초1.확률 분포 정리 - 갈아먹는 머신러닝](https://yeomko.tistory.com/33)

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

#### 감마 분포
감마 분포는 **감마 함수**를 사용하여 전체 **k번의 사건**이 일어날 때까지 **걸리는 시간**을 나타내는 연속 확률분포이다.

theta 와 k 는 감마 분포의 모수이다.

감마 분포는 0~무한대까지 값을 가질 수 있으며 모수의 베이지안 추정을 위해 사용된다.

<div align='center'>
<img src='https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/gamma_dist_formula.png' height='100px'/>
</div>
<br>

<div align='center'>
<img src='https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/gamma_dist.png' height='240px'/>
</div>
<br>

**감마 함수**  
**팩토리얼**을 함수로 일반화한 것  

<div align='center'>
<img src='https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/gamma_function.png' height='100px'/>
</div>
<br>

#### References
- [갈아먹는 통계 기초 [1] 확률 분포 정리 - 갈아먹는 머신러닝](https://yeomko.tistory.com/33)
- [8.7 베타분포, 감마분포, 디리클레분포 - datascience school](https://datascienceschool.net/02%20mathematics/08.07%20%EB%B2%A0%ED%83%80%EB%B6%84%ED%8F%AC,%20%EA%B0%90%EB%A7%88%EB%B6%84%ED%8F%AC,%20%EB%94%94%EB%A6%AC%ED%81%B4%EB%A0%88%20%EB%B6%84%ED%8F%AC.html)

---

## #10

#### 베타 분포
베타 분포는 두 모수 a, b 에 대한 **베타 함수**를 나타내는 연속확률분포이다.

베타 함수는 이항 계수 (조합, combination 으로도 불림) 를 나타내는 함수인데, 이항 계수는 팩토리얼로 이루어져있기 때문에 베타 함수는 감마 함수로 나타낼 수 있다.

베타 분포의 값은 0~1 사이이며 감마 분포와 마찬가지로 베이지안 추정을 위해 사용된다.

<div align='center'>
<img src='https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/beta_dist_formula.png' height='100px'/>
</div>
<br>

<div align='center'>
<img src='https://github.com/boostcamp-ai-tech-4/ai-tech-interview/blob/main/images/heath/beta_dist.png' height='240px'/>
</div>
<br>


#### References
- [갈아먹는 통계 기초 [1] 확률 분포 정리 - 갈아먹는 머신러닝](https://yeomko.tistory.com/33)
- [8.7 베타분포, 감마분포, 디리클레분포 - datascience school](https://datascienceschool.net/02%20mathematics/08.07%20%EB%B2%A0%ED%83%80%EB%B6%84%ED%8F%AC,%20%EA%B0%90%EB%A7%88%EB%B6%84%ED%8F%AC,%20%EB%94%94%EB%A6%AC%ED%81%B4%EB%A0%88%20%EB%B6%84%ED%8F%AC.html)

---
