# You are given a list that contains some numbers. 
# You have to print a list of next palindromes only if the number is greater than 10; 
# otherwise, you will print that number.

# Input:
# [1, 6, 87, 43]

# Output:
# [1, 6, 88, 44]

mylist=[1, 6, 87, 43]
lis=[]
for i in mylist:   
    if i>10:
        strlist=str(i)[::-1]
        if i==int(strlist):                    
            lis.append(i)
        else:
            while True:
                i+=1
                strlist=str(i)
                revslist=strlist[::-1]
                if int(i)==int(revslist):
                    lis.append(i) 
                    break        
    else:
        lis.append(i)

print(f"Old list {mylist}\nNew list {lis}")