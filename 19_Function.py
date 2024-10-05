# function is define by 'def' keyword.
def squareroot(a,b):
    sq = a**b
    print("\nPower of",a,"is",b,"=",sq,"\n")

def multiplication(a,b):
    m = a*b
    print("\n",a,"*",b,"=",m,"\n")

def addition(a,b):
    add = a+b
    print("\n",a,"+",b,"=",add,"\n")

def subtraction(a,b):
    sub = a-b
    print("\n",a,"-",b,"=",sub,"\n")

def divison(a,b):
    div = a/b
    print("\n",a,"/",b,"=",div,"\n")

def reminder(a,b):
    rem = a%b
    print(rem,"\n")

def temporaryfun():
    pass 
# agar hame kisi function ka code baad me likhna hai to ham usme 'pass' likh kar chod denge.
# 'pass' kisi function ko khali chod deta hai aur aage ka code execute kar deta hai.
    
print("\n          --------------CALCULATOR---------------")

print("          |Press '1' for 'Addition'             |")
print("          |Press '2' for 'Subraction'           |")
print("          |Press '3' for 'Multiplication'       |")
print("          |Press '4' for 'Division'             |")
print("          |Press '5' for 'Square Root'          |")
print("          |Press '6' for 'Remainder'            |")

print("          ---------------------------------------")

z = int(input("\nEnter the number for Action:"))

x = int(input("\nEnter first number:"))
y = int(input("Enter second number:"))

if (z==1):
    addition(x,y) # calling the function value.
    
elif (z==2):
    subtraction(x,y) # calling the function value.
    
elif (z==3):
    multiplication(x,y) # calling the function value.
    
elif (z==4):
    divison(x,y) # calling the function value.
    
elif (z==5):
    squareroot(x,y) # calling the function value.
    
elif (z==6):
    reminder(x,y) # calling the function value.
    
else:
    print("\n!!Invalid Number!!\n")