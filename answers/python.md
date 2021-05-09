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

#### References

---

## #20

#### How does break, continue and pass work?

#### References

---

## #21

#### What does `[::-1]` do?

#### References

---

## #22

#### How can you randomize the items of a list in place in Python?

#### References

---

## #23

#### What’s the difference between iterator and iterable?

#### References

---

## #24

#### How can you generate random numbers in Python?

#### References

---

## #25

#### What is the difference between range & xrange?

#### References

---

## #26

#### How do you write comments in python?

#### References

---

## #27

#### What is pickling and unpickling?

#### References

---

## #28

#### What are the generators in python?

#### References

---

## #29

#### How will you capitalize the first letter of string?

#### References

---

## #30

#### How will you convert a string to all lowercase?

#### References

---

## #31

#### How to comment multiple lines in python?

#### References

---

## #32

#### What are docstrings in Python?

#### References

---

## #33

#### What is the purpose of is, not and in operators?

#### References

---

## #34

#### What is the usage of help() and dir() function in Python?

#### References

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

ternary operators(삼항 연산자)는 조건문을 표시하는 데 사용되는 연산자이며 아래의 형태로 표현된다.

```python
[true_value] if [condition] else [false_value]
```

> **Example_1**
```python
a = 123
print("a is 123" if a==123 else "a is not 123")
```
> **Output**
```
a is 123
```
<br>

> **Example_2**
```python
a = 456
print("a is 123" if a==123 else "a is not 123")
```
> **Output**
```
a is not 123
```

#### References

- [[Python] 삼항 연산자(Ternary Operator) - 똑똑이](https://m.blog.naver.com/wideeyed/221858874414)

---

## #38

#### What does this mean: `*args`, `**kwargs`? And why would we use it?

`*args`는 함수에 전달되는 argument의 수를 알 수 없거나, list나 tuple의 argument들을 함수에 전달하고자 할 때 사용한다.

> **Example_1**
```python
def name(*args):
    print(args)

name("샐리", "펭귄", "히스", "원딜")
```
> **Output**
```
('샐리', '펭귄', '히스', '원딜')
```
<br>

`**kwargs`는 함수에 전달되는 keyword argument의 수를 모르거나, dictionary의 keyword argument들을 함수에 전달하고자 할 때 사용한다.

> **Example_2**
```python
def name(**kwargs):
    print(kwargs)

name(sally="샐리", penguin="펭귄", heath="히스", adc="원딜")
```
> **Output**
```
{'sally': '샐리', 'penguin': '펭귄', 'heath': '히스', 'adc': '원딜'}
```

#### References

- [[Python] *args와 **kwargs - Jun94](https://velog.io/@hj8853/Python-args%EC%99%80-kwargs)

---

## #39

#### What does `len()` do?

`len()` 함수는 object의 길이(item의 수)를 return 한다.

argument로는 sequence(string, bytes, tuple, list, range, ...), collection(dictionary, set, frozenset, ...)을 받는다.

> **Example_1**
```python
stg = "ai-tech-interview"
len(stg)
```
> **Output**
```
17
```
<br>

> **Example_2**
```python
ex_list = ["ai", "tech", "interview"]
len(ex_list)
```
> **Output**
```
3
```

#### References

- [Built-in Functions - Python documentation](https://docs.python.org/3/library/functions.html#len)

---

## #40

#### Explain split(), sub(), subn() methods of “re” module in Python.

문자열 수정을 위해 Python의 "re" 모듈은 3 가지 메서드를 제공한다.

- `split(pattern, string[, maxplit=0])`: pattern을 구분자로 string을 분리하여 list로 반환
- `sub(pattern, repl, string[, count=0])`: string에서 pattern과 일치하는 부분에 대하여 repl로 교체하여 결과 문자열을 반환
- `subn(pattern, repl, string[, count=0])`: sub와 동일하나, 결과로(결과문자열, 매칭횟수)를 튜플로 반환

#### References

- [파이썬 – 정규식표현식(Regular Expression) 모듈 - devanix](https://devanix.tistory.com/296)

---

## #41

#### What are negative indexes and why are they used?

**인덱스**
- 시퀀스 객체에 \[](대괄호)를 붙여 사용
- 시퀀스 객체의 인덱스는 항상 0부터 시작
- 시퀀스 객체(list, tuple, range, 문자열)에 사용가능
- 시퀀스객체[인덱스]

**음수 인덱스**
- 인덱스를 음수로 지정하면 뒤에서부터 요소에 접근하게 된다.
    - -1은 뒤에서 첫 번째, -5는 뒤에서 다섯 번째 요소를 뜻한다.
- 시퀀스 객체(list, tuple, range, 문자열)에 사용가능

#### References

- [Python | 인덱스(index) - 황복실](https://velog.io/@sz3728/Python-index)

---

## #42

#### What are Python packages?

**모듈**

모듈은 파이썬 코드를 논리적으로 묶어서 관리하고 사용할 수 있도록 하는 것으로, 보통 하나의 파이썬 `.py` 파일이 하나의 모듈이 된다. 모듈 안에는 함수, 클래스, 혹은 변수들이 정의될 수 있으며, 실행 코드를 포함할 수도 있다.
<br><br>

**패키지**

패키지는 특정 기능과 관련된 여러 모듈을 묶은 것으로 패키지는 모듈에 namespace를 제공한다. 패키지는 하나의 디렉토리에 놓여진 모듈들의 집합을 가리키는데, 그 디렉토리에는 일반적으로 `__init__.py` 라는 패키지 초기화 파일이 존재한다.

패키지는 모듈들의 컨테이너로서 패키지 안에는 또다른 서브 패키지를 포함할 수도 있다. 파일시스템으로 비유하면 패키지는 일반적으로 디렉토리에 해당하고, 모듈은 디렉토리 안의 파일에 해당한다.
<br><br>

<div align='center'>
    <img src='../images/adc/python/42_package.png' height='300'/>
</div>

#### References

- [파이썬 패키지와 모듈 알아보기 - 승톨](https://velog.io/@seanlion/pythonmodule)
- [패키지 - 예제로 배우는 파이썬 프로그래밍](http://pythonstudy.xyz/python/article/18-%ED%8C%A8%ED%82%A4%EC%A7%80)

---

## #43

#### How can files be deleted in Python?

os 모듈을 import 한 후 `os.remove()` 함수를 사용하여 파일을 삭제할수있다.

> **Example**
```python
import os
os.remove("ai-tech-interview.txt")
```
<br>

> 자세한 내용은 [os.remove - Python documentation](https://docs.python.org/3/library/os.html#os.remove) 참고

---

## #44

#### What are the built-in types of python?

Python의 Built-in type은 아래와 같다.
- Integer
- Floating-point
- Complex number
- String
- Boolean
- Built-in function

> 자세한 내용은 [Built-in Types - Python documentation](https://docs.python.org/3/library/stdtypes.html) 참고

---

## #45

#### What advantages do NumPy arrays offer over (nested) Python lists?

파이썬 리스트 대신 넘파이 리스트를 쓸 때의 이점

Ans: 

Python’s lists are efficient general-purpose containers. They support (fairly) efficient insertion, deletion, appending, and concatenation, and Python’s list comprehensions make them easy to construct and manipulate.
They have certain limitations: they don’t support “vectorized” operations like elementwise addition and multiplication, and the fact that they can contain objects of differing types mean that Python must store type information for every element, and must execute type dispatching code when operating on each element.
NumPy is not just more efficient; it is also more convenient. You get a lot of vector and matrix operations for free, which sometimes allow one to avoid unnecessary work. And they are also efficiently implemented.
NumPy array is faster and You get a lot built in with NumPy, FFTs, convolutions, fast searching, basic statistics, linear algebra, histograms, etc. 

list는 효율적인 범용 컨테이너입니다. 그들은 (공정하게) 효율적인 삽입, 삭제, 추가 및 연결을 지원하며 list comprehenshion을 통해 쉽게 구성하고 조작 할 수 있습니다.
특정 제한이 있습니다. 요소 별 덧셈 및 곱셈과 같은 "벡터화 된"연산을 지원하지 않으며, 유형이 다른 객체를 포함 할 수 있다는 사실은 Python이 모든 요소에 대한 유형 정보를 저장해야하며 작동 할 때 유형 디스패치 코드를 각 요소에 실행해야 함을 의미합니다.

NumPy는 더 효율적일뿐만 아니라; 또한 더 편리합니다. 많은 벡터 및 행렬 연산을 무료로 얻을 수 있으며 때로는 불필요한 작업을 피할 수 있습니다. 또한 효율적으로 구현됩니다.
NumPy 배열은 더 빠르며 NumPy, FFT, 컨볼 루션, 빠른 검색, 기본 통계, 선형 대수, 히스토그램 등이 많이 내장되어 있습니다.

#### References

---

## #46

#### How to add values to a python list?

`append()`, `extend()`, `insert()` 함수를 사용하여 list에 value를 추가할 수 있다.

**append()**

`list.append(x)` 형태로 사용한다. 괄호 안에 값을 입력하면 새로운 요소를 list 맨 끝에 추가한다. 요소를 추가할 때는 객체로 추가하게 되는데, 입력한 값이 리스트와 같은 반복 가능한 iterable 자료형이더라도 객체로 저장한다.

> **Example**
```python
nums = [1, 2, 3]
nums.append(4)
print(nums)

nums.append([5, 6])
print(nums)
```
> **Output**
```
[1, 2, 3, 4]
[1, 2, 3, 4, [5, 6]]
```
<br>

**extend**

`list.extend(iterable)` 형태로 사용한다. 입력한 iterable 자료형의 항목 각각을 list의 끝에 하나씩 추가한다. append와 동일하게 요소를 list의 끝에 추가하지만 append와 다른 점은 괄호 안에는 iterable 자료형만 올 수 있다는 것이다. iterable 자료형이 아닌 경우 TypeError가 발생한다.

> **Example**
```python
nums = [1, 2, 3]
nums.extend([4])
print(nums)

nums.extend([5, 6])
print(nums)
```
> **Output**
```
[1, 2, 3, 4]
[1, 2, 3, 4, 5, 6]
```
<br>

**insert()**

`list.insert(i, x)` 형태로 사용한다. list의 원하는 위치 i 앞에 추가할 값 x를 삽입할 수 있다. i는 위치를 나타내는 인덱스를 숫자를 입력한다. 음수를 입력하면 배열의 끝을 기준으로 처리된다. 추가할 값 x는 객체로 추가되며 iterable 자료형이더라도 객체로 저장된다.

> **Example**
```python
nums = [1, 2, 3]
nums.insert(0, 10)
print(nums)

nums.insert(-1, 99)
print(nums)

nums.insert(len(nums), [20, 30])
print(nums)
```
> **Output**
```
[10, 1, 2, 3]
[10, 1, 2, 99, 3]
[10, 1, 2, 99, 3, [20, 30]]
```

#### References

- [파이썬 append( ), extend( ), insert( ) 함수 차이 / 요소추가함수 비교 (Python) - 영지공지](https://ooyoung.tistory.com/117)

---

## #47

#### How to remove values to a python list?

`remove()`, `pop()` 함수를 사용하여 list에 value를 삭제할 수 있다.

**remove()**

remove()는 지우고자 하는 인덱스가 아닌, 값을 입력하는 방식이다. 만약 지우고자 하는 값이 리스트 내에 2개 이상이 있다면 순서상 가장 앞에 있는 값을 지우게 된다. 값을 삭제할 때 삭제된 값을 반환하지 않는다.

**pop()**

pop()은 리스트에서 지우고자 하는 값의 인덱스를 받아서 지우는 방식이다. 값을 삭제할 때 삭제된 값을 반환한다. 인덱스를 지정하지 않으면 리스트의 마지막 요소가 삭제되며 반환된다.

---

## #48

#### Does Python have OOps concepts?

Python은 객체 지향 프로그래밍 언어이다. Python의 주요 OOP 개념에는 Class, Object, Method, Inheritance(상속), Polymorphism(다형성), Data Abstraction(데이터 추상화), Encapsulation(캡슐화)을 포함한다.

#### References

- [Object Oriented Programming Python: All you need to know - Harshit kant](https://www.edureka.co/blog/object-oriented-programming-python/)

---

## #49

#### What is the difference between deep and shallow copy?

**Shallow copy**
- Shallow copy는 새로운 객체(변수)를 만든 후에 원본에 접근할 수 있는 참조(reference)를 입력한다.
    - 이런 경우 서로 다른 변수명이지만 본질적으로 서로 같은 대상을 의미하므로 하나의 변수 역시 수정이 된다.
- 가변형(mutable) 자료형에 대해서 적용이 가능하다.
    - 가변형(mutable) 자료형은 같은 주소에서 값(value)이 변경 가능하기 때문에 얕은 복사가 가능하다.
    - 불변형(immutable) 자료형은 본질적으로 변경이 불가능하므로 재배정을 통해 변수를 바꾼다. 따라서 재배정이 이루어지므로 객체가 서로 달라진다.

**Deep copy**
- Deep copy는 새로운 객체(변수)를 만든 뒤에 원본의 복사본을 변수에 입력한다.
    - 서로 값만 같을 뿐 본질적으로 서로 다르기 때문에 한 변수가 수정될 시 다른 변수가 수정되지 않는다.

#### References

- [[Python]Shallow copy & Deep copy - 박현희](https://velog.io/@hyoniii_log/PythonShallow-copy-Deep-copy/)

---

## #50

#### How is Multithreading achieved in Python?

파이썬에는 Multithreading 패키지가 있지만, 일반적으로 코드 속도를 높이기 위해 Multithread 패키지를 사용하는 것은 좋지 않다.

파이썬에는 GIL(Global Interpreter Lock)이라는 구조가 있다. GIL은 한 번에 하나의 스레드만 실행할 수 있도록 한다. 스레드는 GIL을 획득하고 약간의 작업을 수행 한 다음 GIL을 다음 스레드로 전달한다. 이 작업은 매우 빠르게 수행되므로 사람의 눈에는 스레드가 병렬로 실행되는 것처럼 보일 수 있지만 실제로는 동일한 CPU 코어를 사용하여 번갈아 가며 수행한다.

---

## #51

#### What is the process of compilation and linking in python?

컴파일과 연결을 통해 새로운 확장을 오류없이 적절하게 컴파일 할 수 있으며 컴파일된 절차를 통과해야만 연결을 수행할 수 있다. dynamic loading을 사용하는 경우 시스템과 함께 제공되는 스타일에 따라 다르다. 파이썬 인터프리터는 configuration setup file의 dynamic loading을 제공하는 데 사용할 수 있으며 인터프리터를 다시 빌드한다.

이에 필요한 단계는 아래와 같다.

1. 시스템의 컴파일러가 지원하는 언어로 파일을 만든다.
    - ex. file.c, file.cpp
2. 이 파일을 사용되고있는 배포판의 모듈/디렉토리에 저장한다.
3. 모듈/디렉토리에 있는 Setup.local 파일에 행을 추가한다.
4. spam file.o를 사용하여 파일을 실행한다.
5. 이 작업을 성공적으로 실행 한 후 최상위 디렉토리에서 make 명령을 사용하여 인터프리터를 다시 빌드한다.
6. 파일이 변경되면 `make Makefile` 명령을 사용하여 rebuildMakefile을 실행한다.

---

## #52

#### What are Python libraries? Name a few of them.

파이썬 라이브러리는 패키지의 모음이다. 주로 사용되는 파이썬 라이브러리로는 [`Numpy`](https://numpy.org/), [`Pandas`](https://pandas.pydata.org/), [`Matplotlib`](https://matplotlib.org/), [`Scikit-learn`](https://scikit-learn.org/stable/) 등이 있다.

---

## #53

#### What is split used for?

`split()`은 특정 문자를 기준으로 문자열을 분리할 때 사용한다.

```python
str.split(sep=None, maxsplit=-1)
```

sep을 구분자로 사용하여 문자열에 있는 단어 list를 반환한다.

sep이 지정되면 구분자를 기준으로 문자열을 분리하고, sep이 지정되지 않았거나 None인 경우에는 whitespace를 기준으로 문자열을 분리한다.

maxsplit이 지정되면 그 수만큼의 분할이 수행되고, maxsplit이 지정되지 않았거나 -1인 경우에는 가능한 모든 분할이 수행된다.

> **Example**
```python
a = "ai tech interview"
print(a.split())
a = "ai                    tech          interview"
print(a.split())
a = "ai-tech-interview"
print(a.split("-"))
a = "ai-tech-interview"
print(a.split("-", 1))
```
> **Output**
```
['ai', 'tech', 'interview']
['ai', 'tech', 'interview']
['ai', 'tech', 'interview']
['ai', 'tech-interview']
```

#### References

- [str.split - Python documentation](https://docs.python.org/3/library/stdtypes.html#str.split)

---

## #54

#### How to import modules in python?

`import` 키워드를 사용하여 모듈을 가져올 수 있다. 세 가지 방법으로 모듈을 가져올 수 있다.

> **Example**
```python
import numpy        # importing using the original module name
import numpy as np  # importing using an alias name
from numpy import * # imports everything present in the array module
```
<br>

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
