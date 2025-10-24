li = []
while True:
    try:
        li.extend(map(int, input().split()))
    except:
        break

print(max(li))
print(li.index(max(li))+1)