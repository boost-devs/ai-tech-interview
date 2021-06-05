<div align='center'>
  <h1>🖥️ Operating System 🖥️</h1>
</div>

> 질문 중 일부는 <strong>[WeareSoft님의 tech-interview](https://github.com/WeareSoft/tech-interview)</strong>를 참고하였으며, 질문에 대한 답변은 직접 작성하였습니다.

---

## Table of Contents

- [프로세스와 스레드의 차이(Process vs Thread)를 알려주세요.](#1)
- [멀티 프로세스 대신 멀티 스레드를 사용하는 이유를 설명해주세요.](#2)
- [캐시의 지역성에 대해 설명해주세요.](#3)
- [Thread-safe에 대해 설명해주세요. (hint: critical section)](#4)
- [뮤텍스와 세마포어의 차이를 설명해주세요.](#5)
- [스케줄러가 무엇이고, 단기/중기/장기로 나누는 기준에 대해 설명해주세요.](#6)
- [CPU 스케줄러인 FCFS, SJF, SRTF, Priority Scheduling, RR에 대해 간략히 설명해주세요.](#7)
- [동기와 비동기의 차이를 설명해주세요.](#8)
- [메모리 관리 전략에는 무엇이 있는지 간략히 설명해주세요.](#9)
- [가상 메모리에 대해 설명해주세요.](#10)
- [교착상태(데드락, Deadlock)의 개념과 조건을 설명해주세요.](#11)
- [사용자 수준 스레드와 커널 수준 스레드의 차이를 설명해주세요.](#12)
- [외부 단편화와 내부 단편화에 대해 설명해주세요.](#13)
- [Context Switching이 무엇인지 설명하고 과정을 나열해주세요.](#14)
- [Swapping에 대해 설명해주세요.](#15)

---

## #1

#### 프로세스와 스레드의 차이(Process vs Thread)를 알려주세요.

#### References

---

## #2

#### 멀티 프로세스 대신 멀티 스레드를 사용하는 이유를 설명해주세요.

#### References

---

## #3

#### 캐시의 지역성에 대해 설명해주세요.

#### References

---

## #4

#### Thread-safe에 대해 설명해주세요. (hint: critical section)

#### References

---

## #5

#### 뮤텍스와 세마포어의 차이를 설명해주세요.

#### References

---

## #6

#### 스케줄러가 무엇이고, 단기/중기/장기로 나누는 기준에 대해 설명해주세요.

#### References

---

## #7

#### CPU 스케줄러인 FCFS, SJF, SRTF, Priority Scheduling, RR에 대해 간략히 설명해주세요.

#### References

---

## #8

#### 동기와 비동기의 차이를 설명해주세요.
**동기**는 A, B, C 라는 작업이 **어떤 순서로 끝날지 보장되는 구조**를 말한다. A, B, C 작업이 동시에 시작됐는지 순차적으로 시작됐는지는 중요하지 않다. 작업의 순서를 보장하기 위해 이전 작업이 끝날 때까지 기다리는 방법이 있다. 동기는 파이프라인 프로세스를 지킬 때 용이하다.

**비동기**는 A, B, C **작업이 끝나는 순서를 보장하지 않는 구조**를 말한다. 비동기가 유용한 경우는 네트워크를 생각해볼 수 있다. 사용자마다 환경이 달라 요청에 따른 응답의 시간이 다를 때, 비동기적으로 순서를 보장하지 않고 빠른 순서대로 사용자에게 응답을 할 수 있다.

#### References
- [동기(Synchronous) 작업과 비동기(Asynchronous) 작업, 그리고 블락(Blocking) 과 넌블락(Non-Blocking) 의 개념 - Jins' Dev Inside](https://jins-dev.tistory.com/entry/%EB%8F%99%EA%B8%B0Synchronous-%EC%9E%91%EC%97%85%EA%B3%BC-%EB%B9%84%EB%8F%99%EA%B8%B0Asynchronous-%EC%9E%91%EC%97%85-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EB%B8%94%EB%9D%BDBlocking-%EA%B3%BC-%EB%84%8C%EB%B8%94%EB%9D%BDNonBlocking-%EC%9D%98-%EA%B0%9C%EB%85%90)

---

## #9

#### 메모리 관리 전략에는 무엇이 있는지 간략히 설명해주세요.

#### References

---

## #10

#### 가상 메모리에 대해 설명해주세요.

#### References

---

## #11

#### 교착상태(데드락, Deadlock)의 개념과 조건을 설명해주세요.

#### References

---

## #12

#### 사용자 수준 스레드와 커널 수준 스레드의 차이를 설명해주세요.

#### References

---

## #13

#### 외부 단편화와 내부 단편화에 대해 설명해주세요.

#### References

---

## #14

#### Context Switching이 무엇인지 설명하고 과정을 나열해주세요.

#### References

---

## #15

#### Swapping에 대해 설명해주세요.

#### References

---
