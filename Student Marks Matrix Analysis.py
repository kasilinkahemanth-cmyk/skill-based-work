students = int(input("Number of students: "))
names = []
marks = []
for i in range(students):
    name = input("Student name: ")
    row = []
    for j in range(3):
        mark = int(input("Mark for subject " + str(j + 1) + ": "))
        row.append(mark)
    names.append(name)
    marks.append(row)

for i in range(students):
    total = 0
    for j in range(3):
        total = total + marks[i][j]
    print(names[i], "total:", total)

top_index = 0
top_total = 0
for i in range(students):
    total = 0
    for j in range(3):
        total = total + marks[i][j]
    if i == 0 or total > top_total:
        top_total = total
        top_index = i
if students > 0:
    print("Top performer:", names[top_index])

for subject in range(3):
    total_marks = 0
    for student in range(students):
        total_marks = total_marks + marks[student][subject]
    if students > 0:
        average = total_marks / students
        print("Subject", subject + 1, "average:", round(average, 2))
        if average < 40:
            print("Low average in subject", subject + 1)