marks = []

for i in range(3):
    score = float(input("Enter exam " + str(i + 1) + " marks: "))

    if score < 0 or score > 100:
        print("Invalid marks")
        break

    marks.append(score)

if len(marks) == 3:
    average = sum(marks) / len(marks)

    print("Average marks:", round(average, 2))
    print("Improvement:", marks[2] - marks[0])

    if average >= 75:
        print("Performance: Excellent")
    elif average >= 50:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")
