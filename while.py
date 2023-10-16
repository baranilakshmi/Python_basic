'''
i = 1;
while i < 6:
    print(i)
    i = i + 1
    
#break statement -- With the break statement we can stop the loop even if the while condition is true:
i = 1    
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
    
#continue statement -- With the continue statement we can stop the current iteration, and continue with the next:
p = 0
while p < 6:
    p += 1
    if p == 3:
        continue
    print(p)

#else statement -- With the else statement we can run a block of code once when the condition no longer is true:
a = 1;
while a < 5:
    print(a)
    a += 1
else:
    print("a is no longer than 5")
    

#print 1st 10 integers and squares
num = 1
while num <= 10:
    print("number\t\tsquare")
    print(num,"\t\t",num**2)
    num += 1
    

num1 = 105
while num1 >= 7:
    print(num1)
    num1 -= 7
    
x = 10
while x >= 1:
    print(x)
    x -= 1
    
'''

y = 20
sum = 0
while y >= 1:
    sum = sum + y
    y -= 2
print(sum)