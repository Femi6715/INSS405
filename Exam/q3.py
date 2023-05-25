import random

randomIntegers = []
for _ in range(100):
    randomInt = random.randint(1, 100)
    randomIntegers.append(randomInt)

oddNumbers = [num for num in randomIntegers if num % 2 != 0]

print("Random Integers:", randomIntegers)
print("Odd Numbers:", oddNumbers)

