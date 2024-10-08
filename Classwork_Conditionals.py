# Author='Daniel Lewis'
# Telos=Homework
# Identifier=pg 30 Tasks 1-5
# Topic='Conditionals'
# Date=07-10-2024

# Task 1
print('Task-1:')
n1=int(input('Enter a number :')) # choose numbers
n2=int(input('Enter another number :'))
if n1%n2==0:
    print('The two numbers divide evenly.') # if no remainder they divide evenly
else:
    print('The two numbers do not divide evenly.') # if remainder they do not divide evenly
print('\n')

# Task 2
print('Task-2:')
print('Program to decide if user is eligible for an Irish Driving Licence')
age=int(input('Enter your age :')) # gathering age
if age>=17: # If 17 or over, they are eligible
    print('You are eligible') 
else:
    print('You are not eligible')
print('\n')

# Task 3
print('Task-3:')
print('Rogerson\'s Robotics Factory Purchase Protocol')
cost=float(input('Enter the cost of the purchase, in euros :')) # Gets cost
if cost>10000: # More than 10000
    print('The purchaser must go to tender')
elif cost>=500: # Between 10000 and 500 inclusive
    print('The purchaser must get quotes from 3 different suppliers')
else: # Less than 500
    print('You can go ahead and order')
print('\n')
    
# Task 4
print('Task-4:')
print('Partcipate in this competition to win COMPLETELY FREE Luas tickets!')
letter=input('Enter A, B or C :') # get input
if letter=='A' or letter=='a': # upper or lower case
    print('You get a COMPLETELY FREE ticket to Dundrum Shopping Centre!')
elif letter=='B' or letter=='b':
    print('You get a COMPLETELY FREE ticket to Tallaght!')
elif letter=='C' or letter=='c':
    print('You get a COMPLETELY FREE ticket to Broombridge!')
else:
    print('You uncooperative person. You get no COMPLETELY FREE ticket') # invalid input
print('\n')

# Task 5
print('Task-5:')
print('Program to calculate Higher Level Leaving Cycle Computer Science exam')
grade=int(input('Enter your percentage :'))
if grade>100:
    print('You liar') # impossible
elif grade>=90:
    print('You got a H1') # 90-100
elif grade>=80:
    print('You got a H2') #80-89
elif grade>=70:
    print('You got a H3') #70-79
elif grade>=60:
    print('You got a H4') #60-69
elif grade>=50:
    print('You got a H5') #50-59
elif grade>=40:
    print('You got a H6') #40-49
elif grade>=30:
    print('You got a H7') #30-39
elif grade>=0:
    print('You got a H8') #0-29
else:
    print('You liar')
print('\n\n')

# OneNote tasks

# Task 1
print('Task-1:')
name=input('What is your name? :')
if len(name)>10:
    print('Hello',name+'!','Your name is very long') # very long is more than 10
elif len(name)>=7:
    print('Hello',name+'!','Your name is long') # long is between 10 and 7
else:
    print('Hello',name+'!','Your name is short') # short is less than 7
print('\n')

# Task 2
print('Task-2:')
print('Menu')
print('1. Music')
print('2. History')
print('3. Design and Technology')
print('4. Exit') # Printing menu
choice=input('Please enter your choice :')
if choice=='music' or choice=='1' or choice=='Music': # Number, capitalised, lowercase
    print('You chose music')
elif choice=='history' or choice=='2' or choice=='History':
    print('You chose history')
elif choice=='design and technology' or choice=='Design and Technology' or choice=='3':
    print('You chose design and technology')
elif choice=='4' or choice=='Exit' or choice=='exit':
    print('goodbye')
print('\n')

# Task 3
print('Task-3:')
import random as r
print('rolling dice...')
roll1=r.randint(1,6)
roll2=r.randint(1,6) # Get dice rolls
if roll1==roll2:
    print('Score is',(4*roll1)) # 4*roll1=2*roll1*roll2 (on a double roll, the total is double the sum of the numbers)
else:
    print('Score is',(roll1+roll2)) # Otherwise total is the sum of the two rolls
print('\n')

# Task 4
print('Task-4:')
value=round(float(input('Enter the value of goods purchased :')),2)
if value>=200:
    cost=round((value*0.9),2) # Discount of 10% over 200
elif value>=100:
    cost=round((value*0.95),2) # Discount of 5% between 100 and 199.99
else:
    cost=value # No discount up to 99.99
print('The amount owed is',cost)
print('\n')

# Task 5
print('Task-5:')
# The correct order is A, D, C, B
#A:
num1=int(input('Enter a number :'))
num2=int(input('Enter another number :'))
#D:
if num1>num2:
    difference=num1-num2
#C:
else:
    difference=num2-num1
#B:
print('The difference is',difference)
