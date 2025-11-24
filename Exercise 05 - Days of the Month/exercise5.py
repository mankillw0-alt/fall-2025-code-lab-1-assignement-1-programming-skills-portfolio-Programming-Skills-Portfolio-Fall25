print('welcome to the days of the month program')
#dictionary which holds months numbers as keys and number of days as values
number_days={'1':31,'2':28,'3':31,'4':30,'5':31,'6':30,'7':31,'8':31,'9':30,'10':31,'11':30,'12':31}
month=input('enter the month number from 1-12: ')
#checks if the month number is valid
while not month.isdigit() or int(month)<1 or int(month)>12:
    print('invalid month number please enter a number from 1-12')
    month=input('enter the month number from 1-12: ')
#displays the number of days in the month
if month == '2':
    leap_year = input('Is it a leap year? (yes/no): ')
    if leap_year.lower() == 'yes':
        print('The month 2 has 29 days.')
    else:
        print('The month 2 has 28 days.')
else:
    print(f'The month {month} has {number_days[month]} days.')