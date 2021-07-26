#all challaenges

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
import math


lam =lambda x,y: round(x/y)


print(lam(3500,300))



#multilevel inheritance
#electronic device
#pocket gedget
#phone

class Electronic_device:
    headphone='Headphone'
    bluetooth_speaker='Bluetooth speaker'
    camera='Camera'   

class Poket_gedget(Electronic_device):
    torch='Torch'
    tablet='Tablet'
    lenovo_phone='lenovo'
    def fun(self):
        return f"Electronic {self.torch} work in drak place and {self.tablet} is versy usefull"
    
class phone(Poket_gedget):
    phone=['Lenovo','Samsung','Sony','Oppo','Redmi','Micromax']

    def fun(self):
        return f"This is very good company phone {self.phone}"


emp=Electronic_device()
pk=Poket_gedget()
pon=phone()

print(pk.fun())
phone.fun
phone.bluetooth_speaker
phone.camera
phone.lenovo_phone
phone.bluetooth_speaker
