"""
Author='Daniel Lewis'
Telos=Homework
Topic='Strings, Inputs and ASCII'
Identifier='Page 25, Task 1'
Date=19-09-2024
"""

print('Task-1: \n')
greatMusician=input('What is your favourite music artist? :')
descriptor='talented'
print(greatMusician+' is very '+descriptor+'!')

# Task 2
print('Task 2:\n')
fullName=input('Please enter your full name :')
space=fullName.index(' ') # The place separating first and second name
firstName=fullName[:space] # Everything up to the space
surName=fullName[(space+1):] # Everything after the space
print('Your first name is',firstName+'.')
print('Your surname is',surName+'.')
print('\n')

# Task 3
print('Task 3:\n')
time=input('Enter a time, in the format hours:minutes:seconds :')
hrseparator=time.index(':') # Finds the first colon
hrs=int(time[:hrseparator]) # Finds everything before the first colon (the hours)
time=time[(hrseparator+1):] # Gets rid of everything from the first colon and behind, so we can find the second colon
minseparator=time.index(':') # Finds the second colon
mins=int(time[:minseparator]) # Finds everything before the second colon (the minutes)
secs=int(time[(minseparator+1):]) # Finds everything after the second colon
totalTime=(((hrs*60)+mins)*60)+secs # Puts it all together
print(time,'in seconds is',str(TotalTime)+'.')
print('\n')

# Task 4
print('Task 4:\n')
s=int(input('Enter another amount of seconds :'))
s2=s/60
print(s,'seconds is',int(round(s2,0)),'minutes, rounded.')
print('\n')

# Task 5
print('Task 5:\n')
for uzbekistan in range(1,6): # Loops 5 times, overwriting a each time
    a=input('Input a character to convert to ASCII :')
    print('The ASCII of',a,'is',str(ord(a))+'.')
print('\n')

# Task 6
print('Task 6\n')
use=int(input('Please enter the units of electricity used last month :'))
charge=26.2+(use*0.19)
print('The electricity charge is €'+str(round(charge,2))+'.')
print('\n')

print('Task-7:\n')
fish=int(input('Please enter the number of required orders of fish :'))
chips=int(input('Please enter the number of required orders of chips :'))
orderCost=round(((fish*4.5)+(chips*2.8)),2)
vat=round((orderCost*0.09),2)
finalCost=vat+orderCost
print('Order details:\n'+str(fish)+' Fish Fillet\t€4.50\n'+str(chips)+' Side (chips)\t€2.80')
print('Subtotal:\t€'+str(orderCost))
print('VAT (9%):\t€'+str(vat))
print('Final Cost:\t€'+str(finalCost))
print('\n')

print('Task-8:\n')
word=input('Please input a five-letter word to encode, in lowercase :')
key=int(input('Please input a code to encode with :'))
if (ord(word[0])+key)<122:
    c0=chr(ord(word[0])+key)
else:
    c0=chr(((ord(word[0])+key)-26))
    
if (ord(word[1])+key)<122:
    c1=chr(ord(word[1])+key)
else:
    c1=chr(((ord(word[1])+key)-26))
    
if (ord(word[2])+key)<122:
    c2=chr(ord(word[2])+key)
else:
    c2=chr(((ord(word[2])+key)-26))
    
if (ord(word[3])+key)<122:
    c3=chr(ord(word[3])+key)
else:
    c3=chr(((ord(word[3])+key)-26))
    
if (ord(word[4])+key)<122:
    c4=chr(ord(word[4])+key)
else:
    c4=chr(((ord(word[4])+key)-26))
    
newWord=c0+c1+c2+c3+c4
print(word,'encoded is',newWord+'.')
