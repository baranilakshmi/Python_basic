'''
#print 1st 10 numbers

for i in range(1,11):
    print(i)
    
#print 1st 10 even numbers

for i in range(2,22,2): #it starts with 2 and end with 22 increment by 2 
    print(i)
    
#print 1st 10 even numbers in reverse order

for i in range(20,0,-2):
    print(i)
    
for i in range(21,1,-2):
    print(i)
    
'''

#num = int(input("Enter the no: "))

#for i in range(1,11):
#   print("2 * 1 = " ,num * i )
    
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end= " ")
    print()
    
    
for i in range(4,0,-1):
    for j in range(i):
        print("#",end=" ")
    print()