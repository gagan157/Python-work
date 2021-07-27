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


