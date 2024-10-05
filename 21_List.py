# This is a list which is start with '['and ends with']'
marks = ["1: 18","2: 15","3: 17","4: 19"]

print(marks) # it print the whole element of the list              : All three
print(marks[:]) # it print the whole element of the list           : are equal
print(marks[0:len(marks)]) # it print the whole element of the list: values.
print(marks[1]) # it print the element of index 1
print(marks[1:]) # it print the element of index 1 to end
print(marks[1:3]) # it print the element of index 1 & 2
print(marks[0:3:2]) # the third index(2) is jump index which jump the element by 2
print(marks[0:-2]) # it print the element from 0 index to 2 index(length of list - 2)
print(marks[-2]) # it print the 2 element of the string (length of list - 2)

print("The elements present in list =",len(marks))
for k in marks:
    print("Marks of Student",k)
    
if 1 in marks:
    print("Yes")
else:
    print("No")
    
if "1: 18" in marks:
    print("yess")
else:
    print("no")
    
if "18" in "1: 18":
    print("yes")
else:
    print("no")

# We create the runtime list by this method   
lst = [(i) for i in range(1,11)] # it print the i(which is a number) for range 1 to 10
print(lst)