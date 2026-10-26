students = ["Ravi", "Sita", "Arun"]
subjects = ["Python", "Maths", "English"]

marks = [
    [80, 75, 90],
    [90, 85, 95],
    [70, 80, 75]
]

averages = []

for i in range(len(students)):
    average = sum(marks[i]) / len(marks[i])
    averages.append(average)
    print(students[i], "Average:", round(average, 2))

top_index = averages.index(max(averages))
print("Top student:", students[top_index])

for j in range(len(subjects)):
    total = 0

    for i in range(len(students)):
        total += marks[i][j]

    print(subjects[j], "Average:", round(total / len(students), 2))
