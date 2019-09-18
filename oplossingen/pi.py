from random import random

attempts = 1000000
hits = 0

for i in range(attempts):
    x = random()
    y = random()
    if x*x + y*y < 1:
        hits = hits + 1

print(4 * hits / attempts)
