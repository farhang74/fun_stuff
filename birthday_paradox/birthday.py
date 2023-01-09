peaple = 60

prob = 1
for person in range(1, peaple):
    d = (365 - person) / 365
    prob = d * prob

print(1 - prob)