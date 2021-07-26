import pickle

#read file
with open("iris.data") as irisdata:
    alldata=irisdata.read() 
     
    #create list
bind=alldata.split()  
# print(bind)

#codewithharry solution
"""bind=alldata.split("\n")
datairis=[]
for item in bind:
    if len(item)!=0:
        new=item.split(",")
        datairis.append(new)
print(datairis) """   

#this is my solution
#create list of list
datairis=[]       
for i in bind:
    x=i.split(",")
    # print(x)         
    datairis.append(x)
print(datairis)

# create a pickle file    
with open("datalist.pkl","wb") as datalist:
    pickle.dump(datairis,datalist)
        
#load file uppickling
with open("datalist.pkl","rb") as readlist:
    redlitibj=pickle.load(readlist)    
    print(redlitibj) 
 
 
   
    
        


