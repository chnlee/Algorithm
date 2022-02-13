# 선택 정렬
# 매번 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞으로 두 번째 데이터와 바꾸는 과정을 반복하는 것이다.
# 시간 복잡도 O(N^2)
array = [7,5,9,0,3,1,6,2,4,8]


for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  # 간단하게 리스트 내 두 원소 위치를 변경할 수 있다.
  array[i], array[min_index] = array[min_index], array[i]

print(array)


# 삽입 정렬
# 특정한 데이터를 적절한 위치에 삽입한다는 의미이다.

for i in range(1,len(array)):
  for j in range(i,0,-1):
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break

# 퀵 정렬
# 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.

# 재귀 함수를 이용해서 퀵 정렬을 풀 수 있다. 종료 조건은 원소가 1개일 때이다.

def quickSort(array,start,end):
  if start >= end:
    return
  pivot = start
  left = start + 1
  right = end
  while left <= right:
    while left <= end and array[left] <= array[pivot]:
      left += 1
    while right > start and array[right] >= array[pivot]:
      right -= 1
    if left > right:
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
  quickSort(array,0,right-1)
  quickSort(array,right+1,end)

quickSort(array,0,len(array)-1)
print(array)

def quickSort(array):
  if len(array) <= 1:
    return array
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x> pivot]

  return quickSort(left_side) + [pivot] + quickSort(right_side)

print(quickSort(array))
# 계수 정렬
count = [0] * (max(array)+1)

for i in range(len(array)):
  count[array[i]] += 1

for i in range(len(count)):
  for j in range(count[i]):
    print(i, end = ' ')