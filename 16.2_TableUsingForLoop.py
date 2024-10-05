# Program to print a table of the given number.

i = int(input("\nTo print a Table of desired number \nEnter a number:"))
for k in range(i,(i*11),i):
    print(i,"*",int(k/i)," =",k)