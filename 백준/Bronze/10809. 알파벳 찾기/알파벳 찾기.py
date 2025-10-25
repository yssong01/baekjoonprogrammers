#S = 'baekjoon'
S = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:
    result = S.find(i)
    print(result, end=' ')