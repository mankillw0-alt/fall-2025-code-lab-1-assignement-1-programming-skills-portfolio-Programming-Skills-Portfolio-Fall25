name= input("Enter your full name: ")
hometown= input("Enter your hometown: ")
age= input("Enter your age: ")
while age.isdigit()==False:
    print("Invalid input. Please enter a number for age.")
    age= input("Please enter age in numbers: ")
print('full name:', name, '\nhometown:', hometown, '\nage:', int(age))
