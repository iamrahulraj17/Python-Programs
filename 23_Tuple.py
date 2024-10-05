# Tuple are unchangeable and created by ( ) brackets. in one element tuple it is neccesary to use coma after write an element for ex: hey = (1,). it is treated as a single variable.
# we can't change the value of tuple. 
# we can't change the length of tuple. 
# we can't change the existing tuple. 
# it is similar to the list but not changeable.
# all the methods of list can be applied on the tuple.

hey=(1,34,45,67,"Tuple",True) 
print(type(hey))
print(hey)
print(hey[0])
print(hey[1])
print(hey[2])
print(hey[3])
print(hey[4])
print(hey[5])
print(hey[-5])
print(len(hey))

i = "Tuple"

if i in hey:
    print("Yes",i,"is in the tuple(hey).")
else:
    print("No",i,"is not in the tuple(hey).")
    
hi = hey[1:5] # we performe the slicing method in the tuple 
print(hi) # but the actual tuple doesn't change it simply create the new tuple
print(hey)

print(len(hi))