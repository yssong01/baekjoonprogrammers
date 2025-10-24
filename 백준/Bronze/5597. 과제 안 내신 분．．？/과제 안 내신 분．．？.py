n = 30
tot = set(range(1,n+1))
#print(tot)

m = 28
attend = []
for _ in range(1,m+1):
    attend.extend(map(int, input().split()))
#print(attend)

absence = sorted(tot - set(attend))
print(*absence)