import random

i = 0
while i < 100:
    rnd = random.randrange(0, 1001)
    if rnd == 42:
        break
    i += 1
else:
    print('nix nadel im heuhaufen')
