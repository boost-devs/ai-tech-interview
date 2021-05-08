## 📝 Table of Contents

- [What is the difference between list and tuples in Python?](#1)
- [What are the key features of Python?](#2)
- [What type of language is python? Programming or scripting?](#3)
- [Python an interpreted language. Explain.](#4)
- [What is pep 8?](#5)
- [How is memory managed in Python?](#6)
- [What is namespace in Python?](#7)
- [What is PYTHONPATH?](#8)
- [What are python modules? Name some commonly used built-in modules in Python?](#9)
- [What are local variables and global variables in Python?](#10)
- [Is python case sensitive?](#11)
- [What is type conversion in Python?](#12)
- [How to install Python on Windows and set path variable?](#13)
- [Is indentation required in python?](#14)
- [What is the difference between Python Arrays and lists?](#15)
- [What are functions in Python?](#16)
- [What is `__init__`?](#17)
- [What is a lambda function?](#18)
- [What is self in Python?](#19)
- [How does break, continue and pass work?](#20)
- [What does `[::-1]` do?](#21)
- [How can you randomize the items of a list in place in Python?](#22)
- [What’s the difference between iterator and iterable?](#23)
- [How can you generate random numbers in Python?](#24)
- [What is the difference between range & xrange?](#25)
- [How do you write comments in python?](#26)
- [What is pickling and unpickling?](#27)
- [What are the generators in python?](#28)
- [How will you capitalize the first letter of string?](#29)
- [How will you convert a string to all lowercase?](#30)
- [How to comment multiple lines in python?](#31)
- [What are docstrings in Python?](#32)
- [What is the purpose of is, not and in operators?](#33)
- [What is the usage of help() and dir() function in Python?](#34)
- [Whenever Python exits, why isn’t all the memory de-allocated?](#35)
- [What is a dictionary in Python?](#36)
- [How can the ternary operators be used in python?](#37)
- [What does this mean: `*args`, `**kwargs`? And why would we use it?](#38)
- [What does len() do?](#39)
- [Explain split(), sub(), subn() methods of “re” module in Python.](#40)
- [What are negative indexes and why are they used?](#41)
- [What are Python packages?](#42)
- [How can files be deleted in Python?](#43)
- [What are the built-in types of python?](#44)
- [What advantages do NumPy arrays offer over (nested) Python lists?](#45)
- [How to add values to a python array?](#46)
- [How to remove values to a python array?](#47)
- [Does Python have OOps concepts?](#48)
- [What is the difference between deep and shallow copy?](#49)
- [How is Multithreading achieved in Python?](#50)
- [What is the process of compilation and linking in python?](#51)
- [What are Python libraries? Name a few of them.](#52)
- [What is split used for?](#53)
- [How to import modules in python?](#54)
- [Explain Inheritance in Python with an example.](#55)
- [How are classes created in Python?](#56)
- [What is monkey patching in Python?](#57)
- [Does python support multiple inheritance?](#58)
- [What is Polymorphism in Python?](#59)
- [Define encapsulation in Python?](#60)
- [How do you do data abstraction in Python?](#61)
- [Does python make use of access specifiers?](#62)
- [How to create an empty class in Python?](#63)
- [What does an object() do?](#64)
- [What is map function in Python?](#65)
- [Is python numpy better than lists?](#66)
- [What is GIL in Python language?](#67)
- [What makes the CPython different from Python?](#68)
- [What are Decorators in Python?](#69)
- [What is object interning?](#70)
- [What is @classmethod, @staticmethod, @property?](#71)

---

## #1

#### What is the difference between list and tuples in Python?

#### References

---

## #2

#### What are the key features of Python?

#### References

---

## #3

#### What type of language is python? Programming or scripting?

#### References

---

## #4

#### Python an interpreted language. Explain.

#### References

---

## #5

#### What is pep 8?

#### References

---

## #6

#### How is memory managed in Python?

#### References

---

## #7

#### What is namespace in Python?

#### References

---

## #8

#### What is PYTHONPATH?

#### References

---

## #9

#### What are python modules? Name some commonly used built-in modules in Python?

#### References

---

## #10

#### What are local variables and global variables in Python?

#### References

---

## #11

#### Is python case sensitive?

#### References

---

## #12

#### What is type conversion in Python?

#### References

---

## #13

#### How to install Python on Windows and set path variable?

#### References

---

## #14

#### Is indentation required in python?

#### References

---

## #15

#### What is the difference between Python Arrays and lists?

#### References

---

## #16

#### What are functions in Python?

#### References

---

## #17

#### What is `__init__`?

#### References

---

## #18

#### What is a lambda function?

#### References

---

## #19

#### What is self in Python?

```python
class MyClass:
    def method(self):
        return 'instance method', self

obj = MyClass
print(obj.method())

# >> ('instance method', <__main__.MyClass object at 0x7f10aa8e68b0>)
```

우선 `self`가 어디에서 쓰이는지 알아야 한다. `self`는 인스턴스 메서드(instance method)의 첫 번째 인자이다. 메서드가 호출될 때, 파이썬은 `self`에 인스턴스를 넣고 이 인스턴스를 참조하여 인스턴스 메서드를 실행할 수 있게 된다.

#### References

- [self 이해하기 - 파이썬으로 배우는 알고리즘 트레이딩](https://wikidocs.net/1742)
- [Python's Instance, Class, and Static Methods Demystified - Real Python](https://realpython.com/instance-class-and-static-methods-demystified/)
- [Why must ‘self’ be used explicitly in method definitions and calls? - Python Documentation](https://docs.python.org/3/faq/design.html?highlight=self#why-must-self-be-used-explicitly-in-method-definitions-and-calls)

---

## #20

#### How does break, continue and pass work?

`break`는 가장 가까운 for문이나 while문의 루프에서 빠져나가도록 한다.

```python
for i in range(10):
  if i == 5:
    break
  print(i, end=' ')

# >> 0 1 2 3 4
```

`continue`는 이번 이터레이션(iteration)을 건너뛰고 다음 이터레이션을 이어나가도록 한다.

```python
for i in range(10):
  if i == 5:
    continue
  print(i, end=' ')

# >> 0 1 2 3 4 6 7 8 9
```

`pass`는 문법적으로 필요하지만, 아무 것도 하지 않게 하고 싶을 때 사용한다. 주로 함수나 클래스의 구조부터 세우고 나중에 구현을 하고 싶을 때 사용한다.

```python
class MyClass:
    def not_implemented_method(self):
        pass
```

#### References

- [루프의 break 와 continue 문, 그리고 else 절 - Python Documentation](https://docs.python.org/ko/3/tutorial/controlflow.html?highlight=break)
- [pass 문 - Python Documentation](https://docs.python.org/ko/3/tutorial/controlflow.html?highlight=break#pass-statements)

---

## #21

#### What does `[::-1]` do?

파이썬 시퀀스 자료형은 값이 연속적으로 이어진 자료형으로, **리스트, 튜플, range, 문자열**이 있다. 시퀀스 자료형은 시퀀스 객체의 일부를 잘라낼 수 있는 **슬라이싱(slicing)**이라는 기능을 쓸 수 있다. 슬라이싱은 `seq[start:end:step]`처럼 쓸 수 있으며, `start`는 시작 인덱스, `end`는 끝 인덱스(범위에 포함하지는 않음), `step`은 인덱스 증감폭을 말한다. `step`이 양수이면 증가하고, 음수이면 감소한다.

다시 돌아와 `seq[::-1]`은 `start`와 `end`는 시작 인덱스와 끝 인덱스를 생략하였는데, 이럴 경우 전체 시퀀스를 가져오며, 증감폭이 -1이므로 `end-1`부터 시작해 `start`순으로 요소를 가져온다. 즉, `seq[::-1]`은 시퀀스를 역전(reverse)시킨다.

#### References

- [시퀀스 자료형 활용하기 - 파이썬 코딩 도장](https://dojang.io/mod/page/view.php?id=2205)
- [슬라이스 사용하기 - 파이썬 코딩 도장](https://dojang.io/mod/page/view.php?id=2208)

---

## #22

#### How can you randomize the items of a list in place in Python?

**random 모듈의 `shuffle` 메서드**를 사용하면 구현할 수 있다. `random.shuffle`은 시퀀스 객체의 요소를 임의로 섞어서 해당 시퀀스를 반환한다.

```python
import random

random.seed(2021)       # 시드 고정
lst = list(range(10))
print(lst)              # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(lst)
print(lst)              # [2, 7, 9, 3, 0, 5, 1, 4, 8, 6]
```

#### References

- [Shuffle a list, string, tuple in Python (random.shuffle, sample) - note.nkmk.me](https://note.nkmk.me/en/python-random-shuffle/)
- [random - Python Documentation](https://docs.python.org/ko/3/library/random.html)

---

## #23

#### What’s the difference between iterator and iterable?

```python
lst = [1, 2]            # iterable 객체 : 리스트
lst_iter = iter(lst)    # iterator 객체

print(next(lst_iter))   # 1
print(next(lst_iter))   # 2
print(next(lst_iter))   # StopIteration 예외 발생
```

iterable 객체는 `iter` 함수에 인자로 전달 가능한, 반복 가능한 객체를 말한다. 예를 들면, 리스트(list), 딕셔너리(dictionary), 집합(set), 문자열(string) 등이 있다.

iterable 객체를 `iter` 함수의 인자로 넣으면 iterable 객체를 순회할 수 있는 객체를 반환하는데, 이것이 iterator 객체이다. iterator 객체를 `next` 함수의 인자로 주면 iterable 객체의 요소의 값을 차례대로 반환한다. 만약 iterable 객체를 모두 순회했다면, _StopIteration_ 예외를 발생시킨다. 만약 다시 순회를 하고 싶다면 `iter` 함수로 새로운 iterator 객체를 생성해주면 된다.

#### References

- [🐍 제너레이터(Generator) - 코딩하는펭귄의 저장소](https://cooding-penguin.netlify.app/python/generator/)
- [Iterable 과 Iterator - 파이썬 - 기본을 갈고 닦자!](https://wikidocs.net/16068)

---

## #24

#### How can you generate random numbers in Python?

random 모듈로 간단히 생성할 수 있다. 편의를 위해 다음과 같이 random 모듈을 import하고 시드값을 2021로 고정하자.

```python
import random
random.seed(2021)
```

- 0과 1사이의 임의의 수를 생성하고 싶은 경우

```python
print(random.random())          # 0.8363375023320742
```

- 특정 범위 내의 임의의 정수를 생성하고 싶은 경우

```python
print(random.randint(0, 10))    # 10
```

- 특정 범위 내의 n개의 정수를 생성하고 싶은 경우

```python
n = 5
lst = range(1, 101)
print(random.sample(lst, 5))    # [70, 36, 32, 82, 5]
```

#### References

- [Generating random number list in Python - tutorialspoint](https://www.tutorialspoint.com/generating-random-number-list-in-python)

---

## #25

#### What is the difference between range & xrange?

#### References

- [python range() 와 xrange() 차이 - ㅍㅍㅋㄷ](https://bluese05.tistory.com/57)

---

## #26

#### How do you write comments in python?

#### References

- [Documenting Python Code: A Complete Guide - Real Python](https://realpython.com/documenting-python-code/)

---

## #27

#### What is pickling and unpickling?

#### References

- [pickle — 파이썬 객체 직렬화 - Python Documentation](https://docs.python.org/ko/3/library/pickle.html)

---

## #28

#### What are the generators in python?

#### References

- [🐍 제너레이터(Generator) - 코딩하는펭귄의 저장소](https://cooding-penguin.netlify.app/python/generator/)
- [How to Use Generators and yield in Python - Real Python](https://realpython.com/introduction-to-python-generators/)

---

## #29

#### How will you capitalize the first letter of string?

#### References

- [Python String Methods - w3schools](https://www.w3schools.com/python/python_ref_string.asp)

---

## #30

#### How will you convert a string to all lowercase?

#### References

- [Python String Methods - w3schools](https://www.w3schools.com/python/python_ref_string.asp)

---

## #31

#### How to comment multiple lines in python?

#### References

- [Documenting Python Code: A Complete Guide - Real Python](https://realpython.com/documenting-python-code/)

---

## #32

#### What are docstrings in Python?

#### References

- [Documenting Python Code: A Complete Guide - Real Python](https://realpython.com/documenting-python-code/)

---

## #33

#### What is the purpose of is, not and in operators?

#### References

---

## #34

#### What is the usage of help() and dir() function in Python?

#### References

- [내장 함수: help() - Python Documentation](https://docs.python.org/ko/3/library/functions.html#help)
- [내장 함수: dir() - Python Documentation](https://docs.python.org/ko/3/library/functions.html#dir)

---

## #35

#### Whenever Python exits, why isn’t all the memory de-allocated?

#### References

---

## #36

#### What is a dictionary in Python?

#### References

---

## #37

#### How can the ternary operators be used in python?

#### References

---

## #38

#### What does this mean: `*args`, `**kwargs`? And why would we use it?

#### References

---

## #39

#### What does len() do?

#### References

---

## #40

#### Explain split(), sub(), subn() methods of “re” module in Python.

#### References

---

## #41

#### What are negative indexes and why are they used?

#### References

---

## #42

#### What are Python packages?

#### References

---

## #43

#### How can files be deleted in Python?

#### References

---

## #44

#### What are the built-in types of python?

#### References

---

## #45

#### What advantages do NumPy arrays offer over (nested) Python lists?

#### References

---

## #46

#### How to add values to a python array?

#### References

---

## #47

#### How to remove values to a python array?

#### References

---

## #48

#### Does Python have OOps concepts?

#### References

---

## #49

#### What is the difference between deep and shallow copy?

#### References

---

## #50

#### How is Multithreading achieved in Python?

#### References

---

## #51

#### What is the process of compilation and linking in python?

#### References

---

## #52

#### What are Python libraries? Name a few of them.

#### References

---

## #53

#### What is split used for?

#### References

---

## #54

#### How to import modules in python?

#### References

---

## #55

#### Explain Inheritance in Python with an example.

#### References

---

## #56

#### How are classes created in Python?

#### References

---

## #57

#### What is monkey patching in Python?

#### References

---

## #58

#### Does python support multiple inheritance?

#### References

---

## #59

#### What is Polymorphism in Python?

#### References

---

## #60

#### Define encapsulation in Python?

#### References

---

## #61

#### How do you do data abstraction in Python?

#### References

---

## #62

#### Does python make use of access specifiers?

#### References

---

## #63

#### How to create an empty class in Python?

#### References

---

## #64

#### What does an object() do?

#### References

---

## #65

#### What is map function in Python?

#### References

---

## #66

#### Is python numpy better than lists?

#### References

---

## #67

#### What is GIL in Python language?

#### References

---

## #68

#### What makes the CPython different from Python?

#### References

---

## #69

#### What are Decorators in Python?

#### References

---

## #70

#### What is object interning?

#### References

---

## #71

#### What is @classmethod, @staticmethod, @property?

#### References

---
