data = input().split(' ')
a = int(data[0])
b = int(data[1])
c = int(data[2])

if a == b and b == c and a == c:
    print(10000 + a*1000)

elif a == b and a != c and b != c:
    print(1000 + a*100)
elif a != b and a == c and b != c:
    print(1000 + a*100)
elif a != b and a != c and b == c:
    print(1000 + b*100)

elif a != b and a != c and b != c:
    print(max(a, b, c)*100)