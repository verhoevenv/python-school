from random import random, uniform, randint, choice

print("random()")
for i in range(10):
	print(random())

print()
print("uniform(-5, 5)")
for i in range(10):
	print(uniform(-5, 5))

print()
print("randint(1, 10)")
for i in range(10):
	print(randint(1, 10))

print()
print("choice(['a', 'b', 'c'])")
for i in range(10):
	print(choice(['a', 'b', 'c']))
