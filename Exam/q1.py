def calculate_mean(numbers):
    mean = sum(numbers) / len(numbers)
    return mean

def calculate_sum(numbers):
    totalSum = sum(numbers)
    return totalSum

def calculate_median(numbers):
    sortedNumbers = sorted(numbers)
    n = len(numbers)
    if n % 2 == 0:
        median = (sortedNumbers[n//2 - 1] + sortedNumbers[n//2]) / 2
    else:
        median = sortedNumbers[n//2]
    return median

numInputs = 10
numbers = []
for i in range(numInputs):
    number = float(input(f"Enter number {i+1}: "))
    numbers.append(number)

mean = calculate_mean(numbers)
totalSum = calculate_sum(numbers)
median = calculate_median(numbers)

print("Mean:", mean)
print("Sum:", totalSum)
print("Median:", median)
