T = int(input())

for _ in range(T):
    word = input()
    first = word[0]
    #last = word[len(word)-1] # word[-1] 과 같음
    last = word[-1]
    
    print(first+last)