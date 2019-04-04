import random
def Snake_Ladder():
    b=True
    c=True
    p1=input("Enter your name player 1 : ")
    p2=input("Enter your name player 2 : ")
    bp1=1
    bp2=1
    t=0
    a=0
    while(c):
       while(b):
            print(f"\n{p1}'s turn : ")
            toss=input("Enter T to toss the dice and see what have u got in your luck : ")
            a=0
            while(a!=1):
                if(toss=='T'):
                    t=random.randint(1,6)
                    print(f"{t} came up")
                    if(t==6):
                        print("Therefore tossing again...")
                        at=random.randint(1,6)
                        print(f"{at} came up")
                        if(at==6):
                            print("Therefore tossing again...")
                            aat=random.randint(1,6)
                            print(f"{aat} came up")
                            if(aat==6):
                                print("Therefore tossing again...")
                                t=random.randint(1,6)
                                print(f"Taking only the last toss's result which is {t}")
                            else:
                                t=+at+aat
                        else:
                            t=t+at
                    a=1
                else:
                    toss=input("Enter T : ")
                    continue
            bp1=bp1+t
            if(bp1>100):
                print("Since final board position is becoming more than 100, therefore last board position is retained.")
                bp1=bp1-t
            print(f"\n{p1}, your board position is {bp1}")
            if(bp1==7):
                print(f"\nYour board position had a ladder ")
                bp1=26
                print(f"\n{p1}, your new board position is {bp1}")
            elif(bp1==13):
                print(f"\nYour board position had a ladder ")
                bp1=54
                print(f"\n{p1}, your new board position is {bp1}")
            elif(bp1==17):
                print(f"\nYour board position had a ladder ")
                bp1=36
                print(f"\n{p1}, your new board position is {bp1}")
            elif(bp1==44):
                print(f"\nYour board position had a ladder ")
                bp1=75
                print(f"\n{p1}, your new board position is {bp1}")
            elif(bp1==31):
                print(f"\nYour board position had a ladder ")
                bp1=50
                print(f"\n{p1}, your new board position is {bp1}")
            elif(bp1==60):
                print(f"\nYour board position had a ladder ")
                bp1=82
                print(f"\n{p1}, your new board position is {bp1}")
            elif(bp1==73):
                print(f"\nYour board position had a ladder ")
                bp1=94
                print(f"\n{p1}, your new board position is {bp1}")
            elif(bp1==11):
                print(f"\nYour board position had a snake ")
                bp1=8
                print(f"\n{p1}, your new board position is {bp1}")
            elif(bp1==41):
                print(f"\nYour board position had a snake ")
                bp1=38
                print(f"\n{p1}, your new board position is {bp1}")
            elif(bp1==46):
                print(f"\nYour board position had a snake ")
                bp1=15
                print(f"\n{p1}, your new board position is {bp1}")
            elif(bp1==89):
                print(f"\nYour board position had a snake ")
                bp1=53
                print(f"\n{p1}, your new board position is {bp1}")
            elif(bp1==99):
                print(f"\nYour board position had a snake ")
                bp1=23
                print(f"\n{p1}, your new board position is {bp1}")
            if(bp1==100):
                print(f"\n{p1} is the winner.")
                break 
            
            print(f"\n{p2}'s turn : ")
            toss=input("Enter T to toss the dice and see what have u got in your luck : ")
            a=0
            while(a!=1):
                if(toss=='T'):
                    t=random.randint(1,6)
                    print(f"{t} came up")
                    if(t==6):
                        print("Therefore tossing again...")
                        at=random.randint(1,6)
                        print(f"{at} came up")
                        if(at==6):
                            print("Therefore tossing again...")
                            aat=random.randint(1,6)
                            print(f"{aat} came up")
                            if(aat==6):
                                print("Therefore tossing again...")
                                t=random.randint(1,6)
                                print(f"Taking only the last toss's result which is {t}")
                            else:
                                t=+at+aat
                        else:
                            t=t+at
                            
                    a=1
                else:
                    toss=input("Enter T : ")
                    continue
            bp2=bp2+t
            if(bp2>100):
                print("Since final board position is becoming more than 100, therefore last board position is retained.")
                bp2=bp2-t
            print(f"\n{p2}, your board position is {bp2}")
            if(bp2==7):
                print(f"\nYour board position had a ladder ")
                bp2=26
                print(f"\n{p2}, your new board position is {bp2}")
            elif(bp2==17):
                print(f"\nYour board position had a ladder ")
                bp2=36
                print(f"\n{p2}, your new board position is {bp2}")
            elif(bp2==44):
                print(f"\nYour board position had a ladder ")
                bp2=75
                print(f"\n{p2}, your new board position is {bp2}")
            elif(bp2==31):
                print(f"\nYour board position had a ladder ")
                bp2=50
                print(f"\n{p2}, your new board position is {bp2}")
            elif(bp2==60):
                print(f"\nYour board position had a ladder ")
                bp2=82
                print(f"\n{p2}, your new board position is {bp2}")
            elif(bp2==73):
                print(f"\nYour board position had a ladder ")
                bp2=94
                print(f"\n{p2}, your new board position is {bp2}")
            elif(bp2==11):
                print(f"\nYour board position had a snake ")
                bp2=8
                print(f"\n{p2}, your new board position is {bp2}")
            elif(bp2==41):
                print(f"\nYour board position had a snake ")
                bp2=38
                print(f"\n{p2}, your new board position is {bp2}")
            elif(bp2==46):
                print(f"\nYour board position had a snake ")
                bp2=15
                print(f"\n{p2}, your new board position is {bp2}")
            elif(bp2==89):
                print(f"\nYour board position had a snake ")
                bp2=53
                print(f"\n{p2}, your new board position is {bp2}")
            elif(bp2==99):
                print(f"\nYour board position had a snake ")
                bp2=23
                print(f"\n{p2}, your new board position is {bp2}")
            if(bp2==100):
                print(f"\n{p2} is the winner.")
                break 
        
    q=1
    while(q!=0):
        a=input("Do you want to play again?(Yes/No) ")
        a=a.upper()
        if(a=="YES"):
            q=0
            c=True
        elif(a=="NO"):
            q=0
            print("Thanks for playing!!")
            c=False
        else:
            a=input("Yes/No?")
            q=1
    
Snake_Ladder()
