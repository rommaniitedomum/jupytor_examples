# 정규표현식이란 문자열을 처리하는 방법 중의 하나로 특정한 조건의 문자를 '검색'하거나 '치환'하는 과정을 매우 간편하게 처리할 수 있도록 하는 수단이다.

import re

a = "I live in Korea, Incheon 13"
b = re.search("^I.*Incheon$", a) # ^I로 시작하고 Incheon으로 끝나는 문자열 검색
# print(type(b))
# print(b)

if b:
  print("매칭되었습니다.")
else:
  print("매칭되지 않았습니다.")

# findall() 함수는 매칭되는 모든 문자열을 리스트 형태로 리턴한다.
# search() 함수는 매칭되는 첫번째 문자열만 리턴한다.
# split() 함수는 매칭되는 문자열을 기준으로 문자열을 나누어 리스트 형태로 리턴한다.
# sub() 함수는 매칭되는 문자열을 다른 문자열로 치환한다.

c = re.findall("[a-dA-Z0-9]", a)
# d = re.findall("\d", a) # 숫자만 추출(digits)
e = re.findall("K...a", a) # K로 시작하고 a로 끝나는 5글자 문자열 추출
# print(c)
# print(d)
# print(e)

f = re.findall("K.*a", a) # K로 시작하고 a로 끝나는 문자열 추출 : zero or more
g = re.findall("Kore.+a", a) # Kore와 a 사이에 어떤 문자가 1개 이상 있는 문자열 추출 Korema, koremoa... 등으로 수정하면 찾을 수 있음 : one or more
h = re.findall("Kore.?a", a) # zero or one : Korea, Koreaa 등으로 수정하면 찾을 수 있음 : Koreaaaaa는 찾을 수 없음
# print(f)
# print(g)
# print(h)
i = re.findall("K.{3}a", a)
j = re.findall("live|Korea", a) # live 또는 Korea가 있는 문자열 추출
# print(i)
print(j)
