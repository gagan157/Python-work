#Ex 5 craete files function health management take 3 client make 6 file 3 food or 3 excersice file,client name(Harry,rohan,hammad)
def getdate():
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
    print("Pls Enter the correct number")