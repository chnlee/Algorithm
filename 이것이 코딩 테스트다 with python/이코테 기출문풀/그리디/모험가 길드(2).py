# 현재 상황에서 가장 좋아 보이는 것만을 선택하는 알고리즘이다. 현재 상황에서 가장 좋아보이는 것만을 선택하기 때문에, 정확한 답을 도출하지 못하더라도 그럴싸한 답을 도출하는 데에 도움이 된다. 하지만 코딩 테스트에서는 대부분 최적의 해를 찾는 문제가 출제되기 때문에 그리디 알고리즘의 정당성을 고민하면서 문제 해결 방안을 떠올려야 한다.

N = int(input())
_list = map(int,input().split())
count = 0
result = 0
for i in _list:
  count += 1
  if(count >= i):
    count = 0
    result +=1

print(result)