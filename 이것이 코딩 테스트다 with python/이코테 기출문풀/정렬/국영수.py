N = int(input())
students = []
for i in range(N):
  name, kor, eng, mat = input().split()
  students.append((name,int(kor),int(eng),int(mat)))

ans = sorted(students, key = lambda x :(-x[1],x[2],-x[3],x[0]))

for i in range(len(ans)):
  print(ans[i][0])