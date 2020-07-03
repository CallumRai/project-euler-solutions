from fractions import *

fracs = []
for i in range(10,100):
    for j in range(10,100):

        if j<=i:
            continue

        actual = i/j

        nums = []
        for a in range(2):
            nums.append(str(i)[a])
            nums.append(str(j)[a])

        if len(set(nums)) != 3:
            continue

        valid = False
        for a in range(2):
            if str(j).count(str(i)[a]) == 1 and str(i)[a] != '0':
                common = str(i)[a]
                valid = True

        if not valid:
            continue

        num = int(str(i).replace(common,''))
        den = int(str(j).replace(common,''))

        try:
            triv = num/den
        except ZeroDivisionError:
            continue

        if triv == actual:
            fracs.append([i,j])

num_prod = 1
den_prod = 1
for frac in fracs:
    num_prod *= frac[0]
    den_prod *= frac[1]

prod_frac = Fraction(num_prod, den_prod)
print(prod_frac.denominator)