data = input().split()
h = int(data[0])
m = int(data[1])

dh, dm = [-0,-45]

h = h + dh
m = m + dm

if m >= 0:
    h = h
    m = m
elif m < 0:
    if h - 1 >= 0:
        h = h - 1
        m = m + 60
    elif h - 1 < 0:
        h = h -1 + 24
        m = m + 60

print(h, m)