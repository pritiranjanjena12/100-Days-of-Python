username = "pintu"
password = "python123"

entered_username = input("Enter your username: ")

if entered_username == username:
    entered_password = input("Enter your password: ")

    if entered_password == password:
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")