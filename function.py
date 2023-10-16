#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.



#create function
def my_fun():
    print("Hello world!")
    
my_fun() #calling a fun

#Arguments -- informations can be passed into funcs as arguments.

def my_func(name): #here name passed into funcs as argument.
    print(name)
    
my_func("Bunny");

#No of Arguments -- By default, a function must be called with the correct number of arguments.

def my_funct(fname,lname):
    print("My name is ",fname,lname)
    
my_funct("Afhra","Sajeetha")


#*arg -- If you do not know how many arguments that will be passed into your function,
#        add a * before the parameter name in the function definition.
# The way function will receive a tuples of arguments.

def my_functi(*child):
    print("My elder child name is",child[0])
    
my_functi("Barani","kalai")

#another method

def my_functio(child1,child2):
    print("My younger child name is",child2)
    
my_functio("barani","kalai")


#**arg -- if u add ** before the argument, the function will receive a dictionary of arguments.

def my_function(**name):
    print("My name is",name["fname"],name["lname"])
    
my_function(fname = "barani",lname = 'Lakshmi')

#default functions

def my_fun1(country = "india"):
    print("My country is",country)
    
my_fun1("Sweedan")

#passing list as an argument

def my_func1(food):
    for x in food:
        print(x)
        
fruits = ["mango","orange","apple"]

my_func1(fruits)

#return value

def my_funct1(y):
    return y * 10;

print(my_funct1(3));
    
