N, M = map(int, input().split())
# 바구니 1번 ~ N(=5)번
# [1][2][3][4][5]

basket = []

for n in range(1, N+1): 
    basket += [n]
#print(basket)

# 예제입력 2번째 줄부터...
# 바구니 i 와 바구니 j를 바꿀 횟수 M()=4)
for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1] # 리스트 내부를 직접 교환해야 함.

# basket = [i for i in range(1, 5+1)] # for 문을 간단히 
print(*basket)