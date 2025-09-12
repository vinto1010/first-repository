import random
profit = [random.randint(1,10000000) for x in range(1000)]

maximum=0
for x in profit:
    if x>maximum:
        maximum = x

print(x)