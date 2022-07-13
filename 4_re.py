import re

p = re.compile("ca.e")
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (0) | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, destinaton (0) | fade (x)
# $ (se$) : 문자열의 끝 > case, base (0) | face (x)

def print_match(m):
  if m:
    print(m.group())
  else:
    print("매칭되지 않음")

m = p.match("caffe")
# print(m.group()) # 매치되지 않으면 에러가 발생

m = p.match("careless") # match : 주어진 문자열이 처음부터 일치하는지 확인
print_match(m)
# print(m.group)