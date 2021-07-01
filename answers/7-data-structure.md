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

#### References

---

## #1-1

#### single linked list

#### References

---

## #1-2

#### double linked list

#### References

---

## #1-3

#### circular linked list

#### References

---

## #2

#### hash table

#### References

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

#### References

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
