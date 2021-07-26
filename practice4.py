#Next palindrome
# A palindrome is a string that, when reversed, is equal to itself. Example of the palindrome includes:
# 676, 616, mom, 100001.
# You have to take a number as an input from the user. 
# You have to find the next palindrome corresponding to that number. 
# Your first input should be the number of test cases and then take all 
# the cases as input from the user.

# method1 :
def mthod1():
    user=int(input("Enter how much input you want: "))

    for i in range(user):
        user1=input()     
        
        # mylist.append(user1)   
        if user1.isnumeric():
            data1=int(user1)        
            while True:
                data=data1
                datarev = 0            
                while(data > 0):
                    a = data % 10
                    datarev = datarev * 10 + a
                    data = data // 10
            # print(datarev,type(datarev))
                # if data1==datarev:  
                #     print(f"Already Palindrome for {user1} is {datarev}")
                #     break                        
                if data1==datarev:
                    print(f"Next Palindrome for {user1} is {datarev}")
                    break             
                else:
                    data1+=1    
            
        else:
            data=user1[::-1]

            if user1==data:
                print(f"{user1} is Palindrome: {data}")
            else:
                print(f"{user1} is not Palindrome: {data}")    
    

#method2 
def method2():
    user=int(input("How to take to value you want: "))
    mylist=[]
    for i in range(user):
        user1=input()
        mylist.append(user1)
    
    for data in mylist:
        alldata=data
        
        #this check  loop in integer value 
        #ex alldata=123
        if str(alldata).isnumeric():
            #reverse string
            # after this method 321 in  revdata  
            revdata=alldata[::-1]
            
            if alldata==revdata:
                print(f"{alldata} This is already Palindrome {revdata}")
            #if not equal too both     
            else:
                #typecast in integer
                typecast=int(alldata)
                while True:             
                    #increment 
                    typecast+=1
                    #typecast string and value stote in strtpe
                    strtpe=str(typecast)
                    #this reverse value and store in revtydata
                    revtydata=strtpe[::-1]
                    #again equal to typecast and revtydata
                    if int(typecast)==int(revtydata):
                        print(f"Next Palindrome for {alldata} is {typecast}")
                        break 
        
        else:
            revstrdata=alldata[::-1]
            if alldata==revstrdata:
                print(f"{alldata} This is Palindrome: {revstrdata}") 
            else:
                print(f"{alldata} This is not Palindrome: {revstrdata}")

        
        

method2()    

