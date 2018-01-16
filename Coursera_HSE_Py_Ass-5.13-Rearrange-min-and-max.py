l = list(map(int, input().split()))
minT = l[0]
maxT = l[0]
maxI = 0
minI = 0
for i in range(0, len(l)):
    if minT > l[i]:
        minT = l[i]
        minI = i
for i in range(0, len(l)):
    if maxT < l[i]:
        maxT = l[i]
        maxI = i
t = l[maxI]
l[maxI] = l[minI]
l[minI] = t
print(' '.join(map(str, l)))
