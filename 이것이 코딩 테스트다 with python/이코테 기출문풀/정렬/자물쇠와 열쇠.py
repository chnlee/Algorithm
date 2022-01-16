# 문자열 압축
# 2020 카카오 신입 공채

def rotate_key(key):
    m = len(key)
    new_key = [[0] * m for i in range(m)]
    for i in range(m):
        for j in range(m):
            new_key[j][m-1-i] = key[i][j]
    return new_key

def check(new_lock):
    length = len(new_lock) // 3
    for i in range(length,length*2):
        for j in range(length,length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0] * (n*3) for i in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
            
    for rotation in range(4):
        key = rotate_key(key)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]        
                if check(new_lock) == True:
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j] 
    return False