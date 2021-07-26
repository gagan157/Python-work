import random

def nameslpit(fullnamelist):
    firstnameli=[]
    lastnameli=[]
    for fullnam in fullnamelist:
        firstname=fullnam.split(" ")[0]
        lastname=fullnam.split(" ")[1]
        firstnameli.append(firstname)
        lastnameli.append(lastname)
    swaplastname(firstnameli,lastnameli)  

#random last name concatinate to first name
def swaplastname(firstnameli,lastnameli):
    crefullname=[]
    lastname=[last for last in lastnameli]
    print(lastname)
    for fname in firstnameli:   
        lname=random.choice(lastname)     
        fullname=fname+" "+lname
        crefullname.append(fullname)
        lastname.remove(lname)
    print(crefullname)





if __name__=="__main__":
    namecount=int(input("Enter number of friends:"))
    fullnameli=[]
    for name in range(namecount):
        fullname=input(f"Enter the name of your {namecount} friends:")
        namecount-=1
        fullnameli.append(fullname)
    nameslpit(fullnameli)    