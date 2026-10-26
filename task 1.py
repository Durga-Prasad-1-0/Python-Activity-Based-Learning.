total_classes = int(input("Enter total classes held: "))
attended = int(input("Enter classes attended: "))
required = float(input("Enter required attendance percentage: "))

if total_classes <= 0 or attended < 0 or attended > total_classes:
    print("Invalid attendance details")
elif not 0 < required <= 100:
    print("Invalid required percentage")
else:
    percentage = attended / total_classes * 100
    print("Current attendance:", round(percentage, 2), "%")

    future = 0
    while (attended + future) / (total_classes + future) * 100 < required:
        future += 1

    print("Additional classes required:", future)
