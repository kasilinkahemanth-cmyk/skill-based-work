count = int(input("Number of transactions: "))
threshold = 10000
ids = []
amounts = []
for i in range(count):
    transaction_id = input("Transaction ID: ")
    amount = float(input("Amount: "))
    suspicious = False
    for j in range(len(ids)):
        if ids[j] == transaction_id:
            print("Duplicate transaction ID detected")
            suspicious = True
    if amount > threshold:
        print("Amount exceeds threshold")
        suspicious = True
    if suspicious:
        print("Suspicious entry:", transaction_id, "Rs.", amount)
    ids.append(transaction_id)
    amounts.append(amount)
print("Transactions checked:", count)