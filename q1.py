numbers = []
highest = 0
cluster = 0
numbers.append(int(input("Enter an integer")))
for i in range(9):
    numbers.append(int(input("Enter an integer")))
    if (numbers[i] % 2 == 1) and (numbers[i-1] % 2 == 0):
        cluster += 1
print(cluster)