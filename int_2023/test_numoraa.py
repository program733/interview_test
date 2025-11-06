sig1 = [1, 2, 3, 4]
sig2 = [5, 6, 7, 8]
choser = [1, 2, 1, 2]

#output = [1, 6, 3, 8]


result = []
temp = 0
for i in choser:
    if i == 1:
        result.append(sig1[temp])
    else:
        result.append(sig2[temp])
    temp +=1

print(result)
