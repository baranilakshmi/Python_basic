#it's same as list but, list is changeable (mutable) where tuple is immutable (unchangeable)
#tuples also contain differnt data types.
#it only supports count and index.

tup = (32,45,53,1,6);
print(tup)
print(tup[3])
#tup[0] = 8 -- here we can't change the values.
print(len(tup))
#converting tuples into list
list1 = list(tup)
print(list1)