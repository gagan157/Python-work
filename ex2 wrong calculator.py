#Ex2 Design a calculator which will correctly solve all the problem except
# the foolowing ones: 45*3=555, 56+9=77, 56/6=4
# your program should take oprator and the two numbers as input from the user
# and then return the result   


print("What you want?")
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
    print("ERROR!!Pls Enter correct words")