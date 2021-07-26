import re

garbage_data="""gfgiwefiwefef
efwnweufnjwefn
efowehfhygdyuewgd
gaganrehal93@gmail.com qudhuiqwygdyuwqdq
dqwdvgqvdgqvd
dqwdqwdq komal@gmail.com qdwerewrrew ewrewriyfiuyygf
ladoosingh@yahoo.in ahjydguyqwgwdyuw hdguywgdtuw ravikumar@gmail.com"""



# data=re.compile(r'\w+\@+\S+\w')
# print(data)
# alldata=data.finditer(garbage_data)
# for matc in alldata:
#     print(matc)

# data=re.findall(r'\w+\@+\S+\w',garbage_data)
#or
data=re.compile(r'\w+\@+\w+\S+')
# print(data)
alldata=data.findall(garbage_data)
# print(alldata)
i=1
file_name="garbage_eemail_data.txt"
with open(file_name,'w') as crefile:  
    for match in alldata:
        emaildata=match      
        crefile.write(f"Emial{i} = {emaildata}\n")
        i+=1        
print("Sucessfully Done!")