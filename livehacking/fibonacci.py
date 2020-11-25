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

first = second = 1

print(first)
print(second)

while True:
    third = first + second
    print(third)
    first, second = second, third
