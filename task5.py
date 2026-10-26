n = int(input("Enter number of rows: "))

if n < 1 or n > 20:
    print("Enter a number between 1 and 20")
else:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
