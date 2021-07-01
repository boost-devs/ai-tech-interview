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
  - [Topological sort](#6-5)

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

#### References

---

## #4

#### Dynamic Programming

#### References

---

## #5

#### Greedy Algorithm

#### References

---

## #6

#### Graph

그래프는 정점과 간선으로 이루어진 자료구조이다. 정점 간의 연결관계는 간선으로 나타낸다.

##### 그래프의 종류

<img src="/images/sally/2021-07-01-13-15-10.png" width="50%">

간선이 담고있는 정보와 연결 상태에 따라 그래프의 종류가 나뉜다. 두 정점을 연결하는 간선에 방향이 없다면 `무방향 그래프`, 두 정점을 연결하는 간선에 방향이 존재하면 `방향 그래프`라고 부른다. 방향 그래프는 간선의 방향으로만 이동할 수 있다. 두 정점을 이동할 때 비용이 발생하면 `가중치 그래프`로 나타낼 수 있다. 모든 정점이 간선으로 연결된 경우, `완전 그래프`라고 부른다.

##### 그래프 구현 방식

- 인접행렬 방식
  <img src="/images/sally/2021-07-01-12-54-57.png" width="60%">
  - 노드를 인덱스로 삼는 2차원 배열을 만든다.
  - 각 노드가 간선으로 연결되어있으면 배열에 1을 넣어주고, 연결되지 않았다면 0을 넣어준다.
  - 두 노드의 연결관계를 조회할 때, O(1) 시간이 걸린다.
  - 그러나 모든 정점에 대해, 간선 정보를 입력해야하므로 초기화에 <!-- $O(N^2)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=O(N%5E2)"> 시간이 소요된다.
  - 노드의 수가 많고, 간선의 수가 적은 그래프의 경우에, 공간을 낭비하게 된다.
- 인접리스트 방식
  <img src="/images/sally/2021-07-01-12-55-08.png" width="70%">
  - 그래프의 노드들을 리스트로 표현한다. head 노드와 연결된 노드들을 링크에 달아준다.
  - 한 정점에 연결된 노드들의 정보를 얻기 위해서 O(M) 시간이 걸린다.(M: 간선의 수)
  - 간선 정보만 유지하므로, 공간 낭비가 적다.
  - 두 정점이 연결되었는지 확인하기 위해서 O(M) 시간이 걸리며, 구현이 비교적 어렵다.
  
##### 그래프 용어

그래프에서 사용하는 용어는 다음과 같다.

- `정점(vertice)` : 노드(node)라고도 하며 정점에는 데이터가 저장된다.
- `간선(edge)`: 링크(arcs)라고도 하며 노드간의 관계를 나타낸다.
- `인접 정점(adjacent vertex)` : 간선에 의해 직접 연결된 정점이다.
- `단순 경로(simple-path)` : 경로 중 반복되는 정점이 없는것, 같은 간선을 자나가지 않는 경로이다.
- `차수(degree)` : 무방향 그래프에서 하나의 정점에 인접한 정점의 수이다.
- `진출 차수(out-degree)` : 방향그래프에서 사용되는 용어로 한 노드에서 외부로 향하는 간선의 수를 뜻한다.
- `진입차수(in-degree)` : 방향그래프에서 사용되는 용어로 외부 노드에서 들어오는 간선의 수를 뜻한다.

#### References

- [[Algorithm] 자료구조 그래프(Graph)란 무엇인가? - 코딩팩토리](https://coding-factory.tistory.com/610)

---

## #6-1

#### Graph Traversal: BFS, DFS

##### BFS(Breadth-First Search, 너비우선탐색)

BFS는 그래프 전체를 탐색하는 방법 중 하나로써, 현재 확인하는 노드의 인접한 노드들을 먼저 탐색하는 것이다. 시작 정점으로부터 가까운 정점을 먼저 방문하고 멀리 떨어져 있는 정점을 나중에 방문하는 순회하는 방식으로 노드를 탐색한다. 주로 구현은 Queue라는 자료구조에 이웃하는 정점을 다 담아놓고 차례대로 pop을 하는 방식으로 구현한다. 주로 두 노드 사이의 최단 경로 혹은 임의의 경로를 찾고 싶을 때 이 방법을 사용한다.

- BFS의 장점
  1. 노드의 수가 적고 깊이가 얕은 경우 빠르게 동작할 수 있다.
  2. 단순 검색 속도가 깊이 우선 탐색(DFS)보다 빠르다.
  3. 너비를 우선 탐색하기에 답이 되는 경로가 여러개인 경우에도 최단경로임을 보장한다.
  4. 최단경로가 존재한다면 어느 한 경로가 무한히 깊어진다해도 최단경로를 반드시 찾을 수 있다.
- BFS의 단점
  1. 재귀호출의 DFS와는 달리 큐에 다음에 탐색할 정점들을 저장해야 하므로 저장공간이 많이 필요하다.
  2. 노드의 수가 늘어나면 탐색해야하는 노드 또한 많아지기에 비현실적이다.

##### DFS(Depth-First Search, 깊이우선탐색)

DFS는 그래프 전체를 탐색하는 방법중 하나로써, 시작점 부터 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하고 넘어가는 방법이다. 먼저 보이는 노드부터 계속해서 깊이를 늘려가며 탐색하고, 더 이상 탐색할 노드가 없다면 이전 노드로 돌아가서 다른 브랜치를 다시 깊이 파보는 형식을 말한다. Stack이나 재귀함수를 통해서 구현할 수 있는데, 재귀함수가 구현이 간편하다.

- DFS의 장점
  1. 현재 경로 상의 노드들만 기억하면 되므로, 저장 공간의 수요가 비교적 적다.
  2. 목표 노드가 깊은 단계에 있는 경우에도 해를 빨리 구할 수 있다.
  3. 구현이 너비 우선 탐색(BFS) 보다 간단하다.
- DFS의 단점
  1. 단순 검색 속도는 너비 우선 탐색(BFS) 보다 느리다.
  2. 깊이 우선 탐색은 해를 구하면 탐색이 종료되므로, 구한 해가 최단 경로가 된다는 보장이 없다. 목표에 이르는 경로가 다수인 경우, DFS를 통해 구한 해가 최적이 아닐 수 있다. DFS를 사용하여 최단 경로를 구하기 위해서는, 모든 경로를 전부 확인해보아야 한다.

> BFS와 DFS의 탐색 순서

<img src="/images/sally/2021-07-01-13-31-50.png" width="70%">

> 주의해야할 것

노드를 Queue 혹은 Stack에 넣을 때, 방문 여부를 반드시 표시해주어야 한다. 그렇지 않으면, 자료구조에 노드가 중복되게 들어갈 수 있기 때문이다. 방문 표시를 하지 않으면, 심한 경우에는 무한루프에 빠질 수도 있다.

#### References

- [[Algorithm] BFS 알고리즘 (Breadth-First Search) - 코딩팩토리](https://coding-factory.tistory.com/612)
- [[Algorithm] DFS 알고리즘 (Depth First Search) - 코딩팩토리](https://coding-factory.tistory.com/611)

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

##### Spanning Tree

Spanning Tree(신장 트리)란 그래프에서 일부 간선을 선택해서 만든, 그래프 내의 모든 정점을 포함하는 트리를 말한다.

Spanning Tree는 그래프의 `최소 연결 부분 그래프` 이다. `최소 연결`의 의미는 간선의 수가 가장 적다는 것이다. n개의 정점을 가지는 그래프가 모두 이어지기 위해서는 최소 (n-1)개의 간선이 필요하다. n개의 노드를 가지는 그래프에서 (n-1)개의 간선으로 연결되어 있으면 필연적으로 트리 형태가 되고, 이를 spanning tree라고 부른다. 또한, 트리 형식을 만족해야하므로 사이클을 포함해서는 안된다. DFS, BFS을 통해 탐색 도중에 사용된 간선만 모아서 이어주면, 그래프에서 신장 트리를 찾을 수 있다. 하나의 그래프에는 많은 신장 트리가 존재할 수 있다.

##### Minimum Spanning Tree

MST(Minimum Spanning Tree, 최소 신장 트리)란 Spanning Tree 중에서 사용된 간선들의 가중치 합이 최소인 트리를 말한다.

MST는 간선에 가중치를 고려하여 최소 비용의 Spanning Tree를 선택하는 것을 말한다. 즉, 네트워크(가중치를 간선에 할당한 그래프)에 있는 모든 정점들을 가장 적은 수의 간선과 비용으로 연결하는 것이다.
MST는 **간선의 가중치의 합이 최소**여야 한다는 특징이 있다. 이 외에도 "n개의 정점을 가지는 그래프에 대해 **반드시 (n-1)개의 간선만을 사용**해야 한다"거나 "**사이클이 포함되어서는 안된다**"는 등의 spanning tree의 특징도 포함한다.

MST를 구현하기 위해서 `Kruskal MST 알고리즘` 혹은 `Prim 알고리즘`이 사용된다. 그래프 내에 적은 숫자의 간선만을 가지는 `희소 그래프(Sparse Graph)`의 경우 Kruskal 알고리즘이 적합하고, 그래프에 간선이 많이 존재하는 `밀집 그래프(Dense Graph)` 의 경우는 Prim 알고리즘이 적합하다.

#### References

- [[알고리즘] 최소 신장 트리(MST, Minimum Spanning Tree)란 - heejeong Kwon](https://gmlwjd9405.github.io/2018/08/28/algorithm-mst.html)

---

## #6-3-1

#### Prim

Prim 알고리즘이란 시작 정점에서부터 출발하여 신장트리 집합을 단계적으로 확장해나가는 방법이다. **정점 선택**을 기반으로 하는 알고리즘이며, 이전 단계에서 만들어진 신장 트리를 확장하면서 나아가는 방법이다. Prim 알고리즘의 동작방법은 아래와 같다.

- 시작 단계에서는 시작 정점만이 MST(최소 비용 신장 트리) 집합에 포함된다.
- 앞 단계에서 만들어진 MST 집합에 인접한 정점들 중에서 최소 간선으로 연결된 정점을 선택하여 트리를 확장한다.
- 즉, 가장 낮은 가중치를 먼저 선택한다.
- 위의 과정을 트리가 (N-1)개의 간선을 가질 때까지 반복한다.

Prim 알고리즘의 시간 복잡도는, 주 반복문이 정점의 수 n만큼 반복하고, 내부 반복문이 n번 반복되므로, <!-- $O(n^2)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=O(n%5E2)"> 이다.

> Prim 알고리즘의 수행 단계

<img src="/images/sally/2021-07-01-14-23-56.png" width="70%">

#### References

- [[알고리즘] Prim 알고리즘 이란 - heejeong Kwon](https://gmlwjd9405.github.io/2018/08/30/algorithm-prim-mst.html)

---

## #6-3-2

#### Kruskal

Kruskal 알고리즘이란 **간선 선택**을 기반으로 하는 알고리즘으로, 이전 단계에서 만들어진 신장 트리와는 상관없이 무조건 최소 간선만을 선택하는 방법이다. 매 단계마다 사이클을 만들지 않는 최소 간선을 채택하면 된다.

Kruskal 알고리즘은 탐욕적인 방법(greedy method)을 이용하여, 네트워크(가중치를 간선에 할당한 그래프)의 모든 정점을 최소 비용으로 연결하는 최적 해답을 구하는 방법이다. MST(최소 비용 신장 트리)가 **최소 비용의 간선으로 구성**되며, **사이클을 포함하지 않는다**는 조건에 근거하여, 최적해를 보장할 수 있다. 각 단계에서 사이클을 이루지 않는 최소 비용 간선을 선택하면 된다.

주의할 점은 다음 간선을 `이미 선택된 간선들의 집합`에 추가할 때 사이클을 생성하는지를 체크해야 한다는 것이다. 새로운 간선이 `이미 다른 경로에 의해 연결되어 있는 정점들`을 연결할 때 사이클이 형성된다. 즉, 추가할 새로운 간선의 양끝 정점이 같은 집합에 속해 있으면, 사이클이 형성된다. 따라서, 추가하고자 하는 간선의 양끝 정점이 같은 집합에 속해 있는지를 먼저 검사해야 하고, 이때 `union-find 알고리즘`을 사용하여 검사할 수 있다.

Kruskal 알고리즘의 동작방법은 아래와 같다.

- 그래프의 간선들을 가중치의 오름차순으로 정렬한다.
- 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다.
- 즉, 가장 낮은 가중치를 먼저 선택한다.
- 사이클을 형성하는 간선을 제외한다.
- 해당 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가한다.

Kruskal 알고리즘의 시간 복잡도는 O(elog₂e)이다.

> Kruskal 알고리즘 수행 단계

<img src="/images/sally/2021-07-01-14-31-20.png" width="90%">

#### References

- [[알고리즘] Kruskal 알고리즘 이란 - heejeong Kwon](https://gmlwjd9405.github.io/2018/08/29/algorithm-kruskal-mst.html)

---

## #6-4

#### Union-find

#### References

---

## #6-5

#### Topological sort

#### References

---
