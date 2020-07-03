fib = [1,2]
lower = True

while lower:
    new_term = fib[-1] + fib[-2]

    if new_term > 4000000:
        lower = False
        break

    fib.append(new_term)

even_fib = []

for term in fib:
    if term % 2 == 0:
        even_fib.append(term)

print(sum(even_fib))