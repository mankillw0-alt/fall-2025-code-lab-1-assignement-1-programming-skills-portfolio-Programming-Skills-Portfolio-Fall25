print("Welcome lets test ur knowledge of Capitals!")
#contains dictionary of countries and their capitals
capitals={'France':'paris','Germany':'berlin','Italy':'rome','Spain':'madrid','Portugal':'lisbon','Austria':'vienna','Albania':'tirana','Greece':'athens','Netherlands':'amsterdam','Belgium':'brussels'}
#executes for specific number of times till the questions last
for c in capitals:
    print(f"\nWhat is the capital of {c}?")
    a=input("Enter your answer: ")
#answer will not affect even if user enters capital letters
    if a.lower()==capitals[c]:             
        print("Your answer is correct!")
    else:
        print("Incorrect. The correct answer is "+capitals[c].capitalize()+".")