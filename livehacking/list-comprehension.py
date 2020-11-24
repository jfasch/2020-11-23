for sq in [i**2 for i in range(8)]:
    print(sq)

for sq in [i**2 for i in range(8) if i%2 == 0]:
    print(sq)
