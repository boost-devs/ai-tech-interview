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

> 파이썬2에서는 `range`와 `xrange` 모두 존재하지만, 파이썬3부터는 `range`가 내부적으로 `xrange`로 동작하도록 바뀌어서 `range`만 존재한다. 그러므로 **파이썬2**를 기준으로 `range`와 `xrange`를 설명한다.

`range` 객체는 입력으로 받은 정수 범위의 값을 요소로 같는 리스트를 말한다. 그러므로 `range(3)`과 ` [0, 1, 2]`는 완전히 동일하다.

```python
# python2
r = range(5)
print(r)            # [0, 1, 2, 3, 4]
print(type(r))      # <type 'list'>
```

`xrange`는 제너레이터 객체로, 오직 루프를 돌때만 해당 범위의 정수를 하나씩 반환한다. 제너레이터에 관한 설명은 [여기](#28)에서!

```python
#python2
r = xrange(5)
print(r)            # xrange(5)
print(type(r))      # <type 'xrange'>

for i in r:
    print i,
# >> 0 1 2 3 4
```

#### References

- [python range() 와 xrange() 차이 - ㅍㅍㅋㄷ](https://bluese05.tistory.com/57)
- [[python] range, xrange 차이 - 코딩장이](https://itholic.github.io/python-range-xrange/)
- [range() vs xrange() in Python - GeeksforGeeks](https://www.geeksforgeeks.org/range-vs-xrange-python/)

---

## #26

#### How do you write comments in python?

> 따옴표를 이용한 주석은 Docstring 형식으로 자세한 내용은 [#32](#32)를 참고!

`#`을 사용하여 주석을 달 수 있다.

```python
# this is my comment
```

#### References

- [Documenting Python Code: A Complete Guide - Real Python](https://realpython.com/documenting-python-code/)

---

## #27

#### What is pickling and unpickling?

Pickle module accepts any Python object and converts it into a string representation and dumps it into a file by using dump function, this process is called pickling. While the process of retrieving original Python objects from the stored string representation is called unpickling.

우선 `직렬화(Serialization)`와 `역 직렬화(Deserialization)`의 개념을 알아야 한다. `직렬화`란 객체를 바이트 스트림(byte stream)으로 변환하여 디스크에 저장하거나 네트워크로 보낼 수 있도록 만들어주는 것을 말한다. 반대로 바이트 스트림을 파이썬 객체로 변환하는 것을 `역 직렬화`라고 한다.

**pickle 모듈**은 파이썬 객체의 직렬화와 역 직렬화를 수행하는 모듈이다. 이 때 파이썬 객체를 직렬화할 때를 `pickling`이라고 하며, 바이트 스트림을 역 직렬화할 때를 `unpickling`이라고 한다.

#### References

- [pickle — 파이썬 객체 직렬화 - Python Documentation](https://docs.python.org/ko/3/library/pickle.html)
- [The Python pickle Module: How to Persist Objects in Python - Real Python](https://realpython.com/python-pickle-module/)

---

## #28

#### What are the generators in python?

제너레이터(Generator)란 Iterator 객체를 간단히 만들 수 있는 함수를 말한다. 제너레이터는 다음과 같이 ① yield문과 함수, ② 표현식 형태로 만들 수 있다.

> **방법 1. yield문과 함수**

- 제너레이터 함수 정의

```python
def generator_list(value):
    for i in range(value):
        # 값을 반환하고 여기를 기억
        yield i
```

- 제너레이터 객체 생성 및 next 함수로 호출

```python
gen = generator_list(2)
print(next(gen))    # 0
print(next(gen))    # 1
print(next(gen))    # StopIteration 에러 발생
```

> **방법 2. 표현문**

```python
value = 2
gen = (i for i in range(value))
print(next(gen))    # 0
print(next(gen))    # 1
print(next(gen))    # StopIteration 에러 발생
```

그럼 왜 리스트 대신 제너레이터를 사용할까? 리스트를 사용하면 리스트의 크기만큼 메모리에 공간이 할당된다. 반면 제너레이터는 말그대로 next 함수로 호출될 때 값을 생성하고 해당 값만 메모리에 올린다! 즉, 메모리를 절약할 수 있다. 작은 데이터라면 상관없지만 큰 데이터에서는 제너레이터 사용이 필수이다.

#### References

- [🐍 제너레이터(Generator) - 코딩하는펭귄의 저장소](https://cooding-penguin.netlify.app/python/generator/)
- [How to Use Generators and yield in Python - Real Python](https://realpython.com/introduction-to-python-generators/)

---

## #29

#### How will you capitalize the first letter of string?

문자열 메서드 `capitalize`를 사용하면 된다.

```python
string = "boostcamp ai tech"
print(string.capitalize())      # Boostcamp ai tech
```

자세한 문자열 메서드는 [여기](https://www.w3schools.com/python/python_ref_string.asp)를 참고!

#### References

- [Python String Methods - w3schools](https://www.w3schools.com/python/python_ref_string.asp)

---

## #30

#### How will you convert a string to all lowercase?

문자열 메서드 `lower`을 사용하면 된다.

```python
string = "BOOSTCAMP AI TECH"
print(string.lower())           # boostcamp ai tech
```

#### References

- [Python String Methods - w3schools](https://www.w3schools.com/python/python_ref_string.asp)

---

## #31

#### How to comment multiple lines in python?

> 따옴표를 이용한 주석은 Docstring 형식으로 자세한 내용은 [#32](#32)를 참고!

`#`을 여러 줄 사용하여 여러 줄의 주석을 달 수 있다.

```python
# this is my comment
# I am commenting multiple lines
# - boostcamp ai tech team 4
```

#### References

- [Documenting Python Code: A Complete Guide - Real Python](https://realpython.com/documenting-python-code/)

---

## #32

#### What are docstrings in Python?

docstrings은 주석은 아니지만, 사용자에게 코드에 대한 설명을 적어놓은 문서(documentation)이다. docstrings는 `__doc__` 속성이나 `help()` 내장 함수로 접근할 수 있다. docstrings는 작은 따옴표(`'`) 혹은 큰 따옴표(`"`) 3개로 작성할 수 있다.

```python
def mult(a, b):
  """
  Returns the product of a and b
  - a(float): any real number
  - b(float): any real number 
  """
  return a*b
```

```python
print(help(mult))
print(mult.__doc__)
```

> **Comments(주석) vs Dosctrings**     
> comments와 docstrings은 각각 `#`, `"""`을 쓴다는 점에서 다르지만 가장 큰 차이는 **읽는 대상**이다. comments는 개발을 위해 동료 혹은 나중에 코드를 읽을 나에게 남겨놓는 것이고 docstrings는 이 코드를 사용할 사용자들이 이해하기 쉽도록 남겨놓는 것이다.

#### References

- [Documenting Python Code: A Complete Guide - Real Python](https://realpython.com/documenting-python-code/)

---

## #33

#### What is the purpose of is, not and in operators?

`is`는 객체 비교 연산자(identity operator)로 두 변수가 참조하는 객체의 id가 같을 경우 **True**를 반환한다. 보통 두 변수가 참조하는 객체가 동일한 객체인지 확인할 때 사용한다.

```python
a = [1, 2, 3]
b = a
c = a.copy()

print(a is b) # True
print(a is c) # False
```

`not`은 단항 논리 연산자(logical operator)로 뒤에 오는 boolean 값을 뒤집는다. 뒤에 오는 값이 **True**이면 **False**를, **False**이면 **True**를 반환한다.

```python
print(not True)   # False
print(not False)  # True
```

`in`은 멤버 연산자(membership operator)로, 요소 a와 시퀀스 b가 있는 지를 확인하고 싶을 때 `a in b`로 표현하며 만약 a가 b 안에 있다면 **True**를, 없으면 **False**를 반환한다.

```python
b = "abc"
print("a" in b) # True
print("z" in b) # False
```

#### References

- [Python Operators - w3schools](https://www.w3schools.com/python/python_operators.asp)

---

## #34

#### What is the usage of help() and dir() function in Python?

`help()`는 docstrings를 작성하였다면 해당 docstrings를 출력한다. docstrings에는 클래스, 메서드의 사용법에 관한 내용이 담겨있으므로 해당 클래스와 메서드를 사용자에게 매우 유용하다. docstrings에 대한 내용은 [#31](#31) 참고!

`dir()`은 인자로 넣은 객체의 속성과 메서드를 문자열로 변환하고 그것을 요소로 갖는 정렬된 리스트를 반환한다. `dir`은 사용할 객체의 메서드와 속성에 대한 정보를 얻고 싶을 때 유용하다. 다만 인자가 없다면 현재 지역 스코프에서 정의된 함수와 변수들의 리스트를 반환한다.

```python
def func(x):
  return x

a = 3
print(dir(a))     # 객체 a에 대한 속성, 메서드
print(dir(func))  # 함수 func에 대한 속성, 메서드
print(dir())      # 지역 스코프에 정의된 a와 func
```

#### References

- [내장 함수: help() - Python Documentation](https://docs.python.org/ko/3/library/functions.html#help)
- [내장 함수: dir() - Python Documentation](https://docs.python.org/ko/3/library/functions.html#dir)
- [10 Python built-in functions you should know](https://towardsdatascience.com/10-python-built-in-functions-you-should-know-fbd5c879e0ab)
---

## #35

#### Whenever Python exits, why isn’t all the memory de-allocated?

다른 객체나 전역 네임스페이스에서 참조되는 객체를 순환 참조하는 파이썬 모듈은 항상 해제되지는 않는다. 또한 C 라이브러리가 예약한 메모리의 해당 부분을 해제하는 것은 불가능하다. 그러므로 파이썬 종료 시, 모든 메모리가 해제되지는 않는다.

> **순환 참조(Circular Reference)**
> 두 객체가 서로 참조하는 경우를 말한다. 


> **전역 네임스페이스(Global Namespace)**    
> 네임스페이스(namespace)란 프로그래밍 언어에서 특정 객체를 이름에 따라 구분할 수 있는 범위를 의미한다. 전역 네임스페이스는 import한 모듈들의 이름을 포함하며, 스크립트가 끝날 때까지 지속된다.

#### References

- [Releasing memory in Python - Net-informations.com](http://net-informations.com/python/iq/memory.htm)
- [Whenever you exit Python, is all memory de-allocated? - BYTES](https://bytes.com/topic/python/answers/972248-whenever-you-exit-python-all-memory-de-allocated)
- [Circular References in Python - hearsaysocial](http://engineering.hearsaysocial.com/2013/06/16/circular-references-in-python/)
- [[Python] 네임스페이스 개념 정리 - Hyungcheol Noh's Blog](https://hcnoh.github.io/2019-01-30-python-namespace)
- [네임스페이스 - 제대로 파이썬](https://wikidocs.net/23109)

---

## #36

#### What is a dictionary in Python?

딕셔너리는 **key값과 그에 대응하는 value값을 얻을 수 있는 컬렉션**을 말한다. 딕셔너리는 데이터가 들어온 순서가 상관이 없고, 인덱싱이 되어 있어 key값으로 요소에 접근하여 데이터(= value) 수정이 가능하다. 하지만, key값은 고유 값이므로 key값 중복은 불가능하다. 주로 자체적으로 만든 key값으로 데이터에 접근하고 싶을 때 딕셔너리 컬렉션을 사용한다.

딕셔너리의 뜻은 사전이다. 영한 사전에서 각 영단어(ex. beautiful)에 대응하는 단어(ex. 아름다운)가 나오는 것처럼, 영단어가 key값이고 그에 대응하는 단어를 value값으로 볼 수 있다.

>  **특징1** : 딕셔너리는 {, }를 사용하여 선언하며 { key1 : value1, key2 : value2, ... } 로 요소를 나타낸다.

- key값으로 변하지 않는 값을 사용하고, value값으로 변하는 값과 변하지 않는 값 둘 다 사용할 수 있다.
- key값으로 리스트를 사용하면, 값이 변할 가능성이 있기 때문에 인터프리터에서 type error를 발생시킨다.

```python
ex1 = {'name':'Groot', 'lover':'penguin', 'feature':'really cute'}

# 딕셔너리 생성자로 집합을 생성하는 경우
ex2 = dict(name='Groot', lover='penguin', feature='really cute')

# key값은 변하지 않는 값, value값은 변하지 않는 값과 변하는 값 둘 다 가능
ex3 = {[10, 3]:'birthday'}	# type error!
```

> **특징2** : 딕셔너리는 딕셔너리 쌍(key : value)을 추가하거나 제거할 수 있다.

- 추가 : dict_ex[ 새로운 key값 ] = 그에 대응하는 value값으로 추가할 수 있다.
- 제거 : del 키워드를 이용해 특정 쌍을 제거할 수 있다.
  - 딕셔너리 앞에 del 키워드를 쓰면 딕셔너리가 완전히 제거된다.

```python
ex = {'Kevin':180, 'Anna':165, 'Penelope':175}

# 새로운 딕셔너리 쌍 추가
ex['Groot'] = 100
print(ex)		# {'Kevin': 180, 'Anna': 165, 'Penelope': 175, 'Groot': 100}

# del 키워드로 딕셔너리 쌍 제거
del ex['Penelope']
print(ex)		# {'Kevin': 180, 'Anna': 165, 'Groot': 100}

# del 키워드로 딕셔너리 완전 제거
del ex
print(ex)       	# name error!
```

> **특징3** : 딕셔너리의 key값은 중복될 수 없다.

- key값은 고유값이므로 2개 이상의 key값이 존재할 수 없다.
  - key값에 해당하는 value값을 어떤 걸 불러야할지 모르기 때문.
- key값이 중복될 경우 하나를 제외한 나머지 것들이 모두 무시된다.
  - key값에 대입한 최근의 value값을 불러온다.

```python
ex = {'name': 'Groot', 'lover': 'Penguin', 'feature': 'cute', 'feature': 'handsome'}

print(ex)  # {'name': 'Groot', 'lover': 'Penguin', 'feature': 'handsome'}
```

#### References

- [Python Dictionaries - w3schools](https://www.w3schools.com/python/python_dictionaries.asp)

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
