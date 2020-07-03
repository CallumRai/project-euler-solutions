i = 1
exceed = False

while not exceed:
    if len(str(i*9**5))>i:
        i+=1
    else:
        exceed = True

sum_power = []
for j in range(10,10**i):
    num = str(j)

    cumsum = 0
    for c in range(len(num)):
        cumsum += int(num[c])**5

    if cumsum == j:
        sum_power.append(j)

print(sum(sum_power))