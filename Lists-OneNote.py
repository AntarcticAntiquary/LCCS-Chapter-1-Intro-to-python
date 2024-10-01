# Author='Daniel Lewis'
# Telos=Classwork
# Topic='Lists'
# Identifier='OneNote Lists Worksheet'
# Date=30-01-2024

import random as r
def task1():
    print('Task-1:')
    fruits=['Strawberry','Lemon','Orange','Raspberry','Cherry']
# s1=r.randint(0,4)
# s2=r.randint(0,4)
# s2=r.randint(0,4)
# print(fruits[s1])
# print(fruits[s2])
# print(fruits[s3])
    print(r.choices(fruits,k=5))
    print(r.choices(fruits,k=5))
    print(r.choices(fruits,k=5))
    print('\n')

def task2():
    print('Task-2:')
# Use same fruits list
    fruits=['Strawberry','Lemon','Orange','Raspberry','Cherry']
    print(fruits)
    fruits[0]='Apple'
    fruit='Melon'
    fruits[1]=fruit
    fruits[2]='Raspberry'
    fruits[3]=fruits[4]
    fruits[4]='Pineapple'
    print(fruits)
    print('\n')

def task3():
    print('Task-3:')
    fruits=['apple','pear','orange','banana','kiwi']
    print(fruits[1:3])
    print(fruits[2:4])
    print(fruits[2:5])
    print(fruits[1:])
    print(fruits[:5])
    print('\n')

def task4():
    print('Task-4:')
    fruits=['Strawberry','Lemon','Orange','Raspberry','Cherry']
    print(fruits[0])
    print(fruits[3])
    print(fruits[2])
    print(fruits[len(fruits)-1])
    print(fruits[1])
    fruit=fruits[2+2]
    print(fruit)
    print(fruit[0])
    orange=fruits[1]
    print(orange)
    lemon=fruits[1]
    print(lemon)
    print(fruits[0][0]+fruits[1][0]+fruits[2][0])
    print('\n')

def task5():
    print('Task-5:')
    suits=['Hearts','Diamonds','Spades','Clubs']
    cardfaces=['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    print(cardfaces[1:10])
    colourCards=cardfaces[10:23]
    print(colourCards)
    redSuits=suits[:2]
    blackSuits=suits[2:]
#print(pinStripSuits) Not sure why this was included? Giving NameError:
    print(redSuits)
    print(blackSuits)
    print('\n')
    
def task6():
    print('Task-6:')
    fruits=['pear','apple','orange','banana','kiwi']
    fruit='apple'
    vegs=['peas','carrots']
    fruits.append(fruit)
    print(fruits)
    fruits.extend(vegs)
    print(fruits)
    fruits.insert(2,fruit)
    print(fruits)
    fruits.pop()
#Leaving out brackets pops the last value, but a specific index can be popped by adding the index in brackets
    print(fruits)
    fruits.remove(fruit)
    print(fruits)
    fruits.reverse()
    print(fruits)
    fruits.sort()
    print(fruits)
    print(fruits.index(fruit))
    print(fruits.count(fruit))
    print(fruits.count('cabbage'))
    print('\n')

def task7():
    print('Task-7:')
    userList=[]
    userName=input("Enter your name :")
    userList.append(userName)
    userAge=int(input("What age are you "+userName+"? :"))
    userList.append(userAge)
    userCountry=input("What is your country of birth? :")
    userList.append(userCountry)
    userYOB=int(input('What year were you born? :'))
    userList.append(userYOB)
    userList.reverse()
    print("My database for "+userName+"\n"+str(userList))
    print('\n')

task1()
task2()
task3()
task4()
task5()
task6()
task7()