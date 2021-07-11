<div align='center'>
  <h1>🔻 Algorithm 🔻</h1>
</div>

> 질문은 <strong>[WeareSoft님의 tech-interview](https://github.com/WeareSoft/tech-interview)</strong>를 참고하였으며, 질문에 대한 답변은 직접 작성하였습니다.

---

## Table of Contents

- [시간, 공간 복잡도](#1)
- [Sort Algorithm](#2)
  - [Bubble Sort](#2-1)
  - [Selection Sort](#2-2)
  - [Insertion Sort](#2-3)
  - [Merge Sort](#2-4)
  - [Heap Sort](#2-5)
  - [Quick Sort](#2-6)
  - [Counting Sort](#2-7)
  - [Radix Sort](#2-8)
- [Divide and Conquer](#3)
- [Dynamic Programming](#4)
- [Greedy Algorithm](#5)
- [Graph](#6)
  - [Graph Traversal: BFS, DFS](#6-1)
  - [Shortest Path](#6-2)
    - [Dijkstra](#6-2-1)
    - [Floyd-Warshall](#6-2-2)
    - [Bellman-Ford](#6-2-3)
  - [Minimum Spanning Tree](#6-3)
    - [Prim](#6-3-1)
    - [Kruskal](#6-3-2)
  - [Union-find](#6-4)
  - [Topological Sort](#6-5)

---

## #1

#### 시간, 공간 복잡도

#### References

---

## #2

#### Sort Algorithm

#### References

---

## #2-1

#### Bubble Sort

#### References

---

## #2-2

#### Selection Sort

#### References

---

## #2-3

#### Insertion Sort

#### References

---

## #2-4

#### Merge Sort

#### References

---

## #2-5

#### Heap Sort

#### References

---

## #2-6

#### Quick Sort

#### References

---

## #2-7

#### Counting Sort

#### References

---

## #2-8

#### Radix Sort

#### References

---

## #3

#### Divide and Conquer

분할 정복(Divide and Conquer)은 문제를 **분할**해서 분할한 문제를 **해결**한 다음 결과를 **조합**하는 알고리즘이다. 큰 문제를 작은 문제로 분할한다는 관점에서 하향식 접근 방법으로 문제를 푼다고 볼 수 있다.

- **분할**: 문제를 동일한 유형의 여러 하위 문제로 나누는 것
- **해결**: 가장 작은 단위의 하위 문제를 해결하는 것
- **조합**: 하위 문제에 대한 결과를 원래 문제에 대한 결과로 조합하는 것

분할 정복 알고리즘은 보통 재귀를 사용하여 구현한다. 다음은 분할 정복의 대표적인 문제인 피보나치 수열 코드이다.

```python
def fibb(n):
  if n <= 1:
    return 1
  return fibb(n-1) + fibb(n-2)
```

#### References

- [Divide-and-conquer algorithm - Wikipedia](https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm)
- [22장. 분할 정복 - 파이썬 알고리즘 인터뷰](http://www.yes24.com/Product/Goods/91084402)

---

## #4

#### Dynamic Programming

다이나믹 프로그래밍(Dynamic Programming)은 **중복된 하위 문제들의 결과를 저장**한 후 원래 문제의 결과와 합하는 알고리즘이다.

다이나믹 프로그래밍과 분할 정복 알고리즘의 큰 차이점은 **중복된 문제**의 차이이다. 분할 정복 알고리즘을 사용한 병합 정렬이나 퀵 정렬의 경우 하위 문제들이 중복되지 않는다. 반면 다이나믹 프로그래밍은 중복된 하위 문제들의 결과를 저장함으로써 중복 계산을 피한다. 만약 문제가 중복된 하위 문제가 없다면 그 문제는 다이나믹 프로그래밍으로 풀 수 없다.

다이나믹 프로그래밍은 크게 상향식과 하향식 접근법으로 나뉜다.

> **상향식 접근법: 타뷸레이션(Tabulation)**

상향식 접근법(Bottom-Up Approach)는 작은 문제의 정답을 이용해 큰 문제의 정답을 푸는 방식이다. 데이터를 테이블 형태로 저장하기 때문에 `타뷸레이션(Tabulation)`이라고 부른다.

```python
def fibb(n):
  table = [1] * (n+1)
  for i in range(2, n+1):
    table[i] = table[i-1] + table[i-2]
  return table[n]
```

> **하향식 접근법: 메모이제이션(Memoization)**

하향식 접근법(Top-Down Approach)는 작은 문제의 결과를 얻었는지 확인해가며 문제를 재귀로 풀어가는 방식이다. 분할 정복에서의 재귀 방식과 유사하나 이미 푼 문제인지 검사한다. 이와 같은 방식을 `메모이제이션(Memoization)`이라고 부른다.

```python
# 전역 변수로 table과 n이 미리 선언됨
def fibb(n):
  if n <= 1:
    return 1
  if table[n]:
    return table[n]
  table[n] = fibb(n-1) + fibb(n-2)
  return table[n]
```

#### References

- [23장. 다이나믹 프로그래밍 - 파이썬 알고리즘 인터뷰](http://www.yes24.com/Product/Goods/91084402)

---

## #5

#### Greedy Algorithm

#### References

---

## #6

#### Graph

#### References

---

## #6-1

#### Graph Traversal: BFS, DFS

#### References

---

## #6-2

#### Shortest Path

#### References

---

## #6-2-1

#### Dijkstra

#### References

---

## #6-2-2

#### Floyd-Warshall

#### References

---

## #6-2-3

#### Bellman-Ford

#### References

---

## #6-3

#### Minimum Spanning Tree

#### References

---

## #6-3-1

#### Prim

#### References

---

## #6-3-2

#### Kruskal

#### References

---

## #6-4

#### Union-find

`유니온-파인드(Union-find)` 혹은 `서로소 집합(Disjoint Sets)` 자료구조는 서로소 부분 집합들로 나눠진 원소들에 대한 정보를 다루는 자료구조이다. 유니온-파인드 자료구조는 다음과 같이 합집합(Union)과 찾기(Find) 연산을 제공한다.

- **합집합(Union)**: 두 개의 집합을 하나의 집합으로 합친다.
  - 서로 연결할 두 노드 A, B가 있다고 할 때, A와 B의 루트 노드인 A'과 B'을 찾는다.
  - A'을 B'의 부모 노드로 혹은 B'을 A'을 부모 노드로 설정한다.
- **찾기(Find)**: 노드가 속한 집합을 반환한다.

구현 방법은 [개선된 서로소 집합 알고리즘 (경로 압축) - 이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test/blob/master/10/3.py) 구현 코드를 참고!

> **유니온-파인드 자료구조의 활용**

유니온-파인드 자료구조를 이용해 <u><strong>무방향 그래프 내에서의 사이클</strong>을 판별</u>할 수 있다. 합집합 연산은 그래프의 간선으로 대응된다고 할 때, 다음과 같은 알고리즘으로 사이클을 판별할 수 있다.

- 간선으로 연결된 두 노드의 루트 노드를 확인한다.
- 만약 루트 노드가 서로 다르다면 합집합 연산을 수행한다.
- 만약 루트 노드가 같다면 사이클이 발생했다고 판단한다.

구현 방법은 [서로소 집합을 활용한 사이클 판별 - 이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test/blob/master/10/4.py) 구현 코드를 참고!

#### References

- [서로소 집합 자료 구조 - 위키백과](https://ko.wikipedia.org/wiki/%EC%84%9C%EB%A1%9C%EC%86%8C_%EC%A7%91%ED%95%A9_%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0)
- [Chapter 10. 그래프 이론 - 이것이 취업을 위한 코딩테스트다](http://www.yes24.com/Product/Goods/91433923)

---

## #6-5

#### Topological Sort

`위상 정렬(Topological Sort)`란 <u><strong>방향 그래프</strong>의 모든 노드를 선행 순서를 지키며 정점을 순서대로 나열하는 것</u>이다. 위상 정렬의 대표적인 예로 대학교 선수과목이 있다. 위상 정렬 알고리즘은 다음과 같다.

- 진입차수가 0인 노드를 큐에 넣는다.
- 큐가 빌 때가지 다음을 반복한다.
  - 큐에서 요소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
  - 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

만약 모든 노드를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다. 왜냐하면 사이클이 존재하는 경우 사이클을 형성하는 노드들의 진입차수가 항상 1 이상이므로 큐에 넣을 수가 없기 때문이다.

구현 방법은 [위상 정렬 - 이것이 취업을 위한 코딩테스트다](https://github.com/ndb796/python-for-coding-test/blob/master/10/6.py) 구현 코드를 참고!

> **진입 차수(degree)**
> 노드의 관점에서 들어오는 간선의 개수를 진입 차수(degree)라고 한다.

#### References

- [[알고리즘] 위상 정렬(Topological Sort)이란](https://gmlwjd9405.github.io/2018/08/27/algorithm-topological-sort.html)
- [위상정렬 - 위키백과](https://ko.wikipedia.org/wiki/%EC%9C%84%EC%83%81%EC%A0%95%EB%A0%AC)

---
