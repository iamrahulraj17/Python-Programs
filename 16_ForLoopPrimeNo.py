# Program to find the list of prime number and composite number.

print("\nTo find a given number is prime or composite:\n")
f = int(input("Enter first number of the Range:"))
s = int(input("\nEnter second number of the Range:"))
print("\nYour Range is [",f,",",s,"]\n")
for x in range(f,(s+1)):
    if (((x%2)!=0 and (x%3)!=0 and (x%5)!=0) or (x==2) or (x==3) or (x==5)):
        print(x,"is a prime number.\n") 
    else:
        print(x,"is a composit number.\n")
print("!!Thanx for Visiting Here!!\n")