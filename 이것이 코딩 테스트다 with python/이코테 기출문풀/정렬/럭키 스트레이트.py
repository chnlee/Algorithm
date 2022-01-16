N = input()
length = len(N)
half_length = length//2
result1 = 0
for i in range(half_length):
  num1 = int(N[i])
  result1 += num1
result2 = 0
for j in range(half_length,length):
  num2 = int(N[j])
  result2 += num2

if result1 == result2:
  print("LUCKY")
else:
  print("READY")
# 이코테 ANSWER
# N = input()
# length = len(N)
# half_length = length//2
# result = 0
# for i in range(half_length):
#   num1 = int(N[i])
#   result1 -= num1

# for j in range(half_length,length):
#   num2 = int(N[j])
#   result1 += num2

# if result1 == 0:
#   print("LUCKY")
# else:
#   print("READY")