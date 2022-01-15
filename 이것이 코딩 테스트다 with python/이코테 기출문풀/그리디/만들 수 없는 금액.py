# 주어진 금액으로 목표하는 값을 만들 수 있느냐 없느냐에 초점을 맞춘다.
# 1부터 target -1까지의 모든 금액을 만들 수 있다. 
# 만약 target 금액을 만들 수 있다면, target 값을 업데이트하는 방식을 이용한다.

n = int(input())
data = list(map(int,input().split()))
data.sort()

target = 1
for i in data:
  if target < i :
    break
  target += i

print(target)