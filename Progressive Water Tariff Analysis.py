households = int(input("Number of households: "))
for i in range(1, households + 1):
    usage = float(input("Water use for household " + str(i) + " (kL): "))
    if usage <= 10:
        charge = usage * 5
    elif usage <= 20:
        charge = 10 * 5 + (usage - 10) * 8
    else:
        charge = 10 * 5 + 10 * 8 + (usage - 20) * 12
    bill = charge + 30
    if usage > 25:
        bill = bill + 100
        print("Excessive usage")
    print("Household", i, "bill: Rs.", round(bill, 2))