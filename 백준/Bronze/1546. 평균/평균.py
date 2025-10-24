N = int(input())
#print(N)

li = list(map(int, input().split()))
#print(li)

max_point = max(li)
#print(max_point)

li = [(i / max_point)*100 for i in li]
#print(li)

avg = sum(li) / N
print(avg)