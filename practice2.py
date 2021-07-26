try:
    user_apple=int(input("Enter the number of apple: "))
    min_max=input("Enter the number of min and max: ")
    lis=[]
    inte=min_max.split(" ")    
    for all in inte:
        if len(all)!=0: 
            allint=int(all)        
            lis.append(allint)    
    # print(lis)
    for i in range(lis[0],lis[1]+1):
        if user_apple%i==0:
            print(f"{i} is a divisor of {user_apple}")       
        else:
            print(f"{i} is not a divisor of {user_apple}")

except Exception as e:
    print("Enter valid number")


