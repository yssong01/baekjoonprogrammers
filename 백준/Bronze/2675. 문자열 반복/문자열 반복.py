#T = 1
T = int(input())

R = ''
S = ''
for _ in range(T):
    R, S = input().split()
    R = int(R)
    #print(R)
    #print(S)

    repstr = ''
    for i in S:
        #print(i)
        repstr = repstr + i*R # 문자열 반복 : 'S'*2 = 'SS'
    print(repstr) 