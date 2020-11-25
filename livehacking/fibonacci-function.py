# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# .
# .
# .

def fibonacci(limit):
    fibo_numbers = []

    first = second = 1

    fibo_numbers.append(first)
    fibo_numbers.append(second)

    while len(fibo_numbers) < limit:
        third = first + second
        fibo_numbers.append(third)
        first, second = second, third

    return fibo_numbers

for i in fibonacci(100):
    print(i)
