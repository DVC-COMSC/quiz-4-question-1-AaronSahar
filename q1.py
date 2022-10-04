numbers = []
highest = 0
cluster = 0
for i in range(10):
    numbers.append(int(input("Enter an integer")))
    if i==0:
        if (numbers[i] % 2 == 0):
            cluster += 1
    if i>0:
        if (numbers[i] % 2 == 0) and (numbers[i-1] % 2 == 1):
            cluster += 1
print(cluster)