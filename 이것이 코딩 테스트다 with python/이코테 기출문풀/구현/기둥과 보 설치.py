# 기둥과 보 설치
def _possible(answer):
  for x,y,structure in answer:
    if structure == 0:
      if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
        continue
      return False
    elif structure == 1:
      if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
        continue
      return False
  return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, structure, operate = frame
        if operate == 0:
            answer.remove([x,y,structure])
            if not _possible(answer):
                answer.append([x,y,structure])
        if operate == 1:
            answer.append([x,y,structure])
            if not _possible(answer):
                answer.remove([x,y,structure])
    return sorted(answer)
