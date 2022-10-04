numbers = []
highest = 0
cluster = 0
i=1
for i in range(10):
    numbers.append(int(input("Enter an integer")))
    if (numbers[i] % 2 == 0):
        cluster += 1
        if cluster > highest:
            highest = cluster
    else:
        cluster = 0
print(highest)