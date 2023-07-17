PASSWORD = "Pythonista"
MINIMUM_LENGTH = 0
password_attempt = ""
print(len(PASSWORD))

password_attempt = input("Enter the Password: ")

while password_attempt != PASSWORD:
    if password_attempt > MINIMUM_LENGTH:
        asterisks = "*" * len(password_attempt)
        print(f"{asterisks} = Incorrect Password")
        password_attempt = input("Enter the Password: ")
    else:
        print("Invalid Input")
        password_attempt = input("Enter the Password: ")
