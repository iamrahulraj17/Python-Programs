import time

t = time.strftime('%H:%M:%S')
print("\nTime:",t,"\n")

th = time.strftime("%H")
print("Hours :",int(th))

tm = time.strftime("%M")
print("Minutes :",int(tm))

ts = time.strftime("%S")
print("Seconds :",int(ts))

if (int(th) < 12):
    print("""\n Good Morning Sir :)
!!Have a nice day!!\n""")
elif (int(th) < 16):
    print("\nGood Afternoon Sir :)\n")
elif (int(th) < 20):
    print("\nGood Evening Sir :)\n") 
elif (int(th) < 24):
    print("""\nGood Night Sir :)
  Sweet Dreams\n""")