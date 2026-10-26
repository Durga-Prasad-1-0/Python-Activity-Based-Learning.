days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
prepared = [100, 120, 110, 90, 130]
served = [90, 100, 105, 70, 115]

limit = float(input("Enter acceptable wastage percentage: "))

if not 0 <= limit <= 100:
    print("Invalid wastage limit")
else:
    total_waste = 0
    total_prepared = 0

    for i in range(len(days)):
        waste = prepared[i] - served[i]
        percentage = waste / prepared[i] * 100

        total_waste += waste
        total_prepared += prepared[i]

        print("\nDay:", days[i])
        print("Leftover meals:", waste)
        print("Wastage percentage:", round(percentage, 2), "%")

        if percentage > limit:
            print("Warning: Excessive food waste")
        else:
            print("Wastage within limit")

    overall = total_waste / total_prepared * 100
    print("\nTotal meals wasted:", total_waste)
    print("Overall wastage:", round(overall, 2), "%")
