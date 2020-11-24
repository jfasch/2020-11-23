import sys

number = int(sys.argv[1])

if number == 1:
    print(number, 'is not prime')
    sys.exit()

candidate = 2
while candidate < number:
    if number % candidate == 0:
        print(number, 'is not prime')
        break
    candidate += 1
else:
    print(number, 'is prime')
