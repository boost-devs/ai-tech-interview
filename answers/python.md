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

리스트는 muatble(변경 가능), 튜플은 immutable(변경 불가능)이라는 특징을 가지고 있다. 따라서 리스트는 선언 후에도 값에 대한 변경, 삭제가 가능하지만, 튜플은 선언 후에 값을 변경하거나 삭제하는 것이 불가능하다. 또한 리스트는 튜플보다 느리다는 단점을 가지고 있으며, 하나의 튜플/리스트에 다른 타입의 값을 함께 저장할 수 있다는 공통점이 있다. 리스트는 대괄호 `[ ]`를, 튜플은 소괄호 `( )`를 사용해서 나타낸다.

#### References

[[Python] 튜플(tuple), 리스트(list), 셋(set), 딕셔너리(dict) 비교 - specialscene](https://specialscene.tistory.com/142)

---

## #2

#### What are the key features of Python?

파이썬이 주요 특징은 아래와 같다.

- **인터프리터 언어(Interpreter Language)**
  - 파이썬은 인터프리터 언어이므로, 실행하기 전에 컴파일을 할 필요가 없다.
  - 자세한 내용은 [Python an interpreted language. Explain.](#4) 참고
- **동적타이핑(Dynamic Typing)**
  - 파이썬은 실행시간에 자료형을 검사하므로, 선언할 때 변수 유형(ex.int, double, ...)을 명시할 필요가 없다.
  - `typing`이란 프로그램 내에서 변수의 데이터 타입을 정하는 것을 말한다. 데이터 타입 지정(assign)은 정적 또는 동적 타이핑으로 분류되는데, 프로그램 컴파일 시에 변수의 타입을 체크하는 C, C++과 같은 언어는 정적 타입(static typed) 언어라고 하고, 프로그램 실행 시에 타입을 체크하는 python은 동적 타입(dynamic typed) 언어이다.
- **객체 지향 프로그래밍(OOP)**
  - 파이썬은 클래스와 구성 및 상속을 함께 정의할 수 있다는 점에서 객체 지향 프로그래밍에 매우 적합하다.
- **일급객체(First-class citizen)**
  - 파이썬에서 함수와 클래스는 일급 객체이다. 일급객체는 변수나 데이터 구조 안에 담을 수 있고, 매개변수로 전달이 가능하며, 리턴값으로 사용될 수 있다는 특징을 가지고 있다.

> 이 외 특징

- 파이썬은 **들여쓰기(indentation)** 와 간결하고 쉬운 문법을 통해 빠르게 코드를 작성할 수 있다는 장점을 가지고있다.
- 변수, 인수(argument)를 미리 선언하지 않아도 **자동으로 메모리 공간 할당**되어 편리하다.
- 함수(function) 또는 **모듈**(module) 추가가 용이하여 **확장성과 이식성**이 좋다.
- 파이썬은 인터프리터로 동작하는 **스크립트 언어**이므로 다른 컴파일 언어에 비해 다소 느리다.
  - 컴파일러가 코드를 기계어로 번역해서 실행가능 파일을 만드는 것에 비해, 인터프리터는 코드를 한줄씩 실행시간마다 번역해서 실행하기 때문이다.

#### References

- [Python 시작하기 - crystalcube](https://crystalcube.co.kr/44)
- [파이썬 동적 타이핑과 캐스팅 - 스스로 배우는 코딩](https://blog.naver.com/PostView.nhn?blogId=youndok&logNo=222057656966)
- [python 리스트, 튜플, 딕셔너리 비교 - bskyvision](https://bskyvision.com/854)
- [Python 일급객체(FIRST-CLASS CITIZEN)- 홍찬기]](https://hckcksrl.medium.com/python-%EC%9D%BC%EA%B8%89%EA%B0%9D%EC%B2%B4-1735746a8229)
- [인터프리터 언어와 컴파일 언어의 차이 - jhkang-dev](https://jhkang-tech.tistory.com/136)

---

## #3

#### What type of language is python? Programming or scripting?

파이썬은 정확하게는, 스크립트 언어이다. 모든 스크립트 언어는 프로그래밍 언어로 볼 수 있으나, 모든 프로그래밍 언어가 스크립트 언어로 분류되는 것은 아니다. 따라서 파이썬은 스크립트 언어이자, 프로그래밍 언어이다. 그러나 사람들은 일반적인 경우에 파이썬을 프로그래밍 언어의 목적으로 분류하고, 프로그래밍 목적으로 많이 사용한다.

- 스크립팅(scripting/Scripting Language)
  - 스크립트 언어란 컴파일이 필요없이 실행될 수 있는 명령어의 집합이다. 스크립트 언어는 인터프리터를 사용하는데, 인터프리터는 컴파일 과정이 필요하지 않으며, 소스코드로 부터 바로 명령어를 해석할 수 있다.

#### References

- [What Is a Scripting Language? - CAREER KARMA](https://careerkarma.com/blog/what-is-a-scripting-language/)

---

## #4

#### Python an interpreted language. Explain.

인터프리터는 고급 언어로 작성된 원시코드 명령어들을 한번에 한 줄씩 읽어들여서 실행하는 프로그램이다. 인터프리터 언어는 실행시간(runtime) 전에 기계 레벨 코드(machine-level code)를 만드는 컴파일 언어와 다르게 소스코드를 바로 실행하는 언어이며, 파이썬은 인터프리터 언어에 해당한다.

> 인터프리터 언어는 스크립트 언어와 동일한 의미이다.  
> 스크립팅/스크립트 언어에 대한 질문과 답변은 [What type of language is python? Programming or scripting?](#3)을 참고한다.

#### References

- [인터프리터 - 위키백과](https://ko.wikipedia.org/wiki/%EC%9D%B8%ED%84%B0%ED%94%84%EB%A6%AC%ED%84%B0)

---

## #5

#### What is pep 8?

PEP(Python Enhancement Proposal)는 Python 코드를 포맷하는 방법을 지정하는 규칙 집합이다. 다른 사람과 원활하게 협업하려면 공통된 스타일 공유가 필요하며, 일관성 있는 스타일은 나중에 수정하기도 쉽다. PEP8은 파이썬 코드를 어떻게 구성할 지 알려주는 스타일 가이드로서의 역할을 한다.

> PEP8 스타일 가이드 예시

- whitespace
  - 한 줄의 문자 길이가 79자 이하여야 한다.
  - 함수와 클래스는 빈 줄 두개로 구분한다.
- naming
  - 함수, 변수, 속성 : `lowercase_underscore`
  - 보호(protected) 인스턴스 속성 : `_leading_underscore`
  - 비공개(private) 인스턴스 속성 : `__double_leading_undersocre`

#### References

- [파이썬 PEP8 스타일 가이드 - 초보몽키의 개발공부로그](https://wayhome25.github.io/python/2017/05/04/pep8/)

---

## #6

#### How is memory managed in Python?

Python은 모든 것을 객체로 관리한다. 객체가 더이상 필요하지 않으면 파이썬 메모리 관리자가 자동으로 객체에서 메모리를 회수하는 방식을 사용하므로, 파이썬은 **동적 메모리 할당** 방식을 사용한다고 말할 수 있다. **힙(heap)**은 동적할당을 구현하는데 사용된다. 힙을 사용하여 동적으로 메모리를 관리하면, 필요하지 않은 메모리를 비우고 재사용할 수 있다는 장점이 있다. 모든 파이썬 객체 또는 자료구조는 python private heap 공간에서 관리되며, 프로그래머는 이 공간에 접근할 수 없고, 대신 파이썬 인터프리터가 대신해서 관리한다. 파이썬 객체에 대한 힙 공간 할당은 **파이썬 메모리 관리자(Python Memory Manager)** 에 의해 수행된다. 또한, 파이썬은 사용되지 않는 모든 메모리를 재활용하고 힙 공간에서 사용할 수 있도록 하는 **내장 Garbage Collector(GC)** 를 가지고 있으며, Python 메모리 관리자에는 객체별 할당자가있어 int, string 등과 같은 특정 객체에 대해 메모리를 명확하게 할당 할 수 있다.

#### References

- [[메모리 관리] 파이썬(Python)에서 메모리 관리하기 - DEVLOG/개발일기](https://deepwelloper.tistory.com/130)
- [파이썬 런타임과 메모리 관리 - muchogusto](https://velog.io/@muchogusto/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%9F%B0%ED%83%80%EC%9E%84%EA%B3%BC-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EA%B4%80%EB%A6%AC)

---

## #7

#### What is namespace in Python?

namespace는 이름 지정 충돌(naming conflicts)을 피하기 위해 이름이 고유한지 확인하는 데 사용되는 이름 지정 시스템(naming system)이다. 네임스페이스(namespace, 이름공간)란 프로그래밍 언어에서 특정한 객체(Object)를 이름(Name)에 따라 구분할 수 있는 범위를 의미한다. 파이썬 내부의 모든것은 객체로 구성되며 이들 각각은 특정 이름과의 매핑 관계를 갖게 되는데 이 매핑을 포함하고 있는 공간을 네임스페이스라고 한다.

네임스페이스가 필요한 이유는 다음과 같다. 프로그래밍을 수행하다보면 모든 변수 이름과 함수 이름을 정하는 것이 중요한데 이들 모두를 겹치지 않게 정하는 것은 사실상 불가능하다. 따라서 프로그래밍언어에서는 네임스페이스라는 개념을 도입하여, 특정한 하나의 이름이 통용될 수 있는 범위를 제한한다. 즉, **소속된 네임스페이스가 다르다면 같은 이름이 다른 개체를 가리키도록 하는 것이 가능**하다.

> 파이썬 네임스페이스의 특징

- 네임스페이스는 딕셔너리 형태로 구현된다.
- 모든 이름 자체는 문자열로 되어있고 각각은 해당 네임스페이스의 범위에서 실제 객체를 가리킨다.
- 이름과 실제 객체 사이의 매핑은 가변적(Mutable)이므로 런타임동안 새로운 이름이 추가될 수 있다.
- 빌트인 네임스페이스는 함부로 추가하거나 삭제할 수 없다.

> 파이썬 네임스페이스의 3가지 분류

- `빌트인 네임스페이스(build-in namespace)`: 기본 내장 함수 및 기본 예외들의 이름들이 소속된다. 파이썬으로 작성된 모든 코드 범위가 포함된다.
- `전역 네임스페이스(global namespace)`: 모듈별로 존재하며, 모듈 전체에서 통용될 수 있는 이름들이 소속된다.
- `지역 네임스페이스(local namespace)`: 함수 및 메서드 별로 존재하며, 함수 내의 지역 변수들의 이름들이 소속된다.

![namespace_img](/images/sally/2021-05-09-01-33-50.png)

#### References

- [[Python] 네임스페이스 개념 정리 - Hyungcheol Noh's Blog](https://hcnoh.github.io/2019-01-30-python-namespace)

---

## #8

#### What is PYTHONPATH?

모듈을 import할 때 사용되는 환경변수이다. 모듈을 import할 때마다 PYTONPATH를 조회하여 가져온 모듈이 디렉토리에 있는지 확인한다. 인터프리터는 이를 사용하여 로드할 모듈을 결정한다.

PYTHONPATH 환경 변수에 경로를 추가하면, 파이썬은 이 경로들을 `sys.path`에 추가한다. 이를 통해 파이썬 코드 내부에서 뿐만 아니라 파이썬 코드 밖에서도 `sys.path`를 조작할 수 있다. PYTHONPATH에는 `sys.path`에 추가할 여러 경로들이 들어간다. 리눅스에서는 `/foo:/bar`처럼 `:`로 두 경로를 구분하고, 윈도우에서는 `/foo;/bar`처럼 `;`로 두 경로를 구분한다. 이외에도 sys.path에는 파이썬에 포함된 여러 내장 모듈 등을 탐색하기 위한 기본 경로가 들어간다.

> 주의 `sys.path`의 순서

import는 `sys.path` 리스트에 들어있는 경로들을 탐색하며 불러올 파이썬 파일을 찾는다. 리스트에 들어있는 맨 처음 경로부터 탐색을 시작하여, 특정 경로에서 불러올 파일을 찾았다면 남은 경로를 더 찾아보지 않고 탐색을 중지한다.
`sys.path`의 기본값은 아래의 순서대로 추가된다.

- `.py` 파일이 속한 디렉터리의 절대 경로
- PYTHONPATH 환경 변수
- 기타 기본 경로

> 아래의 코드를 통해서 `sys.path`를 직접 확인할 수 있다.

```python
import sys
print(sys.path)
```

#### References

- [sys.path, PYTHONPATH: 파이썬 파일 탐색 경로 - 방성범 (Bang Seongbeom)](https://www.bangseongbeom.com/sys-path-pythonpath.html#fn:ahead)
- [Python sys module, path 정리 - 일류도 삼류에서 부터](https://smartkuma.tistory.com/entry/Python-sys-module-path-%EC%A0%95%EB%A6%AC)

---

## #9

#### What are python modules? Name some commonly used built-in modules in Python?

모듈이란 Python 코드를 포함하는 파일로써, 함수나 변수 또는 클래스를 모아 놓은 파일이다. 모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일이라고도 할 수 있다. 실행 가능한 코드를 포함하는, 파이썬 확장자 `.py`로 만든 파이썬 파일은 모두 모듈이다. 모듈을 사용하면, 다른 코드에 적용하기가 쉬워지므로 이식성이 좋아진다.

- 자주 사용되는 빌트인 모듈(built-in module)의 예시는 다음과 같다.
  - `os`
  - `sys`
  - `math`
  - `random`
  - `data time`
  - `JSON`

#### References

- [05-2 모듈 - 점프 투 파이썬](https://wikidocs.net/29)

---

## #10

#### What are local variables and global variables in Python?

- **전역변수(Global Variance)** : 함수 외부 또는 전역 공간에 선언된 변수를 전역 변수라고 한다. 프로그램의 모든 함수에서 전역변수에 접근할 수 있다.
- **로컬 변수(Local Variance)** : 함수 내부에 선언된 변수를 로컬 변수라고 한다. 전역변수는 전역 공간이 아닌 로컬 공간에 있다.

> 예시

```python
a=2
def add():
    b=3
    c=a+b
    print(c)
add()

# 출력: 5

# local var: a
# global var: b, c
```

- `add()` 함수의 외부에서 `add()` 함수의 로컬 변수에 액세스하려고 하면 오류가 발생한다.

---

## #11

#### Is python case sensitive?

파이썬은 대소문자를 구분하는 언어이다. 예를들어, `a`와 `A`는 다른 변수이다.

---

## #12

#### What is type conversion in Python?

type conversion은 타입 캐스팅(type casting)과 동일한 의미를 가지며, 이는 어떤 데이터 타입을 다른 데이터 타입으로 변환하는 것을 말한다.

> 타입 캐스팅 함수의 종류

- `int()`: 정수형으로 변환한다.
- `float()`: 실수형으로 변환한다.
- `ord()`: 문자형을 정수형으로 변환한다.
- `hex()`: 정수형을 10진수로 변환한다.
- `oct()`: 정수형을 8진수로 변환한다.
- `tuple()`: 튜플형으로 변환한다.
- `set()`: set으로 변환한다.
- `list()`: list로 변환한다.
- `dict()`: (key,value) 순서로 이뤄진 튜플을 딕셔너리형으로 변환한다.
- `str()`: 정수형을 문자형으로 변환한다.
- `complex(real, image)`: 실수를 복소수로 변환한다.

---

## #13

#### How to install Python on Windows and set path variable?

Windows에 Python을 설치하려면 다음 단계를 거쳐야한다.

1. [링크](https://www.python.org/downloads/)에서 python을 설치한다.
2. PC에 다운로드 받은 python을 설치하면서, `Add Python 3.6 to PATH`에 체크하고, 안내에 따라 설치하며 python을 설치한 위치를 저장해둔다.
3. `시스템 > 시스템 정보 > 고급 시스템 설정 > 환경변수`으로 이동하여 시스템 변수를 편집하여 2번에서 저장해둔 python.exe 실행파일이 있는 경로를 추가해주면 된다.

#### References

- [Python / 설치 / 윈도우에 설치하기 - CODING FACTORY](https://www.codingfactory.net/10023)

---

## #14

#### Is indentation required in python?

Python은 Indentation(들여쓰기)이 필요하다. 파이썬은 `{}`을 사용하여 영역을 지정하지 않고, 들여쓰기를 사용하여 코드블록을 지정하기 때문에 파이썬에서 들여쓰기는 문법적인 강제사항이다. `if, for, class, def` 등의 모든 코드는 들여쓰기 블록 내에서 지정된다. 들여쓰기의 방법은 1칸, 2칸, 4칸, 탭 등 여러가지 방식이 있다. 일반적으로 파이썬은 네 개의 공백 문자를 사용하여 들여쓰기를 수행한다.

코드가 정확하게 들여쓰여지지 않으면 실행되지 않고 오류도 발생한다. 중요한 것은 같은 블록 내에서는 들여쓰기 칸 수가 같아야한다는 것이다. 들여쓰기 규칙 위반시에는 `IndentationError: unexpected indent` 에러를 출력한다.

#### References

- [제 01장 첫번째 계단밟기 02. 들여쓰기(indent) -  Python 계단밟기](https://wikidocs.net/20368)

---

## #15

#### What is the difference between Python Arrays and lists?

Python에서는 array과 list가 동일한 방식으로 데이터를 저장한다. 차이점은, 배열은 단일 데이터 타입 요소만 포함할 수 있는 반면, 리스트에는 다양한 타입의 요소들이 들어갈 수 있다는 것이다. array의 선언 방법은 `arrayName = array(type, [Values])`처럼 자료형을 정하고, 지정한/동일한 자료형만을 넣을 수 있도록 되어있다. list은 변수에 `[]`로 여러 타입의 변수를 묶어서 선언할 수 있다.

array에서 사용할 수 있는 타입은 아래와 같다.

![array_data_type](/images/sally/2021-05-09-03-08-13.png)

> 예시

```python
import array as arr

My_Array=arr.array('i',[1,2,3,4])
My_list=[1,'abc',1.20]
print(My_Array)
print(My_list)

# Output: array(‘i’, [1, 2, 3, 4]) [1, ‘abc’, 1.2]
```

#### References

- [파이썬[Python] 036 Array(배열) 사용하기 - SmartLeader 끔손](https://appia.tistory.com/125)

---

## #16

#### What are functions in Python?

함수는 호출될 때만 실행되는 코드 블록이다. Python 함수를 정의하기 위해 def 키워드가 사용된다. 반복되는 부분을 함수로 만들어서 사용하면, 똑같은 코드를 여러번 반복하여 쓰지 않아도 되고, 프로그램의 흐름을 쉽게 파악할 수 있다는 장점이 있다.

> 예시

```python
def Newfunc():
  print("Hi, Welcome to Edureka")

Newfunc(); # 함수 호출

# Output: Hi, Welcome to Edureka
```

#### References

- [04-1 함수 - 점프 투 파이썬](https://wikidocs.net/24)

---

## #17

#### What is `__init__`?

`__init__`는 파이썬에서 특별하게 약속된 메서드 가운데 하나로, 초기화 메서드 혹은 생성자라고도 한다. 이 메서드는 클래스의 새 개체/인스턴스가 생성될 때 메모리를 할당하기 위해 자동으로 호출되며, 그 객체가 갖게 될 여러 가지 성질을 정해준다. 모든 클래스에는 `__init__` 메서드가 있다.

> 예시

```python
class Employee:
  def __init__(self, name, age,salary):
    self.name = name
    self.age = age
    self.salary = 20000

E1 = Employee("XYZ", 23, 20000)

# E1은 Employee 클래스의 객체
# __init__ 는 E1에 메모리를 할당함

print(E1.name)
print(E1.age)
print(E1.salary)

'''
출력:

XYZ
23
20000
'''
```

#### References

- [7.5. 특별한 메서드들 - 왕초보를 위한 Python](https://wikidocs.net/89)

---

## #18

#### What is a lambda function?

익명 함수(이름이 없는 함수)를 람다 함수라고 한다. 람다 함수는 `def` 키워드를 통해서 함수를 생성하는 리터럴 표기법을 **딱 한 줄의 코드로 표현**할 수 있게 해주며, `lambda 인자 : 표현식`의 형식으로 표현한다. 람다함수는 결과 부분을 return 키워드 없이 자동으로 return한다.  람다함수를 사용하면 코드가 간결해지고 메모리가 절약된다는 장점이 있다. 그러나 함수에 이름이 없고, 저장된 변수가 없기 때문에 다시 사용하기 위해서는 다시 코드를 적어주거나, 람다함수를 변수에 담아주어야한다. 람다함수도 객체이기 때문에 정의와 동시에 변수에 담을 수는 있다. 재사용할 이유가 없다면 lambda 함수를 생성하여 넘겨주는 편이 좋다.

람다함수의 표현법을 그림으로 표현하면 아래와 같다.  

<img src="/images/sally/2021-05-09-03-28-16.png" width="60%">

> 예시

```python
a = lambda x, y : x + y
print(a(5, 6))

# Output: 11
```

#### References

- [3.5 람다(lambda) - 왕초보를 위한 Python - WikiDocs](https://wikidocs.net/64)
- [4) 람다함수(익명함수) - 제대로 파이썬 - WikiDocs](https://wikidocs.net/22804)

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
