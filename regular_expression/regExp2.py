# special sequences는 \문자로 시작한다.
import re

a = "amarshall lives in Korea, Incheon 13"
b = re.findall(r"\Amarshall", a) # \A : 문자열 문장의 시작과 매칭. r을 빼면 warning 발생

if b:
  print("Matched")
else:
  print("Not matched")

c = re.findall(r"marshall\B", a) # marshall 문자열이 뒤에 오지 않으면 매칭 : marshall 뒤에 s가 있으므로 매칭 amarshalls 도 매칭. 뒷 부분에 marshallize가 있게 되면 두개를 매칭. amarshall은 매칭이 안됨.
# print(c)

d = re.findall(r"\Bmarshall", a) # marshall 문자열이 앞에 오지 않으면 매칭 : marshall 앞에 a가 있으므로 매칭. marshalla와 같이 marshall이 앞에 오면 매칭이 안됨.
# print(d)

e = re.findall(r"\bmarshall", a) # marshall 문자열이 단어의 시작에 오면 매칭 : marshall이 단어의 시작에 있으므로 매칭. marshalla와 같이 marshall이 단어의 시작에 오지 않으면 매칭이 안됨. amarsahll은 매칭이 안됨.
# print(e)

f = re.findall(r"marshall\b", a) # marshall 문자열이 단어의 끝에 오면 매칭 : marshall이 단어의 끝에 있으므로 매칭. marshalla와 같이 marshall이 단어의 끝에 오지 않으면 매칭이 안됨. amarsahll은 매칭이 안됨.
# print(f)

g = re.findall(r"\d", a) # 숫자를 찾음
# print(g)

h = re.findall(r"\D", a) # 숫자가 아닌 것을 찾음 : 공백, 문자, 특수문자 등 포함
# print(h)

i = re.findall(r"\s", a) # 공백을 찾음
# print(i)

j = re.findall(r"\w", a) # 문자와 숫자를 찾음
# print(j)

k = re.findall(r"13\Z", a) # 문자열 문장의 끝과 매칭
# print(k)

l = re.findall(r"13$", a) # 문자열 문장의 끝과 매칭
print(l)