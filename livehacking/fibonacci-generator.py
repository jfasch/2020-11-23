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

def fibonacci():
    first = second = 1

    yield first
    yield second

    while True:
        third = first + second
        yield third
        first, second = second, third

for i in fibonacci():
    print(i)
