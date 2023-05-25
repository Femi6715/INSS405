grades = []
for i in range(3):
    grade = int(input(f"Enter grade for student {i+1}: "))
    grades.append(grade)

mean_grade = sum(grades) / len(grades)

if mean_grade >= 90:
    final_grade = "A"
elif mean_grade >= 80:
    final_grade = "B"
elif mean_grade >= 70:
    final_grade = "C"
elif mean_grade >= 60:
    final_grade = "D"
elif mean_grade >= 50:
    final_grade = "E"
else:
    final_grade = "F"

print("Mean Grade:", mean_grade)
print("Final Grade:", final_grade)
