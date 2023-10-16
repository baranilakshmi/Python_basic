#It's a collection of unique elements.
#unordered,unchangeable and duplicates value not allowed.
#it can contain different data types.

s = {45,64,63,1,64,67}
print(s) #we got 64 is once.

#s[2] = 44 -- unchangeable

s.add(99)
print(s)

#The object in the update() method does not have to be a set, 
# it can be any iterable object (tuples, lists, dictionaries etc.)
l = ['a','f',32]
s.update(l)
print(s)

#remove the values -- remvoe,discard,pop,del,clear

s.remove('a')
print(s)
s.discard('f')
print(s)
s.pop() #Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
print(s)
#del and clear will deleted the full set.

#joining two sets -- (union,update - both will exclueded duplicate values),intersection_update,intersection,
#symmetric_difference_update,symmetric_update

s1 = {32,53,92,99}
print(s1)

s2 = s1.union(s)
print(s2)