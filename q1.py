
# ******************************
# Make your Code
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###

numbers = []
cluster = 1
numbers.append(int(input("Enter an integer")))
i=1
for i in range(9):
    numbers.append(int(input("Enter an integer")))
    if (numbers[i] % 2 == 0) and (numbers[i-1] % 2 == 0):
        cluster += 1
print(cluster)