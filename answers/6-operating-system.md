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

시스템 내에는 여러 개의 프로세스가 존재한다. 이 때 시간(time)과 공간(space) 즉, <u>자원을 할당할 프로세스를 선택</u>해야 하는데, 이 역할을 맡은 것을 `스케줄러`라고 한다.

스케줄러의 목적은 **시스템 성능 향상**이며 대표적인 시스템 성능 지표로 응답시간(response time), 작업 처리량(throughput), 자원 활용도(resource utilization)이 있다. **목적에 따라 다양한 성능 지표를 고려**하여 스케줄러를 선택한다.

스케줄러는 <u>발생하는 빈도와 할당하는 자원</u>에 따라 **장기/중기/단기 스케줄러**로 나눌 수 있다.

`장기 스케줄러(Long-term Scheduler)`는 시스템에 제출할 작업을 결정하는 Job Scheduling(Job → created)에서 사용하며, 시스템 내에 프로세스 수를 조절한다. 이 때 중요한 것은 CPU든 I/O든 모두 써서 효율성을 높이기 위해서 I/O bounded와 compute-bounded 프로세스들을 잘 섞어서 선택해야 한다.

`중기 스케줄러(Mid-term Scheduler)`는 메모리 할당을 결정하는 Memory Allocation(suspended ready → ready)에서 사용한다.

`단기 스케줄러(Short-term Scheduler)`는 프로세서를 할당한 프로세스를 결정하는 Process Scheduling(ready → running)에서 사용하며, 가장 빈번하게 발생하므로 매우 빨라야 한다.

> **응답시간 vs 작업 처리량 vs 자원 활용도**

- `응답시간(response time)`: 작업 요청으로부터 응답을 받을 때까지의 시간
- `작업 처리량(throughput)`: 단위 시간 동안 완료된 작업의 수
- `자원 활용도(resource time)`: 주어진 시간동안 자원이 활용된 시간

> **I/O Bounded 프로세스 vs Compute-bounded 프로세스**

- `I/O Bounded 프로세스`: I/O 대기시간이 긴 프로세스
- `Compute-bounded 프로세스`: CPU 사용시간이 긴 프로세스

> **스케줄링의 단계**

<div align='center'>
<img src="../images/penguin/scheduling-level.png" width="80%">
</div>
<br/>

#### References

- [[OS] Lecture 5. Process Scheduling (1/4) / 운영체제 강의 - HPC Lab. KOREATECH](https://www.youtube.com/watch?v=_gNeoGQx-Tc&list=PLBrGAFAIyf5rby7QylRc6JxU5lzQ9c4tN&index=8&ab_channel=HPCLab.KOREATECHHPCLab.KOREATECH)

---

## #7

#### CPU 스케줄러인 FCFS, SJF, SRTF, Priority Scheduling, RR에 대해 간략히 설명해주세요.

#### References

---

## #8

#### 동기와 비동기의 차이를 설명해주세요.

#### References

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
