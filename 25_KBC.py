questions=["1.Which is the biggest continent?","2.Who found the concept of “Gravitation” for the first time?","3. Which planet is known as “The Blue Planet”?","4.What is the driver of a Train called?","5. Who discovered Aeroplane?","6.Which bird is the universal symbol of Peace?","7.What causes Anemia?","8.Who is the author of “Julius Caesar”?","9.What is the “Fear of Darkness” called?","10.What is the capital city of Peru?"]

answers=["Asia","Issac Newton","Earth","Locopilot","Wright Brothers","Dove","By the deficiency of Iron","William Shakespeare","Nyctophobia","Lima"]

option=["a)Asia\t\tb) Africa\nc) Australia\td) Europe", "a) Albert Einstein\tb) Charles Darwin\nc) Issac Newton\t\td) V. Raman", "a) Mercury\tb) Venus\nc) Uranus\td) Earth","a) Pilot\tb) Train Driver\nc) Locopilot\td) Captain","a) Wright Brothers\tb) Steve Waugh\nc) Albert Einstein\td) Stephen Hawking","a) Pigeon\tb) Dove\nc) Peacock\td) Pelican","a) By the deficiency of Iron\t\tb) By the deficiency of Iodine\nc) By the deficiency of Vitamin D\td) By the deficiency Calcium","a) William Shakespeare\tb) Geoffrey Chaucer\nc) John Milton\t\td) Sylvia Plath","a) Nyctophobia\t\tb) Ablutophobia\nc) Ophidiophobia\td) Arachnophobia","a) Prague\tb) Rome\nc) Los Angeles\td) Lima"]

prizemoney=[0,1000,2000,5000,10000,60000,120000,360000,2500000,5000000,10000000]

def opt(i):
    print("\nOption",a,"is the right answer:",answers[i])
    print("--------------------------------------------------------------\n")
    g=input()

def opt2(z,p):
    print("\nOption",a,"is incorect & right answer is:",answers[z],"\n")
    print("!!!!!!!!!!!!!The Game is OVER now.!!!!!!!!!!!!!\n")
    print("Your Total Wining Prize = ₹",prizemoney[p],"\n")
    
def pqo(r,s):
    print("\nPRIZE MONEY = ₹",prizemoney[s],"\n")
    print(questions[r])
    print(option[r])
    
def quit(b):
    if(q=='q'):
        print("\nYou Quit the game.")
        print("Your Winning amount is: ₹",prizemoney[b])
        x = str(input("Guess the correct answer:"))
        print(answers[b],"is the right answer.")
    
print("\n-----------------------------------------KBC------------------------------------------")
print("| 10 - ₹ *1 Crore*                                                                   |")
print("|  9 - ₹ 50 Lakh           WELCOME TO           -> If you quit the game              |")
print("|  8 - ₹ 25 Lakh              KAUN                 you recieve the wining amount.    |")
print("|  7 - ₹ *360000*            BANEGA                                                  |")
print("|  6 - ₹ 120000             CROREPATI           -> If you give the wrong answer      |")
print("|  5 - ₹ 60000                                     you recieve only the              |")
print("|  4 - ₹ *10000*            PRESS <Q>              checkpoint amount.                |")
print("|  3 - ₹ 5000           TO QUIT THE GAME                                             |")
print("|  2 - ₹ 2000            PRESS <ANY KEY>        -> The * amount is the               |")
print("|  1 - ₹ 1000         TO CONTINUE THE GAME         checkpoint amount.                |")
print("--------------------------------------------------------------------------------------")
YES = input("\nPress <ANY KEY> to START the GAME:")

# Question no. 1
pqo(0,1)
q= str(input("\n<Press <Q> for Quit or Press <ANY KEY> for Continue>:"))
if(q=='q'):
    quit(0)
    
else:
    a = str(input("\nIs option ko lock kiya jae:"))
    if (a=='a'):
        opt(0)
        
        # Question no. 2
        pqo(1,2)
        q= str(input("\n<Press <Q> for Quit or Press <ANY KEY> for Continue>:"))
        if(q=='q'):
            quit(1)
        else:
            a = str(input("\nIs option ko lock kiya jae:"))
            if (a=='c'):
                opt(1)
        
                # Question no. 3
                pqo(2,3)
                q= str(input("\n<Press <Q> for Quit or Press <ANY KEY> for Continue>:"))
                if(q=='q'):
                    quit(2)
                else:
                    a = str(input("\nIs option ko lock kiya jae:"))
                    if (a=='d'):
                        opt(2)
                    
                        # Question no. 4
                        pqo(3,4)
                        q= str(input("\n<Press <Q> for Quit or Press <ANY KEY> for Continue>:"))
                        if(q=='q'):
                            quit(3)
                        else:
                            a = str(input("\nIs option ko lock kiya jae:"))
                            if (a=='c'):
                                opt(3)

                                # Question no. 5
                                pqo(4,5)
                                q= str(input("\n<Press <Q> for Quit or Press <ANY KEY> for Continue>:"))
                                if(q=='q'):
                                    quit(4)
                                else:
                                    a = str(input("\nIs option ko lock kiya jae:"))
                                    if (a=='a'):
                                        opt(4)

                                        # Question no. 6
                                        pqo(5,6)
                                        q= str(input("\n<Press <Q> for Quit or Press <ANY KEY> for Continue>:"))
                                        if(q=='q'):
                                            quit(5)
                                        else:
                                            a = str(input("\nIs option ko lock kiya jae:"))
                                            if (a=='b'):
                                                opt(5)

                                                # Question no. 7
                                                pqo(6,7)
                                                q= str(input("\n<Press <Q> for Quit or Press <ANY KEY> for Continue>:"))
                                                if(q=='q'):
                                                    quit(6)
                                                else:
                                                    a = str(input("\nIs option ko lock kiya jae:"))
                                                    if (a=='a'):
                                                        opt(6)

                                                        # Question no. 8
                                                        pqo(7,8)
                                                        q= str(input("\n<Press <Q> for Quit or Press <ANY KEY> for Continue>:"))
                                                        if(q=='q'):
                                                            quit(7)
                                                        else:
                                                            a = str(input("\nIs option ko lock kiya jae:"))
                                                            if (a=='a'):
                                                                opt(7)

                                                                # Question no. 9
                                                                pqo(8,9)
                                                                q= str(input("\n<Press <Q> for Quit or Press <ANY KEY> for Continue>:"))
                                                                if(q=='q'):
                                                                    quit(8)
                                                                else:
                                                                    a = str(input("\nIs option ko lock kiya jae:"))
                                                                    if (a=='a'):
                                                                        opt(8)

                                                                        # Question no. 10
                                                                        pqo(9,10)
                                                                        q= str(input("\n<Press <Q> for Quit or Press <ANY KEY> for Continue>:"))
                                                                        if(q=='q'):
                                                                            quit(9)
                                                                        else:
                                                                            a = str(input("\nIs option ko lock kiya jae:"))
                                                                            if (a=='d'):
                                                                                opt(9)
                                                                                print("CONGRATULATION!!!\nYou WON!!!!\nYour wining PRIZE MONEY: 10000000")
                                                                                print("--------------------------------------------------------------\n")
                                                                            else:
                                                                                opt2(9,10)
                                                                    else:
                                                                        opt2(8,7)
                                                            else:
                                                                opt2(7,7)
                                                    else:
                                                        opt2(6,4)
                                            else:
                                                opt2(5,4)
                                    else:
                                        opt2(4,4)
                            else:
                                opt2(3,4)
                    else:
                        opt2(2,0)
            else:
                opt2(1,0)
    else:
        opt2(0,0)