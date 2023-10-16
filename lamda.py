#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.

#syntax -- lambda arguments : expression

x = lambda a : a + 5;
print(x(2))

y = lambda a,b : a * b;
print(y(2,3))

z = lambda a, b, c : a + b + c;
print(z(1,2,3))

#lambda functions

def my_func(n):
    return lambda a : a * n;

my_doubler = my_func(3);
print(my_doubler(5))

