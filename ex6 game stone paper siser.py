import random
import sys
#ex6 Game Snake gun water whos win like rock paper siser #remider when com and you score equal then game tie
def gun_wat_snk():
    game_list=["Water","Gun","Snake"]
    rnd=random.choice(game_list)
    return rnd

def play_again():
    try:
        print("Do You Want Play Again Y/N")
        ag_user=input()
        again_user=ag_user.capitalize()         
        if again_user=="Y":
            start_game()
        elif again_user=="N":
            sys.exit()   
        else:
            print("Wrong!Press Only Y|N")
            play_again()                        
        return again_user
    except Exception as e:        
        print(e)

def start_game():    
    p_list={"W":"Water","G":"Gun","S":"Snake"}
    print("  WELECOME TO THE GAME\n====Snake Water Gun=====\n")
    us_name=input("Please Enter your Name : ")
    user_name=us_name.capitalize()
    try:
        i=1
        user_score=0
        computer_score=0
        while i<=10:
            print("Enter your choise :",end=" ")
            for key,value in p_list.items():
                print(f"Press {key} for {value}",end="||")
            print(end="\n")            
            user_input=input()
            user_ca=user_input.capitalize()            
            
            
            for keys,values in p_list.items(): #find key like  w to water in sets 
                a=keys               
                if user_ca==a: 
                    user_ch=values
                    print("No of count",i)                
                    print(f"your choise : {user_ch}") 
                    rnd_choise=gun_wat_snk()                           
                    print(f"Computer choise : {rnd_choise}\n")
                    break              
            
            
            if user_ca==a:
                if user_ch=="Snake" and rnd_choise=="Water":#snake>water   water>gun    gun>snake
                    
                    print("You Win\n")
                    user_score+=1
                elif user_ch=="Water" and rnd_choise=="Snake": 
                    
                    print("Computer Win\n")
                    computer_score+=1

                elif user_ch=="Water" and rnd_choise=="Gun":
                    
                    print("You Win\n")
                    user_score+=1
                elif user_ch=="Gun" and rnd_choise=="Water":
                   
                    print("Computer Win\n")
                    computer_score+=1

                elif user_ch=="Gun" and rnd_choise=="Snake":
                    
                    print("You Win\n") 
                    user_score+=1   
                elif user_ch=="Snake" and rnd_choise=="Gun":
                    
                    print("Computer Win\n")
                    computer_score+=1  

                elif user_ch==rnd_choise:
                    
                    print("Draw\n")    
            else:
                print("OOPs! What are you doing? You Enter wrong keyword")
                play_again()

                       
            u_score=user_score
            c_score=computer_score              
            i+=1
            # time.sleep(1)
        print("====Final Score===")
        print(f"Your total score : {u_score}")
        print(f"Computer total score : {c_score}\n")
        while u_score>c_score:
            print(f"{user_name} is winner\n")
            break
        else:
            print("Compuer is winner\n")
            play_again()

    except Exception as e:
        print("Please Enter Correct Keywords\n")         
        play_again()        
    
start_game()