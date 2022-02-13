def solution(N, stages):
    result = []
    length = len(stages)
    for i in range(1,N+1):
        # count 함수를 사용하자!
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count/length
        result.append((fail,i))
        # 총 도전자 수를 게속 최신화 하자
        length -= count
    
    result = sorted(result, key= lambda x : -x[0])
    
    answer = [x[1] for x in result]
    return answer