list = [61,67,494,23,456,]
print(list)

# list.append(7890) # it add the element in the end of the list
# print(list)

# list.sort() # it sort the element present in the list
# print(list)

# list.sort(reverse=True) # it sort the element in reverse order present in the list
# print(list)

# list.reverse() # it reverse the elements of the list
# print(list)

# print(list.index(23)) # it return the index of the given element of the list

# print(list.count(23)) # it count that how many times the element is occur in the list

# m=list.copy() # it copies the element of list in m 
# m[0]=76       # it replace the 0th index element 61 to 76
# print(m)      # it print the new list (m)

# list.insert(0,23) # it insert the new element(23) at index (0). 
# print(list) # NOTE: the length of the list will increases by 1 and no element will remove or delete in the list

# m = [34,564,4645]
# list.extend(m) # it simply open the list(list) and add the element of list(m) in the list(list)
# print(list)

m = [23,345,5656]
n = [2,45,96]
k = m+n+list # it concatinate all the elements of all the lists in a single list.
print(k)