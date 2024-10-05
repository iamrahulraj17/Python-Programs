name = input("Enter your name:")
age = int(input("Enter your age:"))

print("\nHello!!",name)
print("Your age is",age)  
    
if (age<18):
    if (age<=0):
        print("\n!!You are not born yet!!\n")
    else:
        print("\nYou are under age :(\n") 
    
else:
    if (age>60):
        print("\nYou are over age :(\n")
    else:
        print("\nYou achive liegal age :)\n")