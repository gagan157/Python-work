import abc
import random
import time
import datetime
import math
import re
from tkinter.constants import ALL, CURRENT, FIRST, X #for gui
import numpy#for mathmatic 
import pendulum as pp# hadle to time
import pyperclip #copy pase
from emoji import emojize
import sys #this is similar to break statament
from urllib.request import urlopen  #Handle to url 
import turtle
import pytube
from pytube import YouTube  #this for download video on youtube
import pygame

"""video_url = 'https://youtu.be/YjjLZpeIEN8?list=LL'   
youtube = pytube.YouTube(video_url)  
video = youtube.streams.first() 
video.download('E:/')
print(video.title) """ 


   

print(emojize(":thumbs_up:"))

"""myTurtle = turtle.Turtle()
myWin = turtle.Screen()
  
# Turtle to draw a spiral
def drawSpiral(myTurtle, linelen):
    myTurtle.forward(linelen)
    myTurtle.right(90)
    drawSpiral(myTurtle, linelen-10)
  
drawSpiral(myTurtle, 90)
myWin.exitonclick()"""





  
 





"""def randomnum():
    print('Enter the Number : ')
    user=int(input())
    time.sleep(1)
    print('This is the random number: ',random.randint(1,user))

randomnum()"""


"""def swapnumber():
    print('Enter the two number')
    user1=int(input())
    user2=int(input())
    print("your first number %s and Second number is %s"%(user1,user2))
    time.sleep(1)
    user1,user2=user2,user1
    print("Now After Swaping your first number {0} and Second number is {1}".format(user1,user2))

swapnumber()"""    

"""def Red():
    a=1
    def Blue():
        global b
        b=2        
        print(a)
        print(b)
    Blue()
    print(a)
    print(b)
Red() """

"""def removevow():
    print('Enter yhe letter :')
    user=input()
    s=''
    for letter in user:
        if letter not in ['a','e','i','o','u'] : s+=letter
    time.sleep(1)    
    print(s)

removevow()"""      

"""def vadid_password():
    print('Enter ther password ')
    p=input()
    x=True
    while x:
        if len(p)<6 or len(p)>12:break
        elif not re.search("[a-z]",p):break
        elif not re.search("[A-Z]",p):break
        elif not re.search("[0-9]",p):break
        elif not re.search("[@$!$]",p):break
        elif re.search("\s",p):break
        else:
            print("valid password")
            x=False
            break
    if x: print("password not valid")    

vadid_password()""" 


"""def winnum(numbers):
    winner=numbers[0]
    for num in numbers:
        if num>winner:
            winner=num
    print(winner)

winnum([5,4,7,6,3,55,6,8,1])"""

"""def double(a,b):
    #true=1 and false=0 in integer
    red=(1+int(a==2*b))*(a+b)    
    print(red)
double(2,3) """


"""two,three=2,3
print("two" if two>three else "three")"""

"""def modren_sum(a,b):
    print(100 if (a+b>=9)and(a+b<=18)else a+b)
modren_sum(8,2)"""    

"""myself=("Gagan is a good boy")
print(len(myself))
print(myself[-8::2])

mylist=[2,4,3,5,3,2,4]
myseclist=["red"]
print(mylist[1:4])
mylist.sort()
print(mylist)
mylist.append(50)
print(mylist)
mylist.insert(1,60)
print(mylist)

mylist.extend(myseclist)
print(len(mylist))
print(mylist)
print(mylist[1],mylist[8])"""

"""dict={"Gagan":{"bk":"Oats","ln":"roti,rice","dn":"fish or panner"}}

dict["rahul"]={"bk":"parathas","ln":"allo","dn":"pizza"}
#print(dict)
#print(dict["rahul"])
#print(dict.keys())
#print(dict.items())
dict.update({"leena":"toffe"})
#print(dict)

for x in dict.items():
    print(x)"""

#ex1 create a dictonary and take the input from the user and return the meaning of words:

"""worddic={"immutable":"meaning is cantnot change the value ex tuple","muttable":"meaning is can change the value",
        "Gagan":"that name meaning is sky","pc":"this world meaing is personal computer"}
print("Enter the word :")
user=input()
b=user.capitalize()
print(worddic.get(b))
print(worddic[b])"""

#ifelse challange
"""print("Enter your age: ")
user=int(input())

if user<18:
    print(f"Your age({user}) is lower than 18 so you cannot Drive")
    print("Come back when your age is 18+ Thankyou")
elif user>18:
    print("Your age is Limited" if user>80 else "Gotit")
    print(f"your age is {user} Congrats!,Now you can drive")


else:
    print(f"You age is {user},Come to offiice and meet to officer and than he make dicided you drive or not Thank you")    """    


 #Ex2 Design a calculator which will correctly solve all the problem except
 # the foolowing ones: 45*3=555, 56+9=77, 56/6=4
 # your program should take oprator and the two numbers as input from the user
 # and then return the result   

  
"""print("What you want?")
print("Press!","Add,","+,","A,","a")
print("Press!","Multiply,","*,","M,","m")
print("Press!","Divide,","/,","D,","d")
x=input()
z=x.capitalize()
if z=="Add" or z=="+"or z=="A":
    print("Adding...")
    print("Enter the first number:")
    num1=int(input())
    print("Enter the second number:")    
    num2=int(input())
    num3=num1+num2
    if num1==56 and num2==9 or num2==56 and num1==9:
        print("FAULTY!!!")
        print(num1,"+",num2,"=","77")
    else:
        print(num1,"+",num2 ,"=", num3)    
elif z=="Multiply" or z=="*" or z=="M":
    print("Mutipling...")
    print("Enter the first number:")
    num1=int(input())
    print("Enter the second number:")    
    num2=int(input())
    num3=num1*num2
    if num1==45 and num2==3 or num1==3 and num2==45:
        print("FAULTY!!!")
        print(num1,"*",num2,"=","555")
    else:    
        print(num1,"*",num2 ,"=", num3)
elif z=="Divide" or z=="/" or z=="D":
    print("Dividing...")
    print("Enter the first number:")
    num1=int(input())
    print("Enter the second number:")    
    num2=int(input())
    num3=num1/num2
    if num1==56 and num2==6 or num1==6 and num2==56:
        print("FAULTY!!!")
        print(num1,"/",num2,"=","4")
    else:    
        print(num1,"/",num2 ,"=", num3)
        
else:
    print("ERROR!!Pls Enter correct words")"""

#forlopp challage

"""Beverage=["cars","plane",4,"foods",8,40,"bikes",1,22,56,32]      

for item in Beverage:
    #print(type(item))
    #if type(item)==int and item>6:
    #   print(item)
    #another way
    if str(item).isnumeric() and item>6:
        print(item)"""
"""i=1
while (True):
    if i+1<5:
        i=i+1
        continue
    print(i+1 ,end=" ")
    if i==14:         
        break    
    i=i+1 """
              

"""while(True):
    print("Enter the number :")
    x=int(input())
    if x<100:
        continue
    elif x==100:
        continue
    else:
        print("congo! you got it")
        break"""


 #ex3 create game guesses the no n=18
 # no of guesses 9
 # print no of guesses left
 # no of guesses he took to finish
 # game ove and win the game       

"""x=input("Plese press 'S' for Enter the game :\n")
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
    print("Enter the correct letter")"""

#Operators that Python Language supports are:

#Arithmetic Operators
#Assignment Operators
#Comparison Operators
#Logical Operators
#Identity Operators
#Membership Operators
#Bitwise Operators    

#Arithmetic Operators:
#Basic mathematical operations such as addition, multiplication, subtraction, division, etc. are performed with the 
# help of arithmetic Operations. It contains nearly all operations that we can perform with the help of a calculator. 
# Symbols for such operators include *, /, %, -, //, etc.

#Assignment Operators:
#The assignment operator is used to assign values to a variable. In some cases, we have to assign a variable’s 
#value to another variable, in such cases the value of the right operand is assigned to the left operand. One of 
#the basic signs from which we can recognize an assignment operator is that it must have an equal-to(=) sign. Some 
#commonly used assignment operators include +=, -=, /=, etc.

#Comparison Operators:
#They are also known as relational operators. They compare the values on either side of the operator and decide the relation
# among them. Commonly used comparison operators include ==, >, < , >=,etc.

#Logical Operators:
#Logical operators perform logical AND, OR and NOT, operations. They are usually used in conditional statements to join multiple 
#conditions. AND, OR and NOT keywords are used to perform logical operations.

#Identity Operations:
#Identity operator checks if two operands share the same identity or not, which means that they share the same location 
#in memory or different. “is” and “is not” are the keywords used for identity operands.

#Membership Operands:
 #Membership operand checks if the value or variable is a part of a sequence or not. The sequence could be string, 
 #list, tuple, etc. “in” and “not in” are keywords used for membership operands.

#Bitwise Operand:
#Bitwise operands are used to perform bit by bit operation on binary numbers. First, we have to change the format of the number 
#from decimal to binary and then compare them using AND, OR, XOR, NOT, etc.

"""a=6
b=4
c=sum((a,b))
print(c)

def avreage(a,b):
    # This is not comment This is Docstring mean function in string line calling doc string
    ave=(a+b)//2
    return ave"""

"""v=avreage(4,6)
print("yo",v)
print(avreage.__doc__)"""

#try Exaption
"""try:
    print("Ente num")
    a=int(input())
    print("Ente num")
    b=input()

    print("this is your total :",a+b)
except Exception as e:
    print(e)"""

#r : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.
#w : w mode does not concern itself with what is present in the file. It just opens a file for writing and if there is already some data present in the file, it overwrites it.
#x : x is used to create a new file. It does not work for an already existing file, as in such cases the operation fails.
#a : a stands for append, which means to add something to the end of the file. It does exactly the same. It just adds the data we like in write(w) mode but instead of overwriting it just adds it to the end of the file. It also does not have the permission of reading the file.
#t : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals with the file data as a string.
#b : b stands for binary and this mode can only open the binary files, that are read in bytes. The binary files include images, documents, or all other files that require specific software to be read.
#+ : In plus mode, we can read and write a file simultaneously. The mode is mostly used in cases where we want to update our file. 
   
        
#how too read the file content
"""file=open("testing_file.txt","rt")
#txt=file.read()
#txt1=file.readline()
#txt2=file.readline()
#txt=file.readlines()
for line in file:
    print(line,end="")

file.close()"""

"""#write mode this is create new file or u can write same file
file=open("testing_file1.txt","r+")
txt=file.read()
print(txt)#print only number of character when you wite mode is on
txt=file.write("Thankyou")
print(txt)
file.close()"""


#ex4 star pattern
"""print("Enter the number :")
n=int(input())
print("Enter the bool value 0 or 1:")
x=int(input())
z=bool(x)  
if z==True and x<=1:
    i=1
    while i<=n:
        j=1
        while j<=i:
            print("*",end=" ")
            j+=1
    
        print("")    
        i+=1
elif z==False and x<1:         
    i=1
    while i<=n:
        j=n
        while j>=i:
            print("*",end=" ")
            j-=1
        print("")    
        i+=1
else:
    print("please enter correct bool like 0 or 1") """
#=========or======================
"""a=int(input("enter the row number: "))
b=1
while b<=a:
    print("*"*b)
    b=b+1
x=1
while a>=x:
    print("*"*a)
    a=a-1  """

#wiith block function automacally close
"""with open("testing_file1.txt") as f:   
            txt=f.read()
            print(txt)

f=open("testing_file1.txt")
txt=f.read()
print(f.tell()) #tell is where is file pointer
# print(f.seek(0)) #file pointer reset
print(f.readline())
print(txt)
print(f.tell())
f.close()"""


#Ex 5 craete files function health management take 3 client make 6 file 3 food or 3 excersice file,client name(Harry,rohan,hammad)
"""def getdate():
    import datetime
    return datetime.datetime.now()

def userdata(name,food):
    if name=="Harry":
        if food=="food":
            filefood="HarryFood.txt"
            data=filefood
        else:    
            fileexe="HarryExercise.txt"
            data=fileexe

        readwrite(data,food)        
        return data

    elif name=="Rohan": 
        if food=="food":
            filefood="RohanFood.txt"
            data=filefood
        else:    
            fileexe="RohanExercise.txt"
            data=fileexe

        readwrite(data,food)        
        return data 

    elif name=="Hammad":
        if food=="food":
            filefood="HammadFood.txt"
            data=filefood
        else:    
            fileexe="HammadExercise.txt"
            data=fileexe

        readwrite(data,food)        
        return data
    else:
        print("Your Name is not valid pls contect Admin")

def readwrite(data,food):
    if user==1:
        writedata(data,food)       
    
    else:
        readuser(data,food)        

def writedata(data,food):
    if food=="food":
        with open(f"{data}","+a") as f:
            # hour=getdate().hour()
            # min=getdate().minute()            
            now=getdate().strftime("%H:%M:%S")
            dates=getdate().strftime("%d-%m-%y")
            nowtimess=str(input("Enter the time : "))
            print("Enter your eating food: ")
            userw=input()           
              
            v=str(f"Today date: {dates}\ncurrunt time : {now}\nFood Time : {nowtimess}\nYour Entry: {userw}\n\n")
            f.write(v)

    else:
         with open(f"{data}","+a") as f:
            now=getdate().strftime("%H:%M:%S")
            dates=getdate().strftime("%d-%m-%y")
            nowtimess=str(input("Enter the time : "))            
            print("Enter your Exercise: ")
            userw=input()
            v=str(f"Today date: {dates}\ncurrunt time : {now}\nFood Time : {nowtimess}\nYour Entry: {userw}\n\n")
            f.write(v)

def readuser(data,food):
    if food=="food":
        with open(data) as f:
            contant=f.read()
            print(contant)
    else:
        with open(data) as f:
            contant=f.read()
            print(contant)    
       
    
      
print("What you want log(write) or retrieve(read old data) :")
print("press 1 for log \npress 2 for retrieve\n")
user=int(input())
if user==1:
    print("What you want? Entry food or Exercise :")
    print("press 1 for food\npress 2 for Excercise")
    user1=int(input())
    if user1==1:
        print("!Welcome To Food Creation!\nBalance your Diet\n")
        print("Enter client Name: ")
        usern=input()
        newusern=usern.capitalize()
        f="food"
        userdata(newusern,f)
        print("Your Entry Sucessfully Done!")
    elif user1==2:
        print("!Wecome To Exercise Area!\nMaintain your Fitness")
        print("Enter client Name:")
        usern=input()
        newusern=usern.capitalize()
        f=""
        userdata(newusern,f)
        print("Your Entry Sucessfully Done!")
    else:
        print("Wrong Number! Try again")    
elif user==2:    
    print("What you want Acesses to Data? food or Exercise :")
    print("press 1 for food\npress 2 for Excercise")
    user1=int(input())
    if user1==1:
        print("!Welcome To Food Creation!\nCheck your Diet\n")
        print("Enter Cliet Name:")
        usern=input()
        newusern=usern.capitalize()
        f="food"
        userdata(newusern,f)
    elif user1==2:
        print("!Wecome To Exercise Area!\nCheck your Excerice")
        print("Enter Client Name:")
        usern=input()
        newusern=usern.capitalize()
        f=""
        userdata(newusern,f)
    else:
        print("Wrong Number! Try again")
else:
    print("Pls Enter the correct number")"""      



#factorial series :
"""fab=1
def fabwhile():
    user=int(input("Enter fan no: "))
    n=1
    while user>=1:
        n=n*user    
        user=user-1
    print(n)      
fabwhile()   """

"""def fabfor():
    fab=1
    user=int(input("Enter the fab no: "))
    for i in range(user):
        fab=fab*(i+1)
    print(fab)
fabfor()  """    
#recursive factorial
"""def recursion(n):

       
    if n==1:
        return 1
    else:
        return n*recursion(n-1)

number=int(input("Enter the fab: "))
print(recursion(number)) """

#fabonanchi

"""def fab(n):#8
    a=0
    b=1
    # n=int(input("Enter the num:"))

    # print(a)
    # print(b)
    #foor loop
    for i in range(0,n):        
        c=a+b        
        a=b
        b=c  
    return "This is forloop",c
          
    #while loop
    i=1
    while i<=n:
        c=a+b
        a=b
        b=c
        i+=1      
    return "This is while loop",c
    #if else recursion
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fab(n-1)+fab(n-2)            
number=int(input("enter the num: "))       
print(fab(number))"""


#star pyramind using for loop:
"""n=int(input("Enter the name: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    """

#lamda function or anonymous function:
# lamda is a one liner function ,this is call also amnoymous function ex:
"""lam= lambda x,y:x-y

print(lam(4,6))
"""

"""
listss=['6',"cars","plane",4,"foods",8,40,"bikes",1,22,56,32]



for updown in listss:
    # if type(updown)==int:
    #     res=updown
    #     print(res)
        if str(updown).isnumeric():
            y=(updown)
            # x=sorted(y)
            x=''.join(sorted(str(y)))                 
            print(x)"""




#ex6 Game Snake gun water whos win like rock paper siser #remider when com and you score equal then game tie
"""def gun_wat_snk():
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
    
start_game()"""  

# *args and **kwargs  this parameter pass in function and acces to list,dict..etc ..ex

"""def arg_kwfunction(normal,*any,**kwarg):
    print(normal)
    for i in any:
        print(i)
    for keys,values in  kwarg.items():
        print(keys,":",values)    
    print(type(any))
    print(type(kwarg))


lists=["Gagan","Harry","Simran","Pooja"]
dicts={"Gagan":"Programer","Harry":"op Programer","Simran":"Cook","Pooja":"Fashion Designer"}
normal="This is normal"    
arg_kwfunction(normal,*lists,**dicts)
"""

#time 12hour and 24hour
"""date_time = time.strftime("%d %m %Y %I:%M %p") #12hour
now=time.asctime(time.localtime())    #24hour

print(date_time)
print(now)
print(type(now))"""
#lamda
"""mi=lambda x,y: x%y
print(mi(5,2))
"""
#enumrate
"""vehicals=["Car","Bike","Cycle","moppad","Truck"]
i=1
for item in vehicals:
    if i%2 is not 0:#odd number
        print(item)
    i+=1"""
#or with enumerate
"""for keys,values in enumerate(vehicals):
    if keys%2==0:
        print(values)
i=1
for i in range(1,10):
    if i%2!=0:
        print("odd numbers",i)
    elif i%2==0:
        print("Even numbers",i)
"""


#Healthy program Reminder
#time duration 9am - 5pm
# water - water.mp3 (3.5liter) off to input drank - create log with time and date
# Eye -eye.mp3 Every 30 min play - of eydone - log
# physical activity - phicical.mp3 every 45min exdone-log
#1liter=1000ml

"""def cur_time():
    current_t=datetime.datetime.now()
    hours=int(current_t.strftime("%I") )  
    mins=int(current_t.strftime("%M"))
    secs=current_t.strftime("%S")
    a_pm=current_t.strftime("%p")        
    c_time=f"{hours}:{mins} {a_pm}"
    return c_time




def set_alarm(user_hours,user_mins,user_a_pm):
    current_t=datetime.datetime.now()
    hours=int(current_t.strftime("%I"))   
    mins=int(current_t.strftime("%M"))
    secs=current_t.strftime("%S")
    a_pm=current_t.strftime("%p")
    user_hours-=hours
    user_mins-=mins
    hours+=user_hours
    mins+=user_mins
    user_a_pm    
    cu_time=f"{hours}:{mins} {user_a_pm}"
    return cu_time


# increment_time =in_timein()
def remind_me(): #improve
    print("Note set time how much you need rest like 5min 1hour ..")
    user_ho=int(input("Enter the Hour : "))
    user_mi=int(input("Enter the minit : "))
    am_pm=input("Enter AM||PM : ")
    user_am_pm=am_pm.upper()
    se_a=set_alarm(user_ho,user_mi,user_am_pm)
    set_alarms=se_a
    while True:   
        
        file="retro-game-emergency-alarm.wav"
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file)        
     
        
        current_time=cur_time() 
        i=1      
        if i<=10:
            if current_time==set_alarms:
                pygame.mixer.music.play()        
                print("Wake-up")
                query=input("Enter to stop alaram: ")  
                                              
                if query == 'p':
  
                    # Pausing the music
                    pygame.mixer.music.pause()     
                elif query == 'r':
  
                    # Resuming the music
                    pygame.mixer.music.unpause()
                elif query == 's':
  
                    # Stop the mixer
                    pygame.mixer.music.stop()
                    break      

def play_music():
    file="retro-game-emergency-alarm.wav"
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while True:
        a=input()
        if a=='stop':
            pygame.mixer.music.stop()
            print("Thank you")
            break
def user_log(log):
    with open("userexe.txt","a") as f:        
        f.write(f"{time.asctime()}={log}\n")
if __name__=="__main__":
    def water_intake():
        liter=1000
        total_drank=3500
        glass=300
        cup=100
        bottle=800
        water_drank=time.time()
        eye_exe= time.time()
        pyc_exe=time.time()     
        water_sec=30
        eye_sec=5
        pyc_sec=20       
        while True:
            int_water=time.time()
            int_eye=time.time()
            int_pyc=time.time()
            if int_water-water_drank > water_sec: 
                print("Drink water")
                play_music()
                user_log("Done Drank water")
                water_drank=time.time()
            if int_eye-eye_exe > eye_sec: 
                print("Eye Excercise")
                play_music()
                user_log("Done Eye Exerice")
                eye_exe=time.time()
            if int_pyc-pyc_exe > pyc_sec: 
                print("Pysical Exersice")
                play_music()
                user_log("Done Pysical Exersice")
                pyc_exe=time.time()         
        
    
water_intake()"""

#decoration
"""def deco(func):
    def exu():
        print("re bosdike")
        func()
        print("o bete re moj kar di")
    return exu

@deco
def bete():
    print("beteeee")
bete() """               

     
        
    
    






    



# i=1
# while i<10:
#  pygame.mixer.music.play()
#  time.sleep(4)
#  i+=1

    # if query == 'p':
  
    #     # Pausing the music
    #     pygame.mixer.music.pause()     
    # elif query == 'r':
  
    #     # Resuming the music
    #     pygame.mixer.music.unpause()
    # elif query == 'e':
  
    #     # Stop the mixer
    #     pygame.mixer.music.stop()
    #     break

   


"""class Employee:
    department='IT'
    location='Delhi'

    #class contructor
    def __init__(self,aname,asalary,arole) -> None:
        self.name=aname
        self.salary=asalary
        self.role=arole
        


    #class method
    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary}"

    @classmethod
    def change_dp(cls,change_depa):
        cls.department=change_depa
        pass   

    @classmethod
    def in_str(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def stat_p(stri):
        print(f"This is static method {stri}")    

rahul=Employee("Rhul",56666,"programmer")
rahul.stat_p("yo")
Employee.stat_p("OP")
       
class programmer(Employee): 

    def __init__(self, aname, asalary, arole, alanguage) -> None:
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.language=alanguage


    def printemprole(self):
        return f"hi my name is {self.name} and my salary is {self.salary} and my role is {self.role},\nthis is my skill :{self.language},i live in {self.location}" """       



# mukesh=programmer('mukesh',555,'enginer',['python','c++',"C",'javascript'])
# print(mukesh.printemprole())

# gagan=Employee('gagan',10000,'programmer')
# gagan.change_dp(25) 
# #or
# Employee.change_dp(35)
# print(Employee.department)

# komal=Employee.in_str("komal-50000-cook")
# print(komal.salary)

# gagan.stat_p('yo')
# gagan.name='Gagan'
# gagan.salary=1000000
# gagan.role='Best Programer'
# gagan.department='markting'
# print(gagan.department)

# print(Employee.department)
# Employee.department='salesman'
# print(Employee.department)
# print(gagan.department)

# print(gagan.printdetails())
# print(gagan.salary)


# a = int(input('Give amount: '))

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# print(fib(a))

# number = int(input("Enter the number:"))
# def Factorial_gen(n):
#     fac = 1
#     for i in range(n):
#         fac = fac * (i + 1)
#         yield fac
#     # return fac
# print(Factorial_gen(number))

"""def com():
    user=int(input("how much item to add: "))    
    userwhich=input("Which Comprehensions to use: ")  
    

    if userwhich == "list":
        print("List")      
        listitem=[]
        for i in range(user):
            item=input("Enter item: ")
            listitem.append(item)    
        lista= [a for a in listitem] 
        print(lista)
        print(type(lista))
    elif userwhich == "set":
        print("Set")      
        setlist={''}
        for i in range(user):
            item=input("Enter item: ")
            setlist.add(item)
        seta= {a for a in setlist}
        print(seta)
        print(type(seta)) 
    elif userwhich == "dict":
        print("Dict: use ex:ex")      
        dictlist={}
        for i in range(user):
            item=input("Enter item: ")
            keyss=item.split(":")[0]
            valuess=item.split(":")[1]
            dictlist[keyss]=valuess            
        seta= {key:val for key,val in dictlist.items()}
        print(seta)
        print(type(seta))
    #Not work
    elif userwhich == "gen":
        print("Gentrator")      
        genlist=()
        for i in range(user):
            item=input("Enter item: ")
            # genlist.__add__(item)
        seta= (a for a in genlist)
        print(seta)
        print(type(seta))        
             

com()        """



# Meta Characters
# [] A set of characters
# \ Signals a special sequence (can also be used to escape special characters)
# . Any character (except newline character)
# ^ Starts with
# $ Ends with
# * Zero or more occurrences
# + One or more occurrences
# {} Exactly the specified number of occurrences
# | Either or
# () Capture and group
# Special Sequences
# \A Returns a match if the specified characters are at the beginning of the string
# \b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

# \d Returns a match where the string contains digits (numbers from 0-9)
# \D Returns a match where the string DOES NOT contain digits
# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character
# \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# \W Returns a match where the string DOES NOT contain any word characters
# \Z Returns a match if the specified characters are at the end of the string


"""string=input("Enter value for addition : ")
store=0
string_split=string.split(" ")

# for i in range(0,len(string_split)):
#     string_split[i]=int(string_split[i])
#     alldata=string_split
for i in string_split:
    alldata=int(i)
    store+=alldata
print(store)
print(type(store))    
# sdata=sum(alldata)
# print(sdata)"""

# if divisible by 3 fizz and divisible by 5 buzz
"""user=int(input("Enter the num: "))
if user%3==0 and user%5==0:
    print("fizz buzz")
elif user%5==0:
    print("buzz")
elif user%3==0:
    print("fizz")
else:
    print(user)        """

#reverse string
"""word='cat'    
nap=""
for i in range(len(word)):
    nap+=word[len(word)-i-1]
print(nap)"""

#Add to list
"""lis1=[1,3,5,7,45,23]
lis2=[1,3,5,6,11,23]
lis3=[]


for i in range(0,len(lis1)): 
    lis3.append(lis1[i]+lis2[i])    
print(str(lis3))   """

# lt1 = [5, 10, 15, 20, 25, 30]  
# lt2 = [2, 4, 6, 8, 10, 12]  
# res_lt = [] # declaration of the list  
# for x in range (0, len (lt1)):  
#     res_lt.append( lt1[x] + lt2[x])  
  
# # Display the sum of two list in Python  
# print ( " Addition of the list lt1 and lt2 is: " + str (res_lt))





#decorater use   

'''def deco(fun):
    def inner():
        n,i=fun()
        n='gagan'
        i=40
        return n,i
    return inner    

@deco
def remo():
    name='anyname'
    ids=45
    return name,ids    

print(remo())
data=deco(remo)
print(data())'''


"""class student:
    ocuupation = "programmer"
    def __init__(self):                     #constructor
        self.class_section = 9              #instance or object variable
        print("Contructor")

    def stu(self,std_name):                 #instance method
        self.name= std_name 
        print("instance method")                
        print("my name is ",self.name,"and my class is ",self.class_section)

    @classmethod        
    def info(cls):                             #class method
        print("class method")
        print("i am a ",cls.ocuupation)

st = student()
st.info()
st.stu("gagan")"""






    


