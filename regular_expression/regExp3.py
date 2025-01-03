import re

a = "marshall lives in Korea, Incheon 13 12:59 234"
b = re.findall("[img]", a) # i, m, g 중 하나라도 있으면 매칭
# print(b)

c = re.findall("[a-c]", a) # a부터 z까지 중 하나라도 있으면 매칭 : [a-zA-z0-9 ] - 대문자, 소문자, 숫자, 공백 중 하나라도 있으면 매칭
# print(c)

d = re.findall("[^a-zA-Z]", a) # : [^] - ^가 대괄호 안에 있으면 not을 의미. 대괄호 안에 있는 문자를 제외한 나머지 문자를 매칭
# print(d) # [' ', ',', '1', '3'] - 대문자, 소문자를 제외한 나머지 문자를 매칭

e = re.findall("[0-9][0-9]", a) # [0-9] - 숫자 중 하나라도 있으면 매칭 : 숫자 두개 묶 찾음
# print(e) # ['12', '59', '23'] - 숫자 두개 묶음을 찾음 [0-9][0-9][0-9] : 숫자 세개 묶음을 찾음

f = re.search(r"\s", a) # \s - 공백 문자를 매칭 : 객체를 반환
# print(f)

g = re.search(r"live", a)

# span 위치 출력
# print(g.start())
# print(g.end())

# <re.Match object; span=(8, 9), match=' '> 8, 9번째 인덱스에 공백 문자가 있음

h = re.split(r"\s", a, 1) # \s - 공백 문자를 기준으로 문자열을 나눔 : 3번 파라미터는 나눌 횟수, 나누는 기준은 첫번째 공백 문자
# print(h)

i = re.sub(r"\s", ":", a) # \s - 공백 문자를 :로 대체
print(i)