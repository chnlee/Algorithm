S = input()
_list = []
result = []
count = 0
for i in S:
  num1 = ord(i)
  if num1 >= 65:
    _list.append(num1)
  else:
    count += int(i)
_list.sort()

for i in _list:
  num2 = chr(i)
  result.append(num2)
# 0이 아닐경우 삽입해야함
if count != 0:
  result.append(count)

for i in result:
  print(i,end = '')

# 답
# data = input()
# result = []
# value = 0
# for x in data:
#   if x.isalpha():
#     result.append(x)
#   else:
#     value += int(x)

# if value != 0:
#   result.append(value)

# print(''.join(result)) 