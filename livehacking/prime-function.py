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

