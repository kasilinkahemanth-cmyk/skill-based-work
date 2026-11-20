def energy_charge(units):
    if units <= 100:
        return units * 2
    elif units <= 200:
        return 100 * 2 + (units - 100) * 3
    else:
        return 100 * 2 + 100 * 3 + (units - 200) * 5

months = int(input("Number of months: "))
previous_bill = 0
for month in range(1, months + 1):
    units = int(input("Units for month " + str(month) + ": "))
    energy = energy_charge(units)
    surcharge = energy * 0.05
    bill = energy + 50 + surcharge
    if units <= 100:
        bill = bill - 20
    print("Month", month, "bill: Rs.", round(bill, 2))
    if previous_bill > 0 and bill > previous_bill * 1.30:
        print("Unusual increase detected")
    previous_bill = bill