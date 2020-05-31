# 조건에 맞게 neverland() 함수를 만들어 보세요
def neverland(q):
    best =  q.pop(2)
    q.sort()
    q.insert(0, best)
    return q
    
# 대기 시간이 다음과 같을 때 엘리스 토끼가 놀이 기구를 타는 순서를 확인해 보세요
q = [30, 10, 20, 50, 40, 60]
print(neverland(q))
