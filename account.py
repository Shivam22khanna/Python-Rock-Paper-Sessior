print("..........................................................")
print("rock, paper ,sessiors Account Setup")
print("............................................................")
while True:
    username = input("Pick a username: ")
    password = input("pick a password: ")
    password_confirm = input("Please confirm your password: ")

    if password != password_confirm:
        print("Your password don't match. Please try again.")
    if password == password_confirm:
        print("Your Account has been setup.")
        text_file = open("./account.txt","a")
        text_file.write(",")
        text_file.write(username)
        text_file.write(",")
        text_file.write(password)
        text_file.close()
        break    
