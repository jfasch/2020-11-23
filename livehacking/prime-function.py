import sys

def is_prime(number):
    if number == 1:
        return False

    candidate = 2
    while candidate < number:
        if number % candidate == 0:
            return False
        candidate += 1
    else:
        return True

number = int(sys.argv[1])
if is_prime(number):
    print(number, 'is prime')
else:
    print(number, 'is not prime')
