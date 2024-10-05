# The match case in python is recently added fuctionality in python which can only run on python 3.10 version only.
x = int(input("Enter the value of x:"))
print(x)

match (x):
    case (1):
        print("x = 1") 
    case (2):
        print("x = 2") 
    case (3):
        print("x = 3") 
    case (4):
        print("x = 4") 
    case (5):
        print("x = 5") 
    case (6):
        print("x = 6") 
    case (7):
        print("x = 7") 
    case (8):
        print("x = 8") 
    case (9):
        print("x = 9") 
    case (0):
        print("x = 0") 
    case (_):
        print("x is invalid!!!") 
        