subjects = int(input("Number of subjects: "))
grace_used = False
all_pass = True
for i in range(1, subjects + 1):
    mark = int(input("Marks for subject " + str(i) + " (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid mark")
        all_pass = False
        continue
    if mark >= 32 and mark < 35 and grace_used == False:
        mark = mark + (35 - mark)
        grace_used = True
        print("Grace marks applied")
    print("Final mark:", mark)
    if mark >= 35:
        print("PASS")
    else:
        print("FAIL")
        all_pass = False
if all_pass:
    print("Overall result: PASS")
else:
    print("Overall result: FAIL")