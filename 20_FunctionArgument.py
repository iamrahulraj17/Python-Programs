# agar hamne function calling me argument nahi diye hain tab function ke argument execute honge
def avg(a=23,b=45):
    print((a+b)/2)
avg()

# agar funtion me aur function calling dono me arguments hain tab function calling ke argument execute honge
def avg(a=23,b=45):
    print((a+b)/2)
avg(12,34)

# agar function calling me ek argument hai to wo as value of first elment treat hoga aur second value wo function se lega
def avg(a=23,b=45):
    print((a+b)/2)
avg(12) # meaning of this line is 'avg(a=12)'

# function argument me ham value bhi specifiy kar sakte hain first and second element ki
def avg(a=23,b=45):
    print((a+b)/2)
avg(b=12)

# jab values function aur function calling dono me hoti hain to priority hamesha function calling ke elements ko milti hain
def avg(a=23,b=45):
    print((a+b)/2)
avg(a=34,b=12)

# is condition me 'a'&'b' ki value fumction calling se aegi aur 'c' ki value function se
def avg(a,b,c=34):
    print((a+b+c)/3)
avg(12,23) 

# we pass the argument as a string in the function calling
def name(fname,mname,lname):
    print(fname,mname,lname)
name(fname="Rahul",mname="Raj",lname="Kushwaha")

def name(fname,mname,lname):
    print(fname,mname,lname)
name("Rahul","Raj","Kushwaha")

# we pass the argument as a string in the function or function calling
def name(fname,mname,lname="Kushwaha"):
    print(fname,mname,lname)
name(fname="Rahul",mname="Raj")