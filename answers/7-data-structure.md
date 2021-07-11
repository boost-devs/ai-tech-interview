<div align='center'>
  <h1>🗂 Data Structure 🗂</h1>
</div>

> 질문은 <strong>[WeareSoft님의 tech-interview](https://github.com/WeareSoft/tech-interview)</strong>를 참고하였으며, 질문에 대한 답변은 직접 작성하였습니다.

---

## Table of Contents

- [linked list](#1)
  - [single linked list](#1-1)
  - [double linked list](#1-2)
  - [circular linked list](#1-3)
- [hash table](#2)
- [stack](#3)
- [queue](#4)
  - [circular queue](#4-1)
- [graph](#5)
- [tree](#6)
  - [binary tree](#6-1)
  - [full binary tree](#6-2)
  - [complete binary tree](#6-3)
  - [bst(binary search tree)](#6-4)
- [heap(binary heap)](#7)
  - [min heap](#7-1)
  - [max heap](#7-2)
- [red-black tree](#8)
- [b+ tree](#9)

---

## #1

#### linked list

array는 데이터가 연속적인 공간에 존재해야 한다는 특징이 있으나, linked list는 서로 떨어져 있는 데이터를 메모리 주소를 참조함으로써, 이어진 것처럼 사용할 수 있다. linked list는 구조체가 이어진 형태로 존재하며, 이 구조체를 `노드`라고 부른다. 노드는 값을 담고 있는 `데이터 필드`와 다음 구조체를 가리키는 `링크 필드(포인터)`로 구성된다. 정확히는, 포인터가 다음 구조체의 주소를 담고 있다. 보통, linked list의 맨 첫 원소를 가리키는 head 포인터와 맨 마지막 원소를 가리키는 tail 포인터를 통해, 리스트의 요소에 접근하거나 수정한다. linked list는 구현 방법에 따라, single linked list와 double linked list, circular linked list 등으로 구분할 수 있다.

> Array vs. Linked list

array에서 중간에 값을 삽입하고 싶다면, 삽입할 위치 뒤의 모든 데이터가 한 칸씩 이동해야 한다는 단점이 있다. 또한, array가 할당받은 공간이 부족한데, 메모리상 뒤쪽의 메모리가 비어있지 않으면, 모든 데이터가 더 큰 홀로 이사를 가야 한다는 단점도 존재한다. linked list는 연속된 공간을 사용하지 않아도 되기 때문에 앞서 언급했던 array의 단점을 모두 해소할 수 있다. 그러나 N번째 데이터를 참조하고 싶을 때, 계속해서 다음 주소를 참조하는 형식으로 따라가야 하므로 메모리 참조에 시간이 오래 걸린다. 따라서 삽입과 삭제가 빈번한 경우에는 linked list를 사용하고, 참조가 빈번하게 일어날 때는 array를 쓰는 것이 바람직하다.

> Time Complexity 비교

- array
  - insert: O(N)
  - delete: O(N)
  - find: O(1)
- list
  - insert: O(1)
  - delete: O(1)
  - find: O(N)

> 삽입, 삭제, 접근 방법

- 접근
  - 원하는 원소가 나올때까지 링크 필드(포인터, 다음 노드)를 계속해서 탐색한다.
- 삽입
  1. 삽입할 노드의 next에 현재 위치의 next를 연결한다.
  2. 현재 위치의 next에 삽입할 노드의 주소를 넣어준다.
- 삭제
  - 삭제할 노드의 next를 앞선 노드의 next에 연결해준다.

> 기본적인 linked list 구조 (=Single linked list 구조)

![linked list](/images/sally/2021-07-01-04-51-16.png)

---

## #1-1

#### single linked list

<img src="/images/sally/2021-07-01-05-07-59.png" width="60%">

[#1 Linked list](#1)에서 언급한 내용은 모두 Single linked list에 해당한다. Single linked list는 linked list 중에서도 가장 기본적인 구조로 되어 있으며, head에서 tail까지 단방향으로 포인터가 이어져 있으므로 N 번째 노드에서 N-1 번째 노드에 접근할 수 없다. 대신, 다시 head로부터 N-1 번의 탐색을 통해 접근해야 한다.

#### References

- [연결 리스트의 개념과 종류 - suitepotato](https://velog.io/@suitepotato/00007)

---

## #1-2

#### double linked list

<img src="/images/sally/2021-07-01-05-12-52.png" width="60%">

[#1-1 Single linked list](#1-1)은 단방향 연결이기 때문에 한번 다음 노드로 이동하면, 이전 노드로 돌아가기 힘들다는 단점이 있었다. 그러나 Double linked list는 뒤의 노드의 주소뿐만 아니라, 이전 노드의 주소도 담고 있다. 하나의 노드는 하나의 데이터와 두 개의 링크를 가지고 있으며, 각각의 링크를 prev와 next라고 부른다. 다음 노드를 참조하고 싶다면 next 링크가 담고 있는 주소를 확인하면 되고, 이전의 노드를 참조하고 싶다면 prev 링크가 가지는 주소를 확인하면 된다.

#### References

- [연결 리스트의 개념과 종류 - suitepotato](https://velog.io/@suitepotato/00007)

---

## #1-3

#### circular linked list

<img src="/images/sally/2021-07-01-05-12-42.png" width="60%">

앞서 언급했던 linked list 유형들과는 다르게, tail이 다시 head를 가리키는 구조를 가지고 있다. 따라서, tail 노드의 next에는 NULL이 들어가는 것 대신, head의 주소가 들어간다.

#### References

- [연결 리스트의 개념과 종류 - suitepotato](https://velog.io/@suitepotato/00007)

---

## #2

#### hash table

해시 테이블은 (Key, Value)로 데이터를 저장하는 자료구조 중 하나로 빠르게 데이터를 검색할 수 있는 자료구조이다. 해시 테이블이 빠른 검색속도를 제공하는 이유는 내부적으로 배열(버킷)을 사용하여 데이터를 저장하기 때문이다. 해시 테이블은 각각의 Key값에 해시함수를 적용해 배열의 고유한 index를 생성하고, 이 index를 활용해 값을 저장하거나 검색하게 된다. 여기서 실제 값이 저장되는 장소를 버킷 또는 슬롯이라고 한다.

![img](/images/sally/2021-07-01-05-31-53.png)

예를 들어, `(Key, Value)쌍` 구조를 가지는 데이터 `("John Smith", "521-1234")`를 크기가 16인 해시 테이블에 저장한다고 하자. 그러면 먼저 `index = hash_function("John Smith") % 16` 연산을 통해 index 값을 계산한다. 그리고 `array[index] = "521-1234"` 로 value를 저장하게 된다. 이러한 구조로 데이터를 저장하면 Key값으로 데이터를 찾을 때 해시 함수를 1번만 수행하면 되므로 매우 빠르게 데이터를 저장/삭제/조회할 수 있다. 해시테이블의 평균 시간복잡도는 O(1)이다.

> 해시(Hash)값이 충돌하는 경우

만약 "John Smith"를 해시 함수를 돌려 나온 값과 "Sandra Dee"를 해시 함수를 돌려 나온 값이 동일하다면, 아래와 같이 해결할 수 있다.

**해결방법 1: Separate Chaining(분리 연결법)**

![img](/images/sally/2021-07-01-05-35-24.png)

동일한 버킷의 데이터에 대해 자료구조를 활용해 추가 메모리를 사용하여 다음 데이터의 주소를 저장하는 방법이다. 동일한 해시 값을 가지면, 동일한 버킷 안에 엔트리를 할당해줘야한다. 이 때, 버킷 내부의 엔트리 값들은 linked list 형태로 이어준다. 이러한 Chaining 방식은 해시 테이블의 확장이 필요없고 간단하게 구현이 가능하며, 손쉽게 삭제할 수 있다는 장점이 있다. 하지만 데이터의 수가 많아지면 동일한 버킷에 chaining되는 데이터가 많아지며 그에 따라 캐시의 효율성이 감소한다는 단점이 있다.

**해결방법 2: Open Addressing(개방주소법)**

Open Addressing이란 추가적인 메모리를 사용하는 Chaining 방식과 다르게 비어있는 해시 테이블의 공간을 활용하는 방법이다. Open Addressing을 구현하기 위한 대표적인 방법으로는 3가지 방식이 존재한다.

- **Linear Probing**: 현재의 버킷 index로부터 고정폭 만큼씩 이동하여 차례대로 검색해 비어 있는 버킷에 데이터를 저장한다.
- **Quadratic Probing**: 해시의 저장순서 폭을 제곱으로 저장하는 방식이다. 예를 들어 처음 충돌이 발생한 경우에는 1만큼 이동하고 그 다음 계속 충돌이 발생하면 2^2, 3^2 칸씩 옮기는 방식이다.
- **Double Hashing Probing**: 해시된 값을 한번 더 해싱하여 해시의 규칙성을 없애버리는 방식이다. 해시된 값을 한번 더 해싱하여 새로운 주소를 할당하기 때문에 다른 방법들보다 많은 연산을 하게 된다.

충돌을 방지하는 방법들은 데이터의 규칙성(클러스터링)을 방지하기 위한 방식이지만 공간을 많이 사용한다는 치명적인 단점이 있다. 만약 테이블이 꽉 차있는 경우라면 테이블을 확장해주어야 하는데, 이는 매우 심각한 성능의 저하를 불러오기 때문에 가급적이면 확정을 하지 않도록 테이블을 설계해주어야 한다. (통계적으로 해시 테이블의 공간 사용률이 70% ~ 80%정도가 되면 해시의 충돌이 빈번하게 발생하여 성능이 저하되기 시작한다고 한다.) 또한 해시 테이블에서 자주 사용하게 되는 데이터를 Cache에 적용하면 효율을 높일 수 있다. 자주 hit하게 되는 데이터를 캐시에서 바로 찾음으로써 해시 테이블의 성능을 향상시킬 수 있다.

> Time Complexity

- 삽입, 삭제, 탐색
  - 해시 충돌이 일어나지 않는 경우에 O(1), 충돌이 일어난다면 최악의 경우에 O(N)의 시간 복잡도를 가진다.
  - O(N): 해시 충돌로 인해서 하나의 버킷에 여러 엔트리가 연결되어있는 경우에 모든 엔트리를 탐색해야할 수 있다.

#### References

- [[자료구조] 해시테이블(HashTable)이란? - MangKyu's Diary](https://mangkyu.tistory.com/102)

---

## #3

#### stack

**LIFO (Last In First Out)** 구조의 자료형으로 한 쪽으로만 데이터를 넣고 뺄 수 있다.

`push` 명령으로 데이터를 넣고, `pop` 명령으로 가장 마지막에 들어간 데이터를 빼낸다.

<div align='center'>
    <img src='../images/heath/stack.png' height='250px '/>
</div>
<br/>

stack 은 브라우저의 뒤로가기 기능, ctrl + z (되돌리기), 지역 변수와 매개변수를 저장하는 stack 메모리 등에 사용된다. 이외에도 DFS 알고리즘 등 다양한 곳에 사용되는 자료형이다.

stack 에 데이터가 꽉 차서 더 넣을 공간이 없는데 데이터를 push 하는 경우 `overflow`, 반대로 데이터가 없는데 pop 하는 경우를 `underflow` 라고 한다.

#### References
- [[자료구조] 스택, 큐는 무엇인가? - 마이구미](https://mygumi.tistory.com/357)
- [[자료구조] 스택(Stack), 큐(Queue), 덱(Deque) - Choiiis](https://velog.io/@choiiis/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%EA%B3%BC-%ED%81%90Queue)

---

## #4

#### queue

**FIFO (First In First Out)** 구조의 자료형으로 출구(front)와 입구(rear or back)가 따로 존재하여 먼저 입력된 데이터가 먼저 반환된다.

`push` 명령으로 rear 에 자료를 넣는다. rear += 1 되어 다음에 데이터를 받을 메모리를 가리켜야 한다.  
`pop` 명령으로 front 에서 데이터를 빼낸다. front += 1 되어 다음에 데이터를 반환할 메모리를 가리켜야 한다.

<div align='center'>
    <img src='../images/heath/queue.png' height='150px '/>
</div>
<br/>

queue 는 CPU 연산처리 작업대기, 프린터 인쇄, 프로세스 관리 등 들어온 순서를 보장해야하는 경우 사용된다. 이외에도 BFS 알고리즘 등에 사용된다.

queue 의 rear 가 기리키는 공간에 데이터가 있는데 데이터를 push 하는 경우 `overflow`, 반대로 front 가 가리키는 공간에 데이터가 없는데 pop 하는 경우를 `underflow` 라고 한다.

#### References
- [[자료구조] 스택, 큐는 무엇인가? - 마이구미](https://mygumi.tistory.com/357)
- [[자료구조] 스택(Stack), 큐(Queue), 덱(Deque) - Choiiis](https://velog.io/@choiiis/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%EA%B3%BC-%ED%81%90Queue)

---

## #4-1

#### circular queue

크기가 N 인 queue 에서 모든 원소를 다 채우면 rear 는 N-1 을 가리킨다. 이 때, pop 으로 제일 처음 원소를 제거하면 queue 에 남은 공간 1개가 생긴다. 하지만 rear 는 마지막을 가리키고 있기 때문에 더이상 원소를 추가할 수 없다. 이 문제를 해결하기 위해 원형 형태의 `circular queue` 를 사용한다.

<div align='center'>
    <img src='../images/heath/circular_queue.png' height='150px '/>
</div>
<br/>

queue 와 같이 FIFO 구조이다.   

처음에는 front 와 rear 가 같은 메모리를 가리킨다.   
데이터를 입력하기 위해 rear 는 메모리가 꽉찼는지 검사한다. 꽉찬 경우는 rear 다음 번의 메모리가 front 를 가리키는 경우 (rear + 1 == front) 인데, 꽉차지 않았다면 데이터를 입력하고 rear 는 다음 메모리로 이동한다.  
데이터를 반환하기 위해 front 는 메모리가 비었는지 검사한다. 빈 경우에는 현재 front 위치와 rear 위치가 같은 경우 (rear == front) 인데, 비지 않았다면 데이터를 반환하고 front 는 다음 메모리로 이동한다.

#### References
- [[자료구조] 큐(QUEUE)와 원형큐(CIRCULAR QUEUE) 개념과 구현 - reakwon](https://reakwon.tistory.com/30)

---

## #5

#### graph

그래프는 정점과 간선으로 이루어진 자료구조이다. 정점 간의 연결관계는 간선으로 나타낸다.

##### 그래프의 종류

<img src="/images/sally/2021-07-01-13-15-10.png" width="50%">  

간선이 담고있는 정보와 연결 상태에 따라 그래프의 종류가 나뉜다. 두 정점을 연결하는 간선에 방향이 없다면 `무방향 그래프`, 두 정점을 연결하는 간선에 방향이 존재하면 `방향 그래프`라고 부른다. 방향 그래프는 간선의 방향으로만 이동할 수 있다. 두 정점을 이동할 때 비용이 발생하면 `가중치 그래프`로 나타낼 수 있다. 모든 정점이 간선으로 연결된 경우, `완전 그래프`라고 부른다.

##### 그래프 구현 방식

<img src="/images/sally/2021-07-01-12-54-57.png" width="60%">

- 인접행렬 방식
  - 노드를 인덱스로 삼는 2차원 배열을 만든다.
  - 각 노드가 간선으로 연결되어있으면 배열에 1을 넣어주고, 연결되지 않았다면 0을 넣어준다.
  - 두 노드의 연결관계를 조회할 때, O(1) 시간이 걸린다.
  - 그러나 모든 정점에 대해, 간선 정보를 입력해야하므로 초기화에 <!-- $O(N^2)$ --> <img style="transform: translateY(0.1em); background: white;" src="https://render.githubusercontent.com/render/math?math=O(N%5E2)"> 시간이 소요된다.
 - 노드의 수가 많고, 간선의 수가 적은 그래프의 경우에, 공간을 낭비하게 된다.

<img src="/images/sally/2021-07-01-12-55-08.png" width="70%">  

- 인접리스트 방식
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

## #6

#### tree

#### References

---

## #6-1

#### binary tree

#### References

---

## #6-2

#### full binary tree

#### References

---

## #6-3

#### complete binary tree

#### References

---

## #6-4

#### bst(binary search tree)

#### References

---

## #7

#### heap(binary heap)

#### References

---

## #7-1

#### min heap

#### References

---

## #7-2

#### max heap

#### References

---

## #8

#### red-black tree

#### References

---

## #9

#### b+ tree

#### References

---
