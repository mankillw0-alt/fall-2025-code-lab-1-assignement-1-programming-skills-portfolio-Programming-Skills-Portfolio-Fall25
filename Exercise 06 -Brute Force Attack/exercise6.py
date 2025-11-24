#definees the correct password
password = 12345
#asks user to input password
input_password = int(input("Enter the password: "))
#verifys if the input password is correct or not
if input_password == password:
    print("Access granted")
else:
    atempts = 5
    while input_password != password:
        atempts -= 1
        input_password = int(input("Incorrect password. Try again: "))
        if input_password == password:
            print("Access granted")
            break
        else:
            if atempts == 0:
                print("Access denied")
                break