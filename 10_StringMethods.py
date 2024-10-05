# String are immutable(doesn't change)
a = "!!!-Rahul-Rahul-!!!!\n"
blog = "my name is Rahul Raj\n"
xyz = "AbcABC123\n"
pqr = "Abcabc\n"
lc = "hello world\n"
uc = "HELLO WORLD"
s = " "
title = "Iam 21 Years Old"
print(a)
print(len(a))

print(a.upper()) # upper() is use to convert the string into uppercase letters.

print(a.lower()) # lower() is use to convert the string into lowercase letters.

print(a.rstrip("!")) # it only strip the tail characters of the string.

print(a.replace("Rahul","Raj")) # it replace all the occurance of particular character of the string.

print(a.split("-")) # it split the string and return the list of the elements

print(blog.capitalize()) # it capitalize the first letter of the string and remaining character of the string converted into the smallcase.

print(blog.center(50))

print(len(blog))

print(len(blog.center(50)))

print(a.count("Rahul")) # it count how many times the word or letter are come in the string.

print(a.endswith("!")) # it check if the string is end with given value or not. if yes than return True if wrong than False. 

print(blog.endswith("is",5,10))  

print(blog.find("is"))  # it find the index of first occurance of the given value. if it doesn't find any value than it simply return -1.

print(blog.index("is"))  # it find the index of first occurance of the given value. if it doesn't find any vlaue than it through an error(we uses this when we sure that the given value is occur)

print(a.isalnum())

print(blog.isalnum()) # it check the given value is alpha numaric or not

print(xyz.isalnum()) # Alpha numeric = A-Z, a-z, 0-9

print(xyz.isalpha()) # it check the given value is alphabet or not and it doesn't contain numaric values.

print(pqr.isalpha()) # Alpha  = A-Z, a-z

print(lc.islower()) # check wether the string is in lowercase or not

print(uc.islower()) 

print(lc.isupper()) # check wether the string is in Uppercase or not

print(uc.isupper())  

print(uc.isprintable()) # it return true value when all the character of the given string is in printable form or not.

print(lc.isprintable())

print(s.isspace()) # check wether the string contain blank spaces or not

print(title.istitle()) # check wether the first letter of all the characters of the string is capital or not.

print(title.startswith("Iam")) # check the first letter of the string.

print(blog.swapcase()) # convert the uppercase letter to lowercase and lowercase to uppercase

print(lc.title()) # convert the string in title where all the first letter of the every character capitalized.