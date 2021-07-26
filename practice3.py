
lis=[1,2,3,4]
lis2 = lis[:]
#reverse list using inbild method
def reverso():
    lis2.reverse()
    print("method list",lis2)
reverso() 

#reverse list using slicing
def slireverce():    
    all=lis[ : :-1]
    print("slice list",all)
slireverce()  

#reverse list using swaping forloop
def swaprevers():    
    # li=lis[0]
    # lis[0]=lis[-1]
    # lis[-1]=li
    for i in range(len(lis)//2):
        lis[i],lis[len(lis) -i -1] = lis[len(lis) -i -1],lis[i]
        
    print("swap method",lis)
swaprevers()    
         
