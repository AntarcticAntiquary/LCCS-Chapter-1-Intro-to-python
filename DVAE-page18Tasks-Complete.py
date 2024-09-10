#Task 1
print("Task-1:\n")
age=int(input("What is your age? :"))
print("Your age is",age)
print("What a great age!")
print("\n")

#Task 2
import random
print("Task-2:")
num1=random.randint(10,100)/10
num2=random.randint(10,100)/10
print("Their sum is",num1+num2)
print("Their difference is",round(abs(num1-num2),1))
print("Their product is",num1*num2)
print("\n")

#Task 3
print("Task-3:\n")
n1=random.randint(10,100)/10
n2=random.randint(10,100)/10
print("The average of two number is",round(((n1+n2)/2),1))
print("The modular divison is",round((n1%n2),1))
print("One to the power of the other is",round((n1**n2),1))
print("\n")

print("Task-4:\n")
ftemp=float(input("Enter the temperature in degrees Farenheit :"))
ctemp=(5/9)*(ftemp-32)
print(ftemp,"degrees Farenheit is equal to",round(ctemp,1),"degrees Centigrade")
print("\n")

print("Task-5:\n")
mdist=11366829.6
print("CCC is",mdist,"miles from Singapore")
kdist=mdist*1.60935
print("CCC is",round(kdist,1),"kilometres from Singapore")
helicost=kdist*900
print("The cost to take a helicopter to Singapore, at €900 per kilometre, is",round(helicost,2),"euro")