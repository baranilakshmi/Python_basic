#It's used to store values in key:value pairs.
#which is ordered,,changeable and don't allow duplicate values.

data = {'name': 'barani','age' : 22, 'place': 'chennai'}
print(data)

print(data['place'])

#access methods - get(),key(),values(),items()

print(data.get('name'))
print(data.keys())
print(data.values())
print(data.items()) #The items() method will return each item in a dictionary, as tuples in a list.

#to change - update()

data.update({'age' : 25})
print(data)

#to add

data['graduate'] = 'B.sc'
print(data)

#to remove -- pop(),popitem(),del(),clear()

#loop methods

for x in data:
    print(x); #it will return keys
    
for x in data:
    print(data[x]) #it will return values
    
for x in data.keys():
    print(x);
    
for x in data.values():
    print(x);
    
for x in data.items():
    print(x)
    
#copy
dic = data.copy();
print(dic)

#nested dictionaru

child_dic = {
    'child1' : {'name': 'nakshu', 'age': 2},
    'child2': {'name': 'megha', 'age' : 7}
    }

print(child_dic)
