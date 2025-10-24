data = 10
div = 42

num = [int(input()) for _ in range(1,data+1)]
#print(num)

li = [num[i] % div for i in range(data)]
#print(li)

result = set(li)
#print(result)

print(len(result))