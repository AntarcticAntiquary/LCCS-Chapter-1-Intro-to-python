# Author = 'Daniel Lewis'
# Telos = Classwork
# Topic = 'Data, Variables, Assignments and Expressions'
# Identifier = 'OneNote Tasks'
# Date = 10-09-2024

# Task01
print("Task-1:\n")
personName = "Alexander"
favouriteColour="red"
print("Hi",personName,"- your favourite colour is",favouriteColour)
print("Goodbye",personName)
print("\n")

personName = "Charlie"
favouriteColour="green"
print("Hi",personName,"- your favourite colour is",favouriteColour)
print("Goodbye",personName)
print("\n")

#Task-02
print("Task-2:\n")
personName = input("Enter your name :")
favouriteColour=input("Enter your favourite colour :")
print("Hi",personName,"- your favourite colour is",favouriteColour)
print("Goodbye",personName)
print("\n")

#Task-03
#Variables are a useful way to store information
#The naming conventions are strict but not restrictive - I will use camelCase
#Datatypes are quite strict, will need to take care with them

#Task-04
print("Task-4:\n")
goals = 0 #Creates variable to track number of goals scored
goals+=1 #Adds +1 to the number of goals
print("The value of goals is",goals) #Prints result for user
print("\n")

answer=1+2
print(answer)
value1=answer+3 #Gets 1+2+3 in steps
value2=1+2+3 #Gets 1+2+3 all at once
print(value1,value2) #Displays similarity
print("\n")

a=10
b=5
temp=a
a=b
b=temp #Swaps the values of a and b using a temporary variable

accountBalance=1000
withdrawalAmount=600
accountBalance-=withdrawalAmount #Updates account balance with the withdrawal

days=2
hrs=24
mins=60
total=days*hrs*mins
print(total) #Finds the total amount of minutes in two days with simple multiplication
print("\n")

#Task-05
print("Task-5:\n")
year=int(input("Enter the current year :"))
age=int(input("What age will you be at the end of this year? :"))
print("You were born in",year-age)
print("\n")

#Task-06
print("Task-6:\n")
centigrade=float(input("Enter the Centigrade value :"))
farenheit=9/5*centigrade+32
print(centigrade,"degrees C equals",round(farenheit,1),"degrees F")
print("\n")

#Task-07
principal=float(input("Enter principal :"))
rate=float(input("Enter rate :"))
time=float(input("Enter time in years :"))
amount=principal*rate*time
print("The interest amount is",amount)
print("\n")

#Task-08
#Prediction: 10 to the power of 2, which is 100
#(Note: not to the power of -2 becuase it is the abstract value)
print("Task-08:\n")
print(pow(10, abs(-2)))
#Prediction correct!
print("\n")

#Task-09
print("Task-9:\n")
runningTotal=0
price1=10
runningTotal+=price1
price2=14
runningTotal+=price2
price3=6
runningTotal+=price3
print("Total amount is",runningTotal)
print("\n")

#Task-10
print("Task-10:\n")
import random
low=random.randint(1,100)
high=random.randint(low,100)
n1=random.randint(low,high)
n2=random.randint(low,high)
n3=random.randint(low,high)
n4=random.randint(low,high)
n5=random.randint(low,high)
average=(n1+n2+n3+n4+n5)/5
print("The average of",n1,n2,n3,n4,n5,"is",average)
