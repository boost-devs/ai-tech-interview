<div align='center'>
  <h1>🌐 Network 🌐</h1>
</div>

> 질문 중 일부는 <strong>[WeareSoft님의 tech-interview](https://github.com/WeareSoft/tech-interview)</strong>를 참고하였으며, 질문에 대한 답변은 직접 작성하였습니다.

---

## Table of Contents

- [TCP/IP의 각 계층을 설명해주세요.](#1)
- [OSI 7계층와 TCP/IP 계층의 차이를 설명해주세요.](#2)
- [Frame, Packet, Segment, Datagram을 비교해주세요.](#3)
- [TCP와 UDP의 차이를 설명해주세요.](#4)
- [TCP와 UDP의 헤더를 비교해주세요.](#5)
- [TCP의 3-way-handshake와 4-way-handshake를 비교 설명해주세요.](#6)
- [TCP의 연결 설정 과정(3단계)과 연결 종료 과정(4단계)이 단계가 차이나는 이유가 무엇인가요?](#7)
- [만약 Server에서 FIN 플래그를 전송하기 전에 전송한 패킷이 Routing 지연이나 패킷 유실로 인한 재전송 등으로 인해 FIN 패킷보다 늦게 도착하는 상황이 발생하면 어떻게 될까요?](#8)
- [초기 Sequence Number인 ISN을 0부터 시작하지 않고 난수를 생성해서 설정하는 이유가 무엇인가요?](#9)
- [HTTP와 HTTPS에 대해서 설명하고 차이점에 대해 설명해주세요.](#10)
- [HTTP 요청/응답 헤더의 구조를 설명해주세요.](#11)
- [HTTP와 HTTPS 동작 과정을 비교해주세요.](#12)
- [CORS가 무엇인가요?](#13)
- [HTTP GET과 POST 메서드를 비교/설명해주세요.](#14)
- [쿠키(Cookie)와 세션(Session)을 설명해주세요.](#15)
- [DNS가 무엇인가요?](#16)
- [REST와 RESTful의 개념을 설명하고 차이를 말해주세요.](#17)
- [소켓(Socket)이 무엇인가요? 자신 있는 언어로 간단히 소켓 생성 예시를 보여주세요.](#18)
- [Socket.io와 WebSocket의 차이를 설명해주세요.](#19)
- [IPv4와 IPv6 차이를 설명해주세요.](#20)
- [MAC Address가 무엇인가요?](#21)
- [라우터와 스위치, 허브의 차이를 설명해주세요.](#22)
- [SMTP가 무엇인가요?](#23)
- [노트북으로 `www.google.com`에 접속을 했습니다. 요청을 보내고 받기까지의 과정을 자세히 설명해주세요.](#24)
- [여러 네트워크 topology에 대해 간단히 소개해주세요.](#25)
- [subnet mask에 대해서 설명해주세요.](#26)
- [data encapsulation이 무엇인가요?](#27)
- [DHCP를 설명해주세요.](#28)
- [routing protocol을 몇 가지 설명해주세요. (ex. link state, distance vector)](#29)
- [이더넷(ethernet)이 무엇인가요?](#30)
- [client와 server의 차이점을 설명해주세요.](#31)
- [delay, timing(jitter), throughput 차이를 설명해주세요.](#32)

---

## #1

#### TCP/IP의 각 계층을 설명해주세요.

#### References

---

## #2

#### OSI 7계층와 TCP/IP 계층의 차이를 설명해주세요.

#### References

---

## #3

#### Frame, Packet, Segment, Datagram을 비교해주세요.

#### References

---

## #4

#### TCP와 UDP의 차이를 설명해주세요.

#### References

---

## #5

#### TCP와 UDP의 헤더를 비교해주세요.

#### References

---

## #6

#### TCP의 3-way-handshake와 4-way-handshake를 비교 설명해주세요.

#### References

---

## #7

#### TCP의 연결 설정 과정(3단계)과 연결 종료 과정(4단계)이 단계가 차이나는 이유가 무엇인가요?

#### References

---

## #8

#### 만약 Server에서 FIN 플래그를 전송하기 전에 전송한 패킷이 Routing 지연이나 패킷 유실로 인한 재전송 등으로 인해 FIN 패킷보다 늦게 도착하는 상황이 발생하면 어떻게 될까요?

#### References

---

## #9

#### 초기 Sequence Number인 ISN을 0부터 시작하지 않고 난수를 생성해서 설정하는 이유가 무엇인가요?

Connection을 맺을 때 사용하는 포트는 유한 범위 내에서 사용하고 시간이 지남에 따라 재사용된다.

따라서 두 통신 호스트가 과거에 사용된 포트 번호 쌍을 사용하는 가능성이 존재한다.

서버 측에서는 패킷의 SYN을 보고 패킷을 구분하게 되는데 난수가 아닌 순차적인 number가 전송된다면 이전의 connection으로부터 오는 패킷으로 인식할 수 있다.

이러한 문제가 발생할 가능성을 줄이기 위해서 난수로 ISN을 설정하는 것이다.

#### References

- [[Network] (TCP) 3-way-handshake & 4-way-handshake - 어제보다 한 걸음 더](https://k39335.tistory.com/21)

---

## #10

#### HTTP와 HTTPS에 대해서 설명하고 차이점에 대해 설명해주세요.

- <strong>HTTP(Hyper Text Transfer Protocol)</strong>

HTTP란 **서버/클라이언트 모델을 따라 데이터를 주고받기 위한 프로토콜**이다. 즉, HTTP는 인터넷에서 하이퍼텍스트를 교환하기 위한 통신 규약으로, 80번 포트를 사용하고 있다. 따라서 HTTP 서버가 80번 포트에서 요청을 기다리고 있으며, 클라이언트는 80번 포트로 요청을 보내게 된다.

HTTP는 1989년 팀 버너스 리(Tim Berners Lee)에 의해 처음 설계되었으며, WWW(World-Wide-Web) 기반에서 세계적인 정보를 공유하는데 큰 역할을 하였다.
<br><br>

- <strong>HTTPS(Hyper Text Transfer Protocol Secure)</strong>

HTTPS는 **HTTP에 데이터 암호화가 추가된 프로토콜**이다. HTTPS는 HTTP와 다르게 433번 포트를 사용하며, 네트워크 상에서 중간에 제3자가 정보를 볼 수 없도록 공개키 암호화를 지원하고 있다.
<br><br>

HTTP는 암호화가 추가되지 않았기 때문에 보안에 취약한 반면, HTTPS는 안전하게 데이터를 주고받을 수 있다. 하지만 HTTPS를 이용하면 암호화/복호화의 과정이 필요하기 때문에 HTTP보다 속도가 느리다. 또한 HTTPS는 인증서를 발급하고 유지하기 위한 추가 비용이 발생하다.

개인 정보와 같은 민감한 데이터를 주고받아야 한다면 HTTPS를 이용해야 하지만, 단순한 정보 조회 등 만을 처리하고 있다면 HTTP를 이용하면 된다.

#### References

- [[Web] HTTP와 HTTPS 및 차이점 - MangKyu's Diary](https://mangkyu.tistory.com/98)

---

## #11

#### HTTP 요청/응답 헤더의 구조를 설명해주세요.

- **HTTP Request Headers**
  - 해당 request에 대한 추가 정보(addtional information)를 담고 있는 부분
    - ex. request 메세지 body의 총 길이(Content-Length) 등
  - Key:Value 값으로 되어있다.
    - ex. HOST:google.com → Key=HOST, Value=google.com
  - Headers는 크게 3부분으로 나뉜다(general headers, request headers, entity headers)
  - 자주 사용되는 header 정보에는 다음이 있다.
    - Host
      - 요청이 전송되는 target의 host url
        - ex. google.com
    - User-Agent
      - 요청을 보내는 클라이언트의 대한 정보
        - ex. 웹브라우저에 대한 정보
    - Accept
      - 해당 요청이 받을 수 있는 응답(response) 타입
    - Connection
      - 해당 요청이 끝난후에 클라이언트와 서버가 계속해서 네트워크 컨넥션을 유지 할것인지 아니면 끊을것인지에 대해 지시하는 부분
    - Content-Type
      - 해당 요청이 보내는 메세지 body의 타입
        - ex. JSON을 보내면 application/json
    - Content-Length
      - 메세지 body의 길이
<br><br>

- **HTTP Response Headers**
  - Response의 headers와 동일하다.
  - 다만 response에서만 사용되는 header 값들이 있다.
    - ex. User-Agent 대신에 Server 헤더가 사용된다.
<br><br>

<div align='center'>
  <img src="../images/adc/network/http.PNG">
  <br><br>
  <img src="../images/adc/network/http2.png">
</div>

#### References

- [HTTP 구조 및 핵심 요소 - teddybearjung](https://velog.io/@teddybearjung/HTTP-%EA%B5%AC%EC%A1%B0-%EB%B0%8F-%ED%95%B5%EC%8B%AC-%EC%9A%94%EC%86%8C)
- [[네트워크] http 란 - 인생의 로그캣](https://noahlogs.tistory.com/34?category=827412)
- [HTTP 메시지 - MDN Web Docs](https://developer.mozilla.org/ko/docs/Web/HTTP/Messages)

---

## #12

#### HTTP와 HTTPS 동작 과정을 비교해주세요.

<div align='center'>
  <img src="https://t1.daumcdn.net/cfile/tistory/99E3EE4F5C0FE49F17">
  <br><br>
  <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FRhbUB%2Fbtq0iBHCBTX%2FfKL4uGrKHaz7w5rWr9Ottk%2Fimg.png">
  <br><br>
  <img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbE36KD%2Fbtq0tfDkLaZ%2FazI7Wlmon3eCzE5dQKNCq0%2Fimg.png">
</div>

#### References

- [HTTP & DNS & TCP 정의 및 동작원리 - lkh's](https://lkhlkh23.tistory.com/76)
- [[Web 기초] HTTP 통신 과정 - MYSTERICO BLOG](https://mysterico.tistory.com/29)
- [[Web 기초] HTTPS의 동작 원리 (feat. 와이어샤크) - MYSTERICO BLOG](https://mysterico.tistory.com/30)

---

## #13

#### CORS가 무엇인가요?

교차 출처 리소스 공유(Cross-Origin Resource Sharing, CORS)는 추가 HTTP 헤더를 사용하여, 한 출처에서 실행 중인 웹 애플리케이션이 다른 출처의 선택한 자원에 접근할 수 있는 권한을 부여하도록 브라우저에 알려주는 체제이다.

> CORS 체제는 브라우저와 서버 간의 안전한 교차 출처 요청 및 데이터 전송을 지원한다.<br>최신 브라우저는 XMLHttpRequest 또는 Fetch와 같은 API에서 CORS를 사용하여 교차 출처 HTTP 요청의 위험을 완화 한다.

- 웹 애플리케이션은 리소스가 자신의 출처(도메인, 프로토콜, 포트)와 다를 때 교차 출처 HTTP 요청을 실행한다.
- 브라우저는 보안 상의 이유로, 스크립트에서 시작한 교차 출처 HTTP 요청을 제한한다.
  - ex) domain-a.com ↔ domain-b.com 간의 요청은 CORS 정책 위반으로, 브라우저에서 요청을 제한
- 따라서 다른 출처의 리소스를 불러오기 위해서는, 그 출처에서 교차 출처 리소스 공유에 대한 헤더(CORS)를 응답시 반환 해주어야 한다.

**CORS의 동작 원리**

1. 기본적으로 웹은 다른 출처의 리소스를 요청할 때는 HTTP 프로토콜을 사용하여 요청을 하는데, 이때 브라우저는 요청 헤더 (request header)에 `Origin` 필드에 요청을 보내는 출처를 담아 전송한다.
2. 서버는 요청에 대한 응답을 하는데, 응답 헤더(response header)에 `Access-Control-Allow-Origin`이라는 값에 '이 리소스를 접근하는 것이 허용된 출처'를 내려준다.
이후 응답을 받은 브라우저는 자신이 보냈던 요청의 Origin과 서버가 보내준 응답의 `Access-Control-Allow-Origin`을 비교해 본 후 이 응답이 유효한 응답인지 아닌지를 결정한다.
<br><br>

<div align='center'>
  <img src="../images/adc/network/CORS.png">
</div>


#### References

- [CORS란 무엇인가 ? - pilyeooong.log](https://velog.io/@pilyeooong/CORS%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80)
- [교차 출처 리소스 공유 - 위키백과](https://ko.wikipedia.org/wiki/%EA%B5%90%EC%B0%A8_%EC%B6%9C%EC%B2%98_%EB%A6%AC%EC%86%8C%EC%8A%A4_%EA%B3%B5%EC%9C%A0)

---

## #14

#### HTTP GET과 POST 메서드를 비교/설명해주세요.

- **GET**

GET은 클라이언트에서 서버로 어떠한 리소스로부터 정보를 요청하기 위해 사용되는 메서드이다.

GET을 통한 요청은 URL 주소 끝에 파라미터로 포함되어 전송되며, 이 부분을 쿼리 스트링(query string)이라고 부른다.

방식은 URL 끝에 `?`를 붙이고 그다음 `변수명1=값1&변수명2=값2...` 형식으로 이어 붙이면 된다.

> ex. `www.example.com/show?name1=value1&name2=value2`

서버에서는 `name1`과 `name2`라는 파라미터 명으로 각각 `value1`과 `value2`의 파라미터 값을 전달받을 수 있다.

- GET의 특징
  - GET 요청은 캐시가 가능하다. 
    - GET을 통해 서버에 리소스를 요청할 때 웹 캐시가 요청을 가로채 서버로부터 리소스를 다시 다운로드하는 대신 리소스의 복사본을 반환한다. HTTP 헤더에서 cache-control 헤더를 통해 캐시 옵션을 지정할 수 있다.
  - GET 요청은 브라우저 히스토리에 남는다.
  - GET 요청은 북마크 될 수 있다.
  - GET 요청은 길이 제한이 있다.
  - GET 요청은 중요한 정보를 다루면 안 된다.
  - GET은 데이터를 요청할 때만 사용된다.
<br><br>
 
- **POST**

POST는 클라이언트에서 서버로 리소스를 생성하거나 업데이트하기 위해 데이터를 보낼 때 사용되는 메서드이다.

POST는 전송할 데이터를 HTTP 메시지 body 부분에 담아서 서버로 보낸다.(body의 타입은 Content-Type 헤더에 따라 결정된다.)

GET에서 URL의 파라미터로 보냈던 `name1=value1&name2=value2`가 body에 담겨 보내진다 생각하면 된다.

POST로 데이터를 전송할 때 길이 제한이 따로 없어 용량이 큰 데이터를 보낼 때 사용하거나 GET처럼 데이터가 외부적으로 드러나는 건 아니라서 보안이 필요한 부분에 많이 사용된다. 

POST를 통한 데이터 전송은 보통 HTML form을 통해 서버로 전송된다. 

- POST의 특징
  - POST 요청은 캐시 되지 않는다.
  - POST 요청은 브라우저 히스토리에 남지 않는다.
  - POST 요청은 북마크 되지 않는다.
  - POST 요청은 데이터 길이에 제한이 없다.
<br><br>

- **차이점**
  - 사용목적: GET은 서버의 리소스에서 데이터를 요청할 때, POST는 서버의 리소스를 새로 생성하거나 업데이트할 때 사용한다.
  - 요청에 body 유무: GET은 URL 파라미터에 요청하는 데이터를 담아 보내기 때문에 HTTP 메시지에 body가 없다. POST는 body에 데이터를 담아 보내기 때문에 당연히 HTTP 메시지에 body가 존재한다.
  - 멱등성(idempotent): GET 요청은 멱등이며, POST는 멱등이 아니다.

> **멱등이란?**<br>멱등의 사전적 정의는 연산을 여러 번 적용하더라도 결과가 달라지지 않는 성질을 의미한다.<br>GET은 리소스를 조회한다는 점에서 여러 번 요청하더라도 응답이 똑같을 것이다. 반대로 POST는 리소스를 새로 생성하거나 업데이트할 때 사용되기 때문에 멱등이 아니라고 볼 수 있다.(POST 요청이 발생하면 서버가 변경될 수 있다.)

#### References

- [[네트워크] get 과 post 의 차이 - 인생의 로그캣](https://noahlogs.tistory.com/35)

---

## #15

#### 쿠키(Cookie)와 세션(Session)을 설명해주세요.

- <strong>쿠키(Cookie)</strong>

쿠키는 클라이언트(브라우저) 로컬에 저장되는 키와 값이 들어있는 작은 데이터 파일이다.

사용자 인증이 유효한 시간을 명시할 수 있으며, 유효 시간이 정해지면 브라우저가 종료되어도 인증이 유지된다는 특징이 있다.

쿠키는 클라이언트의 상태 정보를 로컬에 저장했다가 참조한다.

Response Header에 Set-Cookie 속성을 사용하면 클라이언트에 쿠키를 만들 수 있다.

쿠키는 사용자가 따로 요청하지 않아도 브라우저가 Request 시에 Request Header를 넣어서 자동으로 서버에 전송한다.


- 쿠키의 동작 방식
  1. 클라이언트가 페이지를 요청
  2. 서버에서 쿠키를 생성
  3. HTTP 헤더에 쿠키를 포함 시켜 응답
  4. 브라우저가 종료되어도 쿠키 만료 기간이 있다면 클라이언트에서 보관
  5. 같은 요청을 할 경우 HTTP 헤더에 쿠키를 함께 보냄
  6. 서버에서 쿠키를 읽어 이전 상태 정보를 변경할 필요가 있을 때 쿠키를 업데이트하여 변경된 쿠키를 HTTP 헤더에 포함시켜 응답
<br><br>

- <strong>세션(Session)</strong>

세션은 쿠키를 기반하고 있지만, 사용자 정보 파일을 브라우저에 저장하는 쿠키와 달리 세션은 서버 측에서 관리한다.

서버에서는 클라이언트를 구분하기 위해 세션 ID를 부여하며 웹 브라우저가 서버에 접속해서 브라우저를 종료할 때까지 인증 상태를 유지한다.

접속 시간에 제한을 두어 일정 시간 응답이 없다면 정보가 유지되지 않게 설정이 가능하다.

사용자에 대한 정보를 서버에 두기 때문에 쿠키보다 보안에 좋지만, 사용자가 많아질수록 서버 메모리를 많이 차지하게 된다.

즉 동접자 수가 많은 웹 사이트인 경우 서버에 과부하를 주게 되므로 성능 저하의 요인이 된다.

클라이언트가 Request를 보내면, 해당 서버의 엔진이 클라이언트에게 유일한 ID를 부여하는 데 이것이 세션 ID다.


- 세션의 동작 방식
  1. 클라이언트가 서버에 접속 시 세션 ID를 발급
  2. 클라이언트는 세션 ID에 대해 쿠키를 사용해서 저장하고 가지고 있음
  3. 클라이언트는 서버에 요청할 때, 이 쿠키의 세션 ID를 서버에 전달해서 사용
  4. 서버는 세션 ID를 전달받아서 별다른 작업 없이 세션 ID로 세션에 있는 클라언트 정보를 가져옴
  5. 클라이언트 정보를 가지고 서버 요청을 처리하여 클라이언트에게 응답
<br><br>

- **차이점**
  - 사용자의 정보가 저장되는 위치
    - 쿠키는 서버의 자원을 전혀 사용하지 않으며, 세션은 서버의 자원을 사용한다.
  - 보안
    - 쿠키는 클라이언트 로컬에 저장되기 때문에 변질되거나 request에서 스니핑 당할 우려가 있어서 보안에 취약하다.
    - 세션은 쿠키를 이용해서 세션 ID만 저장하고 그것으로 구분해서 서버에서 처리하기 때문에 비교적 보안성이 좋다.
  - 라이프 사이클
    - 쿠키는 만료시간이 있지만 파일로 저장되기 때문에 브라우저를 종료해도 계속해서 정보가 남아 있을 수 있다. 또한 만료 기간을 넉넉하게 잡아두면 쿠키 삭제를 할 때까지 유지될 수도 있다.
    - 반면에 세션도 만료시간을 정할 수 있지만 브라우저가 종료되면 만료시간에 상관없이 삭제된다.
  - 속도
    - 쿠키에 정보가 있기 때문에 서버에 요청 시 속도가 빠르다.
    - 세션은 정보가 서버에 있기 때문에 처리가 요구되어 비교적 느린 속도를 낸다.

세션은 서버의 자원을 사용하기 때문에 무분별하게 만들다 보면 서버의 메모리가 감당할 수 없어질 수가 있고 속도가 느려질 수 있기 때문에 쿠키를 함께 사용한다.

#### References

- [쿠키와 세션 개념 - 라이언 서버](https://interconnection.tistory.com/74)

---

## #16

#### DNS가 무엇인가요?

- **Domain**

모든 네트워크 통신에는 고유의 주소, 즉 IP 주소가 필요하다.

이때 통신을 주고받는 주체가 되는 네트워크에 연결되어 있는 모든 장치들을 host라고 한다.

IP는 사람이 이해하고 기억하기 어렵기 때문에 이를 위해서 각 ip에 부여한 이름이 도메인이다.

예를 들어 210.89.164.90의 도메인은 naver.com이다.
<br><br>

- <strong>DNS(Domain Name Service)</strong>

DNS(Domain Name Server 또는 Domain Name Service 모두를 의미)를 통해 네트워크 통신은 IP 주소를 사용하는데 어떻게 도메인을 가지고 통신을 할 수 있다.

DNS는 숫자로 이루어진 IP 주소와 일정한 형식을 가진 도메인을 서로 매핑 시키고 정보를 가지고 있다.


예를 들어 네이버에 접속하기 위해 주소창에 도메인(naver.com)을 입력하면, 컴퓨터는 해당 도메인이 연결된 네임서버(DNS)로 가서 서버 IP를 요청한다.

요청받은 네임 서버는 해당 도메인과 연결되어 있는 서버 IP(210.89.164.90)를 찾은 후, 컴퓨터에게 알려준다.

이처럼 도메인에 연결된 서버의 주소를 찾아주는 역할이 네임서버(DNS)이다.
<br><br>

- **브라우저가 도메인에 해당하는 IP를 찾는 순서**
1. local cache 안에 검색한 해당 도메인의 IP가 있는지 확인한다. 이미 해당 도메인을 방문한 적이 있다면 컴퓨터가 해당 도메인의 IP를 기억하고 있으므로 그것을 사용한다.
2. 만약 캐시에 없다면 컴퓨터 내부에 파일 형태로 존재하는 hosts 파일을 검색해서 찾는다. 해당 hosts 파일에 특정 도메인과 IP를 매핑 시켜놓으면 해당 도메인은 지정한 IP로 이동한다.
3. 만약 위의 경우에서 도메인에 대한 IP를 찾지 못하면 최종적으로 DNS를 검색한다.
<br><br>

<div align='center'>
  <img src="../images/adc/network/dns.png">
</div>

#### References

- [[Network] 네트워크 기초 개념 - 차근차근 개발로그](https://hyuntaekhong.github.io/blog/Network/#3-dnsdomain-name-service)
- [Domain, DNS란 무엇인가 - 매일의 공부 기록](https://study-recording.tistory.com/8)

---

## #17

#### REST와 RESTful의 개념을 설명하고 차이를 말해주세요.

`REST`란 **Re**presentational **S**tate **T**ransfer의 약자로, <u>URI로 자원(Resource)을 명시하고 HTTP 메서드를 통해 해당 자원에 대한 CRUD 연산을 적용하는 것</u>을 의미한다.

여기서의 자원은 데이터베이스의 정보를 말한다. 하지만 클라이언트가 직접 데이터베이스에 접속해 변경하는 것은 매우 위험한 방식 이다. 그래서 이를 막기 위해 REST API를 사용하는 것이다. **클라이언트**가 서버에 데이터를 조회·생성·삭제·업데이트를 하겠다고 <u>HTTP 메서드로 요청</u>을 하면 **서버**는 로직에 따라 데이터베이스에 접근하여 <u>요청을 처리</u>한다.

`RESTful`은 REST 아키텍처로 구현된 웹 서비스를 나타내기 위한 용어로, "REST API를 제공하는 웹 서비스는 RESTful하다"처럼 사용된다.

> **HTTP 메서드 종류**

요청의 종류에 다라 다른 HTTP 메서드를 사용하는데 주로 사용하는 대표적인 메서드는 다음과 같다.

| 메서드 | 역할                                                    |
| :----: | :------------------------------------------------------ |
|  GET   | 데이터를 조회한다.                                      |
|  POST  | 데이터를 등록한다. 인증 작업을 거칠 때 사용하기도 한다. |
| DELETE | 데이터를 삭제한다.                                      |
|  PUT   | 데이터를 새 정보로 통째로 업데이트할 때 사용한다.       |
| PATCH  | 데이터의 특정 필드를 수정할 때 사용한다.                |

> **URI란?**

URI는 Uniform Resource Identifier의 약자로, 자원을 식별자로 취급하여 나타내는 주소를 말한다. URI의 종류로 URL과 URN이 있다. URI는 일반적으로 다음과 같은 형식을 갖고 있다.

<div align="center">
<img src="../images/penguin/uri.png" width="90%"/>
</div>
<br/>

#### References

- [[Network] REST란? REST API란? RESTful이란? - HeeJeong Kwon](https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html)
- [REST API 제대로 알고 사용하기 - NHN Cloud Meetup!](https://meetup.toast.com/posts/92)
- [URL과 URI의 의미와 차이점 (Difference between URL & URI) - Lael's World](https://blog.lael.be/post/61)
- [통합 자원 식별자 - 위키피디아](https://ko.wikipedia.org/wiki/%ED%86%B5%ED%95%A9_%EC%9E%90%EC%9B%90_%EC%8B%9D%EB%B3%84%EC%9E%90)
- [21장. 백엔드 프로그래밍: Node.js의 Koa 프레임워크 - 리액트를 다루는 기술](http://www.yes24.com/Product/Goods/79260300)

---

## #18

#### 소켓(Socket)이 무엇인가요? 자신 있는 언어로 간단히 소켓 생성 예시를 보여주세요.

`소켓(Socket)`이란 <u>Application 프로세스와 end-to-end 통신을 제공하는 Transport 프로토콜 사이의 인터페이스</u>을 말한다. 즉, Application에서 Transport 프로토콜을 쓰기 위한 API를 말한다.

소켓은 크게 UDP와 TCP 두종 종류로 분류할 수 있다. 자세한 내용은 [#4. TCP와 UDP의 차이를 설명해주세요.](#4)을 참고!

파이썬으로 TCP에서의 소켓과 UDP에서의 소켓 생성 코드를 구현하면 다음과 같다. 소켓을 생성한다고 바로 통신을 할 수 없으며 실제 통신을 하기 위해는 바인딩, 연결 등 추가 작업이 필요하다.

> **TCP**

- TCP Client

```python
from socket import *

server_name = "example.com"
server_port = 1234

client_socket = socket(AF_INET, SOCKET_STREAM)  # 소켓 생성
client_socket.connect((server_name, server_port)) # 서버에 연결 요청
```

- TCP Server

```python
from socket import *

server_port = 1234

server_socket = socket(AF_INET, SOCKET_STREAM)  # 소켓 생성
server_socket.bind(('', server_port)) # 소켓에 주소 바인딩
server_socket.listen(1) # 클라이언트 연결 대기

(client_socket, client_address) = server_socket.accept()  # 클라이언트 연결 수락
```

> **UDP**

- UDP Client

```python
from socket import *

server_name = "example.com"
server_port = 1234

client_socket = socket(AF_INET, SOCK_DGRAM) # 소켓 생성
```

- UDP Server

```python
from socket import *

server_port = 1234
server_socket = socket(AF_NET, SOCK_DGRAM)  # 소켓 생성
server_socket.bind(('', server_port)) # 소켓에 주소 바인딩
```

#### References

- [Chapter 2. Application Layer - Computer Networking: A Top-Down Approach](http://www.yes24.com/Product/Goods/24320296?OzSrank=2)

---

## #19

#### Socket.io와 WebSocket의 차이를 설명해주세요.

> **WebSocket**

<div align="center">
<img src="../images/penguin/web-socket.png" width="50%"/>
</div>
<br/>

`WebSocket`은 <u>서버와 브라우저 간 연결을 유지한 상태로 데이터를 교환할 수 있도록 하는 **프로토콜**</u>을 말한다.

전형적인 브라우저 렌더링 방식은 HTTP 요청에 대한 응답을 받아 브라우저 화면을 깨끗히 지우고 받은 내용을 새로 표시하는 방식인데, 내용을 지우고 다시 그리면 브라우저의 깜박임이 생기게 된다. 이러한 깜박임 없이 필요한 부분만 다시 그리는 상호작용 방식의 수요가 생겼다.

이러한 상호작용을 구현하기 위해 Pooling, Long Pooling, Streaming 등 다양한 방식을 사용했지만 요청을 보내고 응답을 보내는 **단방향 메시지 교환 규칙을 준수**하였기 때문에 상호작용하는 웹페이지를 구현하는 것은 매우 어려웠다.

이보다 쉽게 구현하기 위해 **브라우저와 서버 간 양방향 메시지 송수신 규칙**이 필요했고 이것이 WebSocket이다.

> **Socket.io**

`socket.io`는 <u>서버와 브라우저의 양방향 통신을 가능하게 하는 **모듈**</u>을 말한다. WebSocket의 경우 정말 좋은 기술이지만 오래된 브라우저의 경우 지원을 하지 않는 경우가 있다. 이런 경우 socket.io는 서버와 브라우저의 종류와 버전을 파악하여 가장 적합한 기술을 선택해 양방향 통신이 가능하도록 한다.

#### References

- [WebSocket과 Socket.io - NAVER D2](https://d2.naver.com/helloworld/1336)
- [웹소켓 - 위키백과](https://ko.wikipedia.org/wiki/%EC%9B%B9%EC%86%8C%EC%BC%93)
- [웹소켓 - 모던 JavaScript 튜토리얼](https://ko.javascript.info/websocket)
- [websocket, socket.io를 이용한 양방향 통신 - zych1751](http://www.secmem.org/blog/2019/08/17/websocket-socketio/)
- [10.5 Node.js(Express)와 Socket.io - PoiemaWeb](https://poiemaweb.com/nodejs-socketio)

---

## #20

#### IPv4와 IPv6 차이를 설명해주세요.

IPv4와 IPv6는 **인터넷 프로토콜(IP)의 버전**을 말하며, IPv4는 IP의 4번째 버전, IPv6는 IP의 6번째 버전을 말한다. 이 때 인터넷 프로토콜은 호스트 간 패킷 교환 네트워크에서 패킷(Packet) 혹은 데이터그램(Datagram)으로 불리는 정보를 주고받는데 사용하는 프로토콜을 말한다.

<div align="center">
<img src="../images/penguin/ipv4-ipv6.png" width="80%"/>
</div>
<br/>

`IPv4`는 헤더에 options이 존재하고, fragmentation/reassembly 기능을 제공해 MTU(Maximum Transport Unit)을 넘는 큰 데이터그램을 쪼개 전송을 하고 도착지에서 재조합을 한다. 또한 checksum 비트도 존재하여 매 라우터마다 checksum 비트를 갱신한다.

반면 `IPv6`는 빠른 속도를 위해 fragmentation/reassembly 기능을 제공하지 않으며, 데이터그램의 우선순위를 설정할 수 있는 priority 비트가 존재한다.

#### References

- [Chapter 4. Network Layer - Computer Networking: A Top-Down Approach](http://www.yes24.com/Product/Goods/24320296?OzSrank=2)

---

## #21

#### MAC Address가 무엇인가요?

`MAC 주소(Media Access Control Address)`는 Data Link Layer에서 통신을 위해 **네트워크 인터페이스에 할당한 식별자**를 말한다. 즉, 모든 네트워크 장비는 자신의 MAC 주소가 있으며 주소는 장비 제조업체가 할당한다. MAC 주소는 물리적 주소(Physical Address)라고 불리기도 한다.

#### References

- [MAC 주소 - 위키백과](https://ko.wikipedia.org/wiki/MAC_%EC%A3%BC%EC%86%8C)

---

## #22

#### 라우터와 스위치, 허브의 차이를 설명해주세요.

> 여기서의 네트워크는 LAN(Local Area Network)를 말합니다.

`라우터(Router)`는 **네트워크 사이를 연결하는 장치**로, 최종 도착지의 네트워크에 도착할 수 있도록 적절한 경로를 설정하여 패킷을 전송한다.

`스위치(Switch)`는 **네트워크 내에서 패킷을 전송하는 장치**를 말한다. 스위치로 요청이 들어오면 IP 주소에 대응되는 MAC 주소를 찾아 해당 MAC 주소로 패킷을 전송한다. 만약 IP 주소에 대응되는 MAC 주소가 없다면 허브처럼 브로드캐스트 방식으로 패킷을 전송하고 IP 주소와 MAC 주소를 대응시킨 테이블을 갱신시킨다.

`허브(Hub)`는 **여러 기기를 연결하여 네트워크를 만들어주는 장치**로, 패킷을 받으면 연결된 모든 기기에 패킷을 전송한다.

#### References

- [허브, 라우터, 공유기, 스위치의 개념과 차이점 - Easy is Perfect](http://melonicedlatte.com/network/2019/12/21/154500.html)
- [네트워크 스위치와 허브, 라우터는 어떻게 다른 걸까 - IT WORLD](https://www.itworld.co.kr/news/167585)
- [라우터 그리고 스위치 - HelloWorld](https://server-engineer.tistory.com/582)

---

## #23

#### SMTP가 무엇인가요?

`SMTP(Simple Mail Transfer Protocol)`은 **인터넷에서 이메일을 보내기 위해 사용하는 TCP/IP 프로토콜**을 말한다. 사용하는 TCP Port 번호는 25번이다.

SMTP는 다음의 명령어를 사용하여 메일을 주고 받는다.

- MAIL 명령: 주소 반환 확립
- RCPT 명령: 메시지 수신자 확립
- DATA 명령: 메시지 텍스트의 첫 신호를 제공

#### References

- [간이 우편 전송 프로토콜 - 위키백과](https://ko.wikipedia.org/wiki/%EA%B0%84%EC%9D%B4_%EC%9A%B0%ED%8E%B8_%EC%A0%84%EC%86%A1_%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C)

---

## #24

#### 노트북으로 `www.google.com`에 접속을 했습니다. 요청을 보내고 받기까지의 과정을 자세히 설명해주세요.

> **1단계**

웹 사이트에 접속하기 위해서는 **노트북의 IP주소, 1-hop 라우터의 IP 주소, DNS 서버 주소**가 필요하다. 이를 알아 내기 위해 DHCP query가 담긴 IP 데이터그램을 1-hop 라우터에게 전송한다. DHCP 서버가 내장된 라우터가 노트북의 IP주소, 자신의 IP주소, DNS 서버의 IP주소를 답은 DHCP ACK를 다시 노트북에게 전송한다.

- DNS란 **D**omain **N**ame **S**ystem의 약자로 `www.google.com`과 같은 도메인 주소를 IP 주소로 바꿔주는 시스템을 말한다.
- DHCP 서버는 보통은 라우터에 DHCP 서버가 내장되어 있으며 DHCP 서버에 연결된 클라이언트에게 자동적으로 IP주소를 할당한다.

> **2단계**

DNS 서버에 DNS query를 보내기 전에 **1-hop 라우터의 MAC 주소**가 필요하므로 ARP query를 브로드캐스트 방식으로 전송하여 router의 MAC주소를 알아낸다.

- ARP란 **A**ddress **R**esolution **P**rotocol의 약자로, MAC 주소와 IP 주소를 1:1 매핑하기 위해 사용된다.

> **3단계**

`www.google.com`에 요청을 보내기 위해서는 `www.google.com`의 IP주소가 필요하므로, DNS query가 담긴 IP 데이터그램을 DNS 서버에 전송하고 `www.google.com`의 IP 주소를 클라이언트인 노트북에게 전송한다.

> **4단계**

TCP 소켓을 생성하고 3-way handshake로 연결을 생성한다. HTTP 요청을 보내고 응답을 받아 브라우저에 렌더링을 하면 Google 웹페이지를 브라우저에서 확인할 수 있다.

#### References

- [Chapter 6.7. Life of a web request - Computer Networking: A Top-Down Approach](http://www.yes24.com/Product/Goods/24320296?OzSrank=2)
- [ARP 쉽게 이해하기 - 네트워크 엔지니어 환영의 AWS 기술블로그](https://aws-hyoh.tistory.com/entry/ARP-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0)

---

## #25

#### 여러 네트워크 topology에 대해 간단히 소개해주세요.
##### 네트워크 토폴로지
컴퓨터끼리 정보를 교환하고 교류하는 형태를 의미하는 네트워크에서 토폴로지는 컴퓨터들의 특정한 망구성 방식을 의미한다.

하나의 네트워크 구성 방식을 보더라도, 노드와 링크와 같은 물리적 배치로 구분하는 **물리적 토폴로지**와 노드 간의 데이터 흐름으로 구분하는 **논리적 토폴로지**로 네트워크 구성을 각각 판단할 수 있다.


##### Star
중앙에 위치한 메인 노드를 통해 다른 노드와 소통할 수 있는 구조

장점
- 장애 발견이 쉽고 관리가 용이함

단점
- 메인 노드에 장애가 발생하면 전체 네트워크 사용 불가능

<div align='center'>
    <img src='../images/heath/star_topology.png' height='250px '/>
</div>
<br/>

##### Bus
버스라는 공통 배선을 통해 노드들이 연결되어 있어서, 한 노드의 신호가 모든 노드에 전달됨 (타겟 노드만 신호에 반응을 하고 다른 노드는 무시함)

장점
- 노드 추가 및 삭제가 용이
- 한 노드에 장애가 발생해도 다른 노드에 영향을 주지 않음

단점
- 공통 배선의 크기(대역폭)가 제한되어 있으므로 배선에 과부하가 걸릴 경우 네트워크 성능 저하

<div align='center'>
    <img src='../images/heath/bus_topology.png' height='250px '/>
</div>
<br/>


##### Ring
각 노드가 양 옆으로 연결된 원형 구조, 단방향으로 신호가 전달됨

장점
- 단방향 구조로 단순하고, 중간에 있는 노드들이 증폭기의 역할을 해줌 (거리 제약 적어짐)

단점
- 노드 추가 및 삭제가 어려움

<div align='center'>
    <img src='../images/heath/ring_topology.png' height='250px '/>
</div>
<br/>

##### Mesh
다수의 노드가 서로 연결된 형태 (모두 연결되면 완전 연결형, 일부만 연결되면 부분 연결형)

장점
- 노드의 장애에 영향받지 않으며 유연한 대처가 가능함, 안정적임

단점
- 망 구축 비용이 크고, 노드 추가에도 비용이 많이 듬

<div align='center'>
    <img src='../images/heath/mesh_full_topology.png' height='250px '/>
</div>
<br/>

<div align='center'>
    <img src='../images/heath/mesh_part_topology.png' height='250px '/>
</div>
<br/>

#### References
- [네트워크 토폴로지 정의 및 종류 - 브릭봇](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=brickbot&logNo=220418950837)
- [토폴로지 - 풍뎅아 공부하자](https://sungks.tistory.com/268)
---

## #26

#### subnet mask에 대해서 설명해주세요.

##### IP 주소와 서브네팅 (subnetting)
IPv4 의 경우 2^(8*4=32) 의 숫자로 주소를 표현하고, 이를 국가, 회사 등 잘게 나눠 어느 영역을 쓰게할 것인지 결정한다.

한정된 자원이기 때문에 효율적으로 노드에 주소를 할당하는게 중요하다. 이를 위해 IP 를 쪼개는, 네트워크 파트 + 호스트 파트로 구성하는 서브네팅을 활용한다.

기본적으로 IP 주소에 따라 5 개의 클래스로 구분된다. 각 클래스에 따라 네트워크 파트와 호스트 파트가 정해진다.

<div align='center'>
    <img src='../images/heath/network_class.png' height='250px '/>
</div>
<br/>

위와 같은 클래스 구조와 더불어 더욱 효율적인 서브네팅을 위해서 사용하는 방법이 서브넷 마스크이다.

##### 서브넷 마스크 (subnet mask)
할당된 IP 주소는 기본적으로 네트워크 파트와 호스트 파트가 정해져있다. 

효율적인 주소 관리를 위해 내부적으로 호스트 파트를 새로운 네트워크 파트와 호스트 파트로 나눌 수 있다. 이 때 서브넷 마스크를 활용할 수 있다.

만약 C 클래스인 192.12.16.1 IP, 255.255.255.0 서브넷 마스크(호스트 파트)가 할당되었을 때 마지막 8 비트를 1111 0000 으로 구분했다면, 4 비트만큼의 네트워크 파트 (그룹) 4 비트만큼의 호스트 (멤버) 를 할당할 수 있다. 이렇게 된다면 동일 네트워크 간에는 커뮤니케이션이 자유롭지만, 다른 네트워크 간에는 라우터를 거쳐야 커뮤니케이션을 할 수 있다.

#### References
- [IP 주소 및 서브넷 마스크 - 보안전문가가 되자](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=hatesunny&logNo=220790654612)
- [[Network] IP주소 클래스(A,B,C class)란? Limky 삽질 블로그](https://limkydev.tistory.com/168?category=954021)
- [서브네팅 목적 및 개념 - 트레비스의 IT 라이프](https://travislife.tistory.com/53)

---

## #27

#### data encapsulation이 무엇인가요?
data encapsulation 은 데이터를 보내는 송신측에서 데이터를 생성하는 방법으로, 네트워크 계층에서 상위 계층에서부터 하위 계층으로 내려올 때마다 각 계층의 헤더를 붙여 보내는 데이터로 만들어낸다.

반대로 데이터를 받는 수신측에서는 데이터를 받은 후에 계층을 거슬러 올라가면서 헤더를 떼내며 데이터를 파악한다.

<div align='center'>
    <img src='../images/heath/network_encapsulation.png' height='250px '/>
</div>
<br/>

#### References
- [[network] 캡슐화 & 역캡슐화 (encalsulation & decapsulation) - CHAEN](https://ychae-leah.tistory.com/20)
- [[네트워크] TCP/ IP 캡슐화 - jhkang-dev](https://jhkang-tech.tistory.com/20)

---

## #28

#### DHCP를 설명해주세요.
DHCP (Dynamic Host Configuration Protocol) 는 동적으로 IP 주소나 기타 정보들을 관리해주는 프로토콜을 말한다. 관리해야하는 컴퓨터가 많고 이들의 IP 를 모두 직접 할당하고 관리하려면 상당히 복잡하고 시간이 많이들지만, DHCP 를 사용하면 이러한 문제점을 해결할 수  있다.

DHCP 는 UDP 를 사용하여 클라이언트/서버 구조로 통신한다.
그 과정은 아래와 같다.

1. DHCP discover  
: 컴퓨터가 동일 서브넷으로 브로드캐스팅(255.255.255.255) 으로 DHCP 서버를 찾음
2. DHCP offer  
: DHCP 가 사용가능한 IP 주소의 리스트를 컴퓨터에게 전달함
3. DHCP request  
: 컴퓨터가 리스트 중 하나의 IP 주소를 선택하여 서버에 전달
4. DHCP ack  
: DHCP 가 컴퓨터에게 해당 IP 주소를 허락/거절하는 메세지를 전달

##### 장점
- DHCP 서버에서 자동으로 IP 를 관리해주므로 편리함
  - IP 에 변동이 있을 때, DHCP 에만 정보를 입력하면 됨
  - 자동 할당
- 사용중인 컴퓨터에 대해서만 할당하므로 효율적임

##### 단점
- DHCP 서버에 의존하기 때문에 서버가 다운되는 경우 모든 컴퓨터에서 인터넷을 할 수 없음
- 초기 DHCP 세팅 시간 및 트래픽이 큼
- 단말 컴퓨터를 끌 경우, 완전히 주소가 release 될 때 까지 해당 IP 를 사용할 수 없음

#### References
- [DHCP 열심히 정리한 글 :) - Don't forget your time](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=hai0416&logNo=221578608161)
- [DHCP란 그 개념부터 알아보자 - 네트워크보안](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=haionvpn&logNo=40181076143)

---

## #29

#### routing protocol을 몇 가지 설명해주세요. (ex. link state, distance vector)

<div align='center'>
    <img src='../images/heath/routing.png' height='250px '/>
</div>
<br/>

패킷을 전달할 때 어느 경로로 갈지 정하는 것을 라우팅이라고 한다.

##### 라우팅 경로 고정 여부
어떤 경로로 라우팅할지를 미리 정해두냐 동적으로 정하냐에 따라 `정적 라우팅`, `동적 라우팅` 으로 구분한다.

##### 내/외부 라우팅
동적 라우팅에서 AS (Auotonomous System, 하나의 네트워크 관리자에 의해 관리되는 네트워크 집단) 를 기준으로 내부적으로 동작하냐, 외부적으로 동작하냐에 따라 `내부 라우팅` (RIP, IGRP, OSPF, EIGRP) 과 `외부 라우팅` (BGP, EGP) 으로 나눈다.

##### 라우팅 테이블 관리
동적 라우팅에서 어떤 방식으로 라우팅 테이블을 관리하느냐에 따라서도 방법이 다르다.
크게 link state, distance vector 방법이 있다.

`distance vector` 방법은 현재 위치 (단말 또는 라우터) 까지의 방향과 거리를 기록한 라우팅 테이블을 인접한 라우터들에게 전달하고 갱신한다.
메모리가 적게 들고 구성이 쉽지만, 전체 테이블 구성 시간이 길어질 수 있고 같은 경로를 반복해서 도는 루핑 문제가 발생할 수 있다. (EIGRP 는 루핑이 발생하지 않음)

`link state` 방법은 인접 테이블에 정보를 전달했으면 또 그 인접 테이블들은 이 정보를 바로 인접 테이블로 넘겨, 직접 연결되지 않은 모든 라우터들도 현재 정보를 파악할 수 있다.
정확하고 루핑 문제가 없다는 장점이 있어 대형 네트워크에서 많이 사용되지만 메모리의 소모와 cpu 로드가 많다는 단점이 있다.

#### References
- [라우팅 프로토콜(Routing Protocol) - 자비스가 필요해](https://needjarvis.tistory.com/159)
- [라우팅 프로토콜 종류 - 개발일기](https://developmentdiary.tistory.com/494)
- [라우팅 프로토콜의 종류 - 청년 고득녕](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=nackji80&logNo=221431942767)
- [디스턴스 벡터/링크 스테이트 - 이삭이의 토스트 공장](https://toastfactory.tistory.com/286)

---

## #30

#### 이더넷(ethernet)이 무엇인가요?
이더넷은 근거리 유선 통신을 위해 사용되는 네트워킹 방법으로 [CSMA/CD](https://security-nanglam.tistory.com/193)프로토콜을 사용한다.  IEEE 802.3 에 표준으로 정의되었다.

장점
- 적은 용량의 데이터를 보낼 때 성능이 좋다.
- 비용이 적고 관리가 쉽다.
- 구조가 단순하다.

단점
- 캐리어 충돌이 발생할 수 있다.
- 충돌이 발생하면 지연이 생긴다.

*CSMA/CD 방법을 간략히 말하자면 버스 구조로 통신을 하는데 캐리어라는 네트워킹 상의 신호를 감지하여 캐리어가 없으면 정보를 보내는 방식이다. 

#### References
- [[네트워크] 이더넷(Ethernet) - DevOwen](https://devowen.com/351)
- [[네트워크] 이더넷? _ Ethernet에 대하여 - 낭람](https://security-nanglam.tistory.com/192)

---

## #31

#### client와 server의 차이점을 설명해주세요.
네트워크 상에서 요청을 보내는 대상을 `client`, 요청에 응답하는 대상을 `server` 라고 한다. client 와 server 는 고정되지 않고 요청에 따라 바뀐다. 전에는 요청을 보내는 client 였어도 다음 번에는 다른 노드로부터 요청을 받으면 server 가 된다.

#### References
- [서버 클라이언트 뜻 - 오나바딩요](https://blog.naver.com/myca11/221369799273)

---

## #32

#### delay, timing(jitter), throughput 차이를 설명해주세요.
위 세가지 개념 중 delay 와 timing 은 
##### delay
하나의 데이터 패킷이 출발 지점에서 도착 지점에 도착한 시간을 의미한다.

딜레이는 
1) 전송 지연 : 장비의 전송 속도가 느려서 생기는 지연
2) 전파 지연 : 거리가 멀어서 생기는 지연
3) 노드 처리 지연 : 라우터에서 데이터 패킷 처리 등을 하며 생기는 지연
4) 큐 지연 : 패킷이 많아서 큐에 쌓여있는 동안 생기는 지연
의 합으로 계산된다.


##### timing(jitter)
delay 의 변동을 (변화량 수준) 의미한다. 같은 스위치가 아닌 경우 패킷마다 대기 시간이 달라지므로 지터가 생긴다.


##### throughput
지정된 시간동안 실제로 전송된 정보량을 의미한다. 

데이터가 지나갈 수 있는 통로의 크기인 bandwidth 와 헷갈릴 수 있는데, bandwidth 가 크더라도 실제로 전송된 정보량이 적으면 throughput 이 적은 것이다.

#### References
- [Network의 4가지 종류 - 공대생의 개발 노트](https://corona-world.tistory.com/47)
- [4. 네트워크의 delay, loss, throughput - 나도 잘 모름](https://snnchallenge.tistory.com/98)
- [[네트워크]latency, bandwidth와 throughput 개념 정리 - 코딩 세상](https://darkstart.tistory.com/141)
- [Latency Delay Jitter 의 명쾌한 비교](https://sensechef.com/1156)
---

```

```
