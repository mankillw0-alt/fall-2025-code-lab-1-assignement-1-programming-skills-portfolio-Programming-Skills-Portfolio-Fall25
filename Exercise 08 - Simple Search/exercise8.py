#contains list of names
list=["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]
#searches for a specific name in the list
search_name= "Sam"
if search_name in list:
    print(f"{search_name} found in the list.")
#asks user to input a name to search
search_name = input("Enter a name to search for: ")
if search_name.capitalize() in list:
    print(f"{search_name} found in the list.")
else:
    print(f"{search_name} not found in the list.")