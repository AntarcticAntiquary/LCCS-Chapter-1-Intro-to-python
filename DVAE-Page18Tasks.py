# Author = 'Daniel Lewis'
# Telos = Classwork
# Topic = 'Data, Variables, Assignments and Expressions'
# Identifier = 'textbook page 18 Tasks 1-5'
# Date = 10-09-2024

#Task 1
print("Task-1:\n")
age=int(input("What is your age? :"))
print("Your age is",age)
print("What a great age!")
print("\n")

#Task 2
import random
print("task-2:")
num1=random.randint(10,100)/10
num2=random.randint(10,100)/10
print("Their sum is",num1+num2)
print("Their difference is",round(abs(num1-num2),1))
print("Their product is",num1*num2)
print("\n")

#Task 3
n1=random.randint(10,100)/10
n2=random.randint(10,100)/10
print("The average of two number is",round(((n1+n2)/2),1))
print("The modular divison is",round((n1%n2),1))
print("One to the power of the other is",round((n1**n2),1))