n=5
i=1
#row 1 to n
# while i<=n:
#     j=1
#     #column 1 to n+1-i
#     while j<=(n+1)-i:
#         print(j,end=" ")
#         j+=1
#     print("")
#     i+=1

#output:
#1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
     
## ==========================================
# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end=" ")
#         j+=1
#     print("")
#     i+=1

# #output:
# #1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5     

## ===========================================
# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         if (i+j)%2==0:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#         j+=1    
#     print("")
#     i+=1

# #output:
# # 1
# # 0 1
# # 1 0 1
# # 0 1 0 1
# # 1 0 1 0 1    

##===========================================

# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=n-i:
#         print(" ",end=" ")
#         j+=1
#     j=1    
#     while j<=n:        
#         print("*",end=" ")    
#         j+=1
#     print("")
#     i+=1   

# #output:
# #         * * * * *
# #       * * * * *
# #     * * * * *
# #   * * * * *
# # * * * * *

#========================================
# n=5
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print("*",end=" ")
#         j+=1
#     print("")     
#     j=1
#     while j<=i:
#         print(" ",end=" ")
#         j+=1    
#     i+=1  

#output:
# * * * * * 
#   * * * * *
#     * * * * *
#       * * * * *
#         * * * * *     

#=======================================



# n=5
# i=1
# while i<=n:    
#     j=1
#     while j<n+1-i:
#         print(" ",end=" ")
#         j+=1
#     j=1    
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print("")    
#     i+=1

# output:
#         * 
#       * *
#     * * *
#   * * * *
# * * * * *

# ===============================================

# n=5
# i=1
# while i<=n: 
#     j=1
#     while j<=n+1-i:
#         print("*",end=" ")
#         j+=1
#     print("")
#     j=1    
#     while j<=i:
#         print(" ",end=" ")
#         j+=1           
#     i+=1

# output:
# * * * * * 
#   * * * *
#     * * *
#       * *
#         *    

# ====================================
# need:
# 1234*1234
# 123* *123
# 12* * *12
# 1* * * *1
# * * * * *


# n=5
# i=1     
# while i<=n:        
#     j=1
#     while j<=n+1-i:
#         print(" ",end=" ")
#         j+=1  
#     j=1     
#     while j<=i:    
#         print("*",end=" ")
#         j+=1 
                    
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j+=1
#     print("")
#     i+=1



# using forloop
#Normal shape of star without front space 
us=11
"""for i in range(us):
    for j in range(i):
        print("*",end="")
    print()   
for i in range(us):
    # print("row")         
    for counter in range(us,0,-1):   
        #print col 
        print("*",end="")          
    print()
    us-=1   """   
        

#Star shape whith front of space 
"""for i in range(us):
    for j in range(us,i,-1):    #first space in coloumn run like dicrement
        print(' ',end="")   
               
    for colo in range(i+1):     #and print *  run like increment
        print("*",end="")
                        #end line col
    print() 

for i in range(us):
    for colo in range(i+1):     #first space run increment in coloum
        print(" ",end="")
    for j in range(us,i,-1):    #second decrement star
        print('*',end="")     
               
    print()"""




#Dimond Shape of star pattern 
    

"""for i in range(us):
    for j in range(us,i,-1):    #first space in coloumn run like dicrement
        print(' ',end="")   
               
    for colo in range(i+1):     #and print *  run like increment
        print("*",end="")
                        #end line col

    #another part
    for j in range(i):
        print("*",end="")

    print() 

for i in range(us):
    for colo in range(i+1):     #first space run increment in coloum
        print(" ",end="")
    for j in range(us,i,-1):    #second decrement star
        print('*',end="")     

    for counter in range(us,i+1,-1):   
#         #print col 
        print("*",end="")                   
    print()"""



# for row in range(1,5+1,1):
#     for col in range(1,row+1):
#         print(col,end="")  #print row or col
#     print()    

# k=1
# for row in range(5):
#     for col in range(5-row,0,-1):
#         print(col,end="")
#     k+=1
#     print()    