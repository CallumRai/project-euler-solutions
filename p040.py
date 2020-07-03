champ = ''

for i in range(1,1000001):
    champ += str(i)

exp = 1
for i in range(7):
    exp *= int(champ[10**i - 1])

print(exp)