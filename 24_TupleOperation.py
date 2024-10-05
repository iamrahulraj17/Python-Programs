# We can change the tuple values by changing it to the list and manipulate the list and than change it to the tuple. There is no direct way to change the tuple.

friends = ("Rohit", "Abhay", "Naman") # We create a tuple(friend)
print("\n",type(friends))
print(friends,"\n")

temp=list(friends) # We copy the element of tuple(friends) to the list in the list(temp)
print(type(temp))
print(temp,"\n")

temp.append("Satendra") # We add a new member or element in the list(temp)
print(type(temp))
print(temp,"\n")

temp.pop(2) # it remove the element which index is '2' in the list
print(type(temp))
print(temp,"\n")

temp[2]="Naman" # it change the value of index(2) for ex: Satendra change to Naman
print(type(temp))
print(temp,"\n")

friends= tuple(temp) # it copies the element of list(temp) to the friends as a tuple.
print(type(temp))
print(temp,"\n")
print(type(friends))
print(friends,"\n")

# We concatinate the two or more tuple into a single tuple
friends1=("Rohit","Abhay","Naman")
friends2=("Prajjwal","Ridhum","Nitin")
allfriends=friends1+friends2 # we create a new tuple allfriends and store the concatinated items
print(allfriends,"\n")

t=(1,4,5,31,34,6,7,3,45,3,3,45)
print(t)
print("Occurance of 3 in tuple is (",t.count(3),") times")# it count the occurance of the certain element
print("Index of element 3 is (",t.index(3),")") # it shows the index of tuple of the element
print("Index of 3 between 8 & 10 (",t.index(3, 8, 10),")\n")# it shows the index of '3' in between '8' and '10' index.