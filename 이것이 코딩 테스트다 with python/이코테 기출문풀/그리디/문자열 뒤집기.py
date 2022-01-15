# 1로 시작한다면, 1->0으로 바뀌는 시점에 count += 1
# 0으로 시작한다면, 0 -> 1로 바뀌는 시점에 count +=1
 
S = input()
start = int(S[0])
count = 0
if start == 0:
  for i in range(len(S)-1):
    num1 = int(S[i])
    num2 = int(S[i+1])
    if num1 == 0:
      if num2 ==1:
        count += 1
  print(count)
else:
  for i in range(len(S)-1):
    num1 = int(S[i])
    num2 = int(S[i+1])
    if num1 == 1:
      if num2 ==0:
        count += 1
  print(count)


#Answer
data = input()
count0 = 0
count1 = 0
if data[0] =='1':
  count0 += 1
else:
  count1 += 1
for i in range(len(data)-1):
  if data[i] != data[i+1]:
    if data[i+1] =='1':
      count0 += 1
    else:
      count1 += 1
print(min(count0,count1))