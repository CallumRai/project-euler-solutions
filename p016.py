num = str(2**1000)

cumsum = 0
for i in range(len(num)):
    cumsum += int(num[i])

print(cumsum)