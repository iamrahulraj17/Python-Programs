#  Program to print the character of the list.

color = ['Purple','Red','Green','Blue','Black','White']
for c in color:
    print("\n",c)
    if (c==("Red")):
        print("This is the favorite color of the Developer.\n")
    else:
        print("This is a random color.\n")
    for e in c:
        print(e)