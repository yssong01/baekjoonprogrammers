#num1, num2 = '734', '893'
#print(num1)
#print(num2)
num1, num2 = input().split()

rnum1 = num1[::-1]
rnum2 = num2[::-1]
#print(rnum1)
#print(rnum2)
sangn = max(int(rnum1), int(rnum2))
print(sangn)