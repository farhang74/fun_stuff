import decimal
def sequence(c):
    z = 0
    while True:
        yield z
        z = z ** 2 + c

epsilon = 0.00000001

for n, z in enumerate(sequence(c=0.25 + epsilon)):
    if n >= 10000000000000000 or z > 2:
        print(n)
        break