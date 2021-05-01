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
