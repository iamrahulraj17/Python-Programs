print("\n''''''''''''''''''Votting Eligiblity Test''''''''''''''''''\n")
name = input("Enter your name: ")

print(name,"Please")
age = int(input("Enter your age: "))
print("\nHELLO!!",name,"Your age is",age)

if (age>=60):
    print("\nYou are senior citizen and you also eligible for voting.\n")
    
elif (age>=18):
    print("\nYou are eligible for voting\n")
    
elif (age<=0):
    print("\n!!! You are not born yet !!!\n")
    
else:
    print("\nYou are not eligible for voting\n")
    
print("""\n''''''''''''''''''Thanks for visiting here''''''''''''''''''
                     Have a Nice Day :)\n""")