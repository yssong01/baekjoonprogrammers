N, M = map(int, input().split())

basket = []
for n in range(1, N+1): 
    basket += [n]
#print(basket)

for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = basket[i-1:j][::-1] # basket[i-1:j] 의 역순

print(*basket)