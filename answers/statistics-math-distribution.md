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

#### References

---

## #7

#### 카이제곱 분포

#### References

---

## #8

#### F 분포

#### References

---

## #9

#### 베타 분포

#### References

---

## #10

#### 감마 분포

#### References

---
