#Object Oriented Program

#ceate class
class My_class:
    x = 5;
    
#create object
p1 = My_class()
print(p1.x)

#in-buile function - __init__() --All classes have a function called __init__(),
# which is always executed when the class is being initiated.

class person:
    def __init__(self,name,age):
        self.name = name;
        self.age = age;
        
p1 = person("baran",22);

print(p1.name);
print(p1.age);

#The self parameter is a reference to the current instance of the class, 
# and is used to access variables that belong to the class.

