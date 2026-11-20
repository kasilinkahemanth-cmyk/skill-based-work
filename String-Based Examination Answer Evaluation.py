key = input("Enter answer key (example ABCD): ").upper()
answers = input("Enter student answers; use - for blank: ").upper()
if len(key) != len(answers):
    print("Error: answer strings must have the same length")
else:
    correct = 0
    incorrect = 0
    unanswered = 0
    for i in range(len(key)):
        if answers[i] == "-":
            unanswered = unanswered + 1
        elif answers[i] == key[i]:
            correct = correct + 1
        else:
            incorrect = incorrect + 1
    score = correct - incorrect * 0.25
    print("Correct:", correct)
    print("Incorrect:", incorrect)
    print("Unanswered:", unanswered)
    print("Final score:", round(score, 2))