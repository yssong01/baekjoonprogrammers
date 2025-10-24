N, X = map(int, input().split())
# li = input().split()
# print(N, X)
# print(li)

a = list(map(int, input().split()))
# print(a)
for i in range(N):
    if a[i] < X:
        print(a[i], end=' ')