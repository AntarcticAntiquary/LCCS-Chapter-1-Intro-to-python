# Author = 'Daniel Lewis'
# Telos = 'Classwork'
# Topic = 'Data, Variables, Assignments and Expressions'
# Date = 09-09-2024

# OneNote - 02 - Data, Variables, Assignments and Expressions

# Introduction
personName = "Alexander"
favouriteColour = "red"
print("Hi", personName, "- your favourite colour is", favouriteColour)
print ("Goodbye", personName)

print("\n")

personName = "Charles"
favouriteColour = "green"
print("Hi", personName, "- your favourite colour is", favouriteColour)
print ("Goodbye", personName)

print("\n")

# Using input
personName = input("Enter your name :")
favouriteColour = input("Enter your favourite colour :")
print("\n")
print("Hi", personName, "- your favourite colour is", favouriteColour)
print ("Goodbye", personName)

# Operations
# Note that normal order of operations rules apply
x=7
y=3
print(x+y)	# Addition
print(x-y)	# Subtraction
print(x*y)	# Multiplication
print(x%y)	# Remainder
print(x/y)	# Division
print(x//y)	# Floor Division
print(x**y)	# Power
# The Remainder of Modular operator returns the remainder in a divison sum of x and y

print("\n")

# Input-Process-Output
# Input commands return a string
# If a numeric value is needed, two commands can help:
# int() makes it an integer
# float() makes it a float
year=int(input("Enter the current year :"))
age=int(input("What age will you be at the end of this year? :"))
print("You were born in", year-age)
# Using str(), numbers can be converted to strings
print("2000"+str(18))

print("\n")

# Example - Temperature Conversion
# The round function allows for controlling the degree of specificity
centigrade = float(input("Enter the Centigrade value :"))
farenheit = 9/5 * centigrade + 32
print(centigrade, "degrees C equals", round(farenheit,1), "degrees F")
# Other similar functions include abs(), returning absolute value
# And pow(x,y) is the same as x**y

print("\n")

# Running Total programs
# Running Totals start at 0 and successively increase
# e.g. shopping basket
runningTotal=0
price1=10
runningTotal=runningTotal+price1
price2=14
runningTotal=runningTotal+price2
price3=6
runningTotal=runningTotal+price3
print("Total amount is", runningTotal)

print("\n")

# Random Numbers
# Multiply 2 random numbers
import random
num1=random.randint(1,10)
num2=random.randint(1,10)
print(num1, "times", num2, "=", num1*num2)
print("\n")
# Average 5 random numbers
low=random.randint(1,100)
high=random.randint(low,100)
n1=random.randint(low,high)
n2=random.randint(low,high)
n3=random.randint(low,high)
n4=random.randint(low,high)
n5=random.randint(low,high)
average=(n1+n2+n3+n4+n5)/5
print("The average of", n1, n2, n3, n4, n5, "is", average)
