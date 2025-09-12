prime_number=[]

for x in range(2,100):
    a=True
    for i in prime_number:
        if x%i == 0:
            a=False
            break
    if a:
        prime_number.append(x)

print(prime_number)