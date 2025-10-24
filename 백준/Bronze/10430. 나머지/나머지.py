result = input().split(' ')
a = int(result[0])
b = int(result[1])
c = int(result[2])

print( (a+b)%c )
print( ((a%c)+(b%c))%c )
print( (a*b)%c )
print( ((a%c)*(b%c))%c )