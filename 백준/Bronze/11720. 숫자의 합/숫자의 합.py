N = int(input()) # = 문자열수
text = input()

sum = 0
for i in range(N):
    num = int(text[i])
    sum += num
print(sum)