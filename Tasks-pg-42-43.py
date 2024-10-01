 Author='Daniel Lewis'
# Telos=Classwork
# Topic='Lists'
# Identifier='Tasks page 42'
# Date=29-09-2024

# Task 1:
print('Task-1:')
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
print('Task-2:')
hours=[12,7,9,9,6,8,2]
litres=0
for counter in range(len(hours)):
    litres+=(hours[counter]*0.5)
print('Stephen drinks',litres,'litres of milk in a week')
cost=litres*1.35
print('The amount he should pay is',round(cost,2),'euro per week.')
print('\n')

# Task 3
print('Task-3:')
print('Please enter the precipitation amount for the week below, in centimetres')
precipitation=[0,0,0,0,0,0,0]
weekdays=['Monday,','Tuesday,','Wednesday,','Thursday,','Friday,','Saturday,','Sunday,']
precipitation[0]=round(int(input('Monday :')),2)
precipitation[1]=round(int(input('Tuesday :')),2)
precipitation[2]=round(int(input('Wednesday :')),2)
precipitation[3]=round(int(input('Thursday :')),2)
precipitation[4]=round(int(input('Friday :')),2)
precipitation[5]=round(int(input('Saturday :')),2)
precipitation[6]=round(int(input('Sunday :')),2)
totalRainfall=0
for looper in range(len(precipitation)):
    totalRainfall+=precipitation[looper]
print('The total rainfall was',str(totalRainfall)+'cm')
print('The days with high rainfall are:',end=' ')
for looper in range(len(precipitation)):
    if precipitation[looper]>3.5:
        print(weekdays[looper],end=' ')
