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
