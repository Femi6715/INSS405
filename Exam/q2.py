import random

def sortNumbers(numbers):
    sortedNumbers = sorted(numbers)
    return sortedNumbers

randomNumbers = []
for _ in range(100):
    randomNumber = random.randint(1, 1000)
    randomNumbers.append(randomNumber)

sortedNumbers = sortNumbers(randomNumbers)

print("Random Numbers:", randomNumbers)
print("Sorted Numbers:", sortedNumbers)
