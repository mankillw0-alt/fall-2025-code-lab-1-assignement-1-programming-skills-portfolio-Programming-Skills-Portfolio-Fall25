#def check_num function to determine if a number is even or odd
def check_num(num):
    if num % 2 == 0:
        return "The Number is Even"
    else:
        return "The Number is Odd"
#main function to get user input and display result
def main():
    num = int(input("Enter a number: "))
    print(check_num(num))
#call main function
if __name__ == "__main__":
    main()