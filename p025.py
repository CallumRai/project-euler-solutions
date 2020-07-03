fib = [1, 1]
over = False
ix = 2

while not over:
    ix += 1
    next = fib[-1] + fib[-2]
    fib.append(next)

    if next >= 10 ** 999:
        over = True

print(ix)
