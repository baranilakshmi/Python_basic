#Lists are used to store multiple items in a single variable.
#ordered,changeable and allow duplicate values.
#adding values - append,insert,extend
#removing values - remove,pop,del,clear
#


nums = [1, 2, 34, 54]
print(nums[2])
print(nums[1:])
names = ['barani','gowri','afhra']
values = [9.5,'kalai',34]
print(values)
mil = [names,values]
print(mil)

#add
values.append(233)
print(values)
values.insert(1,'barani')
print(values)
values.extend([40,'vaishu'])
print(values)

#remove
values.remove(233)
values.pop(1)
values.pop()
del values[1:2]
values.clear()
print(values)

#sort
nums.sort()
print(nums)

#list in loops

for i in nums:
    print(i);
    
for i in range(len(nums)):
        print(i);
        
i = 0
while i < len(nums):
    print(i)
    i = i + 1;
    
fruits = ['apple','mango','kiwi','pineapple'];
l1 = [ ];

for i in fruits:
    if "i" in i:
        l1.append(i);
        print(l1)
        
#copy
l2 = l1.copy()
print(l2)