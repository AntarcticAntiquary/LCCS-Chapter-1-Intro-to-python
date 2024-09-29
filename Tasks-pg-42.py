# Author='Daniel Lewis'
# Telos=Classwork
# Topic='Lists'
# Identifier='Tasks page 42'
# Date=29-09-2024

# Task 1:
print('Task-1:\n')
nlist=[]
n0=int(input('Enter a number :'))
nlist.insert(0,n0)
n1=int(input('Enter another number :'))
nlist.insert(1,n1)
n2=int(input('Enter another number :'))
nlist.insert(2,n2)
n3=int(input('Enter another number :'))
nlist.insert(3,n3)
n4=int(input('Enter another number :'))
nlist.insert(4,n4)
print(nlist)
for counter in range(len(nlist)):
    nlist[counter]+=1
print(nlist)
print('\n')

# Task 2
print('Task-2:\n')
hours=[12,7,9,9,6,8,2]
litres=0
for counter in range(len(hours)):
    litres+=(hours[counter]*0.5)
print('Stephen drinks',litres,'litres of milk in a week')
cost=litres*1.35
print('The amount he should pay is',round(cost,2),'euro per week.')


