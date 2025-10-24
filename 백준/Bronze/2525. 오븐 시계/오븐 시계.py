start_time = input().split(' ')
h = int(start_time[0])
m = int(start_time[1])

cooking_time = input()
dm = int(cooking_time)


total_mins = h*60 + m + dm
#print(total_mins)
#print(total_mins // 60)

hour = (total_mins // 60) % 24 # hour가 24시 기준으로 순환
minute = total_mins % 60 # minute이 60분 기준으로 순환
print(hour, minute)