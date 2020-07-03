cumsum = 0
for i in range(1,1001):
    cumsum += i ** i

print(str(cumsum)[-10:])