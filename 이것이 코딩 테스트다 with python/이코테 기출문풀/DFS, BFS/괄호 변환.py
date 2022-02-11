def balanced_string(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
# right_sting을 구현하기 위해선 count를 이용한다.
def right_string(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else: 
            if count == 0:
                return False
            count -= 1
    return True

# string은 item assignment가 불가능하므로(임의로 string의 element 값을 변경할 수 없음) string을 list로 바꾸고 join method를 이용해야한다.

def solution(p):
    answer = ''
    if len(p) == 0:
        return p
    index = balanced_string(p)
    u = p[:index + 1]
    v = p[index+1:]
    if right_string(u):
        answer = u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        new_u = list(u[1:-1])
        for i in range(len(new_u)):
            if new_u[i] == '(':
                new_u[i] = ')'
            else:
                new_u[i] = '('
        answer += ''.join(new_u)
    return answer
        