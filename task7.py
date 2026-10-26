key = ["A", "B", "C", "D", "A"]
answers = []

for i in range(len(key)):
    answer = input("Enter answer for question " + str(i + 1) + ": ")
    answers.append(answer.strip().upper())

correct = 0
wrong = 0
unanswered = 0

for i in range(len(key)):
    if answers[i] == "":
        unanswered += 1
    elif answers[i] == key[i]:
        correct += 1
    else:
        wrong += 1

score = correct * 2 - wrong * 0.5

print("Correct answers:", correct)
print("Wrong answers:", wrong)
print("Unanswered:", unanswered)
print("Final score:", score, "out of", len(key) * 2)
