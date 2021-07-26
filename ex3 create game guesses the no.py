#ex3 create game guesses the no n=18
 # no of guesses 9
 # print no of guesses left
 # no of guesses he took to finish
 # game ove and win the game       

x=input("Plese press 'S' for Enter the game :\n")
z=x.capitalize()
if z=="S": 
    print("WELCOME TO THE GAME! GUESS THE NUMBERS",end="=*=*=")
    print("Note your life line is only 9")
    print("Guess Correct number and win the Game, BEST OF LUCK!!\n")
    i=1
    j=8
    while i<=9 or j>=1:
        print("Enter your Guess number:")
        user_guess=int(input())
        main_guess=int(18)   
         
              
        if user_guess!=main_guess:            
            print("Wrong,Guess again")            
            print(f"your {user_guess} No is lesser, Guess UP(Bigger) Number" if user_guess<main_guess else f"your {user_guess} No is Greator, Guess down(lower) Number")            
            print(f"Now your life line only {j} left")
            print(i,"\n")            
            if i==9:
                print("======Game Over======/n")
                print(f"Your life line {j}")
                break
            i=i+1
            j=j-1
            continue                             
               
        else:
            print("Congrats!You won Game")
            print(f"you done with {i} step")
            break
else: 
    print("Enter the correct letter")