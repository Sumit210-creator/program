name = input("Enter your name: ").strip()
print(f"Hello, {name or 'Stranger'}!")

password1 = input("Enter a new password: ")
password2 = input("Confirm your password: ")
if password1 == password2:
    print("Password Set!")
else:
    print("Passwords do not match.")

password1 = input("Enter a password (8-12 characters): ")
if 8 <= len(password1) <= 12:
    password2 = input("Confirm your password: ")
    if password1 == password2:
        print("Password Set!")
    else:
        print("Passwords do not match.")
else:
    print("Password must be 8-12 characters long.")

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password1 = input("Enter a password (8-12 characters): ")
if 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
    password2 = input("Confirm your password: ")
    if password1 == password2:
        print("Password Set!")
    else:
        print("Passwords do not match.")
else:
    print("Invalid password.")

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    password1 = input("Enter a password (8-12 characters): ")
    if 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
        password2 = input("Confirm your password: ")
        if password1 == password2:
            print("Password Set!")
            break
        else:
            print("Passwords do not match.")
    else:
        print("Invalid password.")

for i in range(13):
    print(f"{i} x 7 = {i * 7}")
 
table = int(input("Enter a number (0-12): "))
if 0 <= table <= 12:
    for i in range(13):
        print(f"{i} x {table} = {i * table}")
else:
    print("Number must be between 0 and 12.")

table = int(input("Enter a number (negative for backward): "))
if table >= 0:
    for i in range(13):
        print(f"{i} x {table} = {i * table}")
else:
    table = abs(table)
    for i in range(12, -1, -1):
        print(f"{i} x {table} = {i * table}")
