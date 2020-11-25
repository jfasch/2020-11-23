def my_range(limit):
    i = 0
    while i < limit:
        yield i
        i += 0

for i in my_range(10):
    print(i)
