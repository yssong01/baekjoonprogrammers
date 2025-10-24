X = int(input())
N = int(input())
sum = 0
for _ in range(N):
    A, B = input().split()
    a = int(A)
    b = int(B)
    sum += a * b
if sum == X:
    print("Yes")
elif sum !=X:
    print("No")