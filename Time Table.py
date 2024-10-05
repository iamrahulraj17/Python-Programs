import time

print("\n                        Time Table")
print("                 --------------------------")
print("                 |11:00 - 1:00 UPCET      |")
print("                 |1:00 - 2:00 Lunch       |")
print("                 |2:00 - 5:00 Rest        |")
print("                 |5:00 - 6:00 Coaching    |")
print("                 |6:00 - 7:00 Programming |")
print("                 |7:00 - 7:30 Rest        |")
print("                 |7:30 - 9:30 UPCET       |")
print("                 --------------------------")

t = time.strftime("%H:%M:%S")
print("\nTime =",t)

th = time.strftime("%H")
tm = time.strftime("%M")
thm = time.strftime("%H%M")

if(int(th)>=11):
    print("\nIt's time to study UPCET.\n")
elif(int(th)>=13):
    print("\nIt's time to eat lunch.\n")
elif(int(th)>=14):
    print("\nIt's time to Rest.\n")
elif(int(th)>=17):
    print("\nThis is the time to Teach coaching.\n")
elif(int(th)>=18):
    print("\nIt's Programming time.\n")
elif(int(th)>=19):
    print("\nIt's time to Rest.\n")
elif(int(thm)>=1930):
    print("\nIt's time to study UPCET.\n")
else:
    print("\nIt's time to Sleep.\n")