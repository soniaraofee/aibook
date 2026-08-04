USERNAME = "admin"
PASSWORD = "1234"

max_attempts = 3

for attempt in range(max_attempts):
    username = input("Username: ")
    password = input("Password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
        break
    else:
        remaining = max_attempts - attempt - 1
        if remaining > 0:
            print(f"Invalid credentials. {remaining} attempt(s) remaining.\n")
        else:
            print("Account locked. Too many failed attempts.")