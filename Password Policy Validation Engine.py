password = input("Enter a sample password: ")
valid = True
if len(password) < 8:
    print("Failed: password must contain at least 8 characters")
    valid = False

has_upper = False
has_lower = False
has_digit = False
has_special = False
for ch in password:
    if 'A' <= ch <= 'Z':
        has_upper = True
    if 'a' <= ch <= 'z':
        has_lower = True
    if '0' <= ch <= '9':
        has_digit = True
    if ch in "!@#$%":
        has_special = True

if not has_upper:
    print("Failed: add an uppercase letter")
    valid = False
if not has_lower:
    print("Failed: add a lowercase letter")
    valid = False
if not has_digit:
    print("Failed: add a digit")
    valid = False
if not has_special:
    print("Failed: add a special character (!@#$%)")
    valid = False
if "password" in password.lower():
    print("Failed: the word 'password' is prohibited")
    valid = False

for i in range(len(password) - 2):
    if password[i] == password[i + 1] and password[i] == password[i + 2]:
        print("Failed: three identical characters in a row")
        valid = False
        break

if valid:
    print("Password accepted")
else:
    print("Password rejected")