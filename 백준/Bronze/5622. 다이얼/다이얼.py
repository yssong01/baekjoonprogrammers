li = {'':1, 'ABC':2, 'DEF':3, 'GHI':4, 'JKL':5, 'MNO':6, 'PQRS':7, 'TUV':8, 'WXYZ':9}
#print(li[''])
#print(li['ABC'])

word = input()
#word = 'UNUCIC'
#word = 'WA'

time = 0 # 초기 시작 시간

time_step = 1  # 번호 사이, 걸리는 시간 : 1초 
for spell in word:
    #print(spell)
    for key in li:
        if spell in key:
            time += li[key] + time_step # 번호 + 1초, 숫자1을 걸려면 2초 걸림. 숫자2는 3초.
            break
    
print(time)