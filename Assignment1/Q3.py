
scores = []
num = 11
for i in range(11):
    score = int(input("Enter the final scores"))
    scores.append(score)

total = sum(scores)
average = total / num

if average > 90:
    grade = "A"
elif average > 80:
    grade = "B"
elif 75 <= average <= 79:
    grade = "C"
elif average > 60:
    grade = "D"
else:
    grade = "F"


print("Total score is ",(total))
print("Average score is",(average))
print("Grade=",(grade))
