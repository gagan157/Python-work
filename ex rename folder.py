import os

# os.chdir("D:\Downloads")
# print(os.getcwd())
# print(os.listdir())

def solider(path,file,format):
    os.chdir(path)
    i=1
    allfiles=os.listdir(path)
    print(allfiles)
    with open(file) as f:
        #this file in folder name ,you dont want to change anything
        filelist=f.read().split("\n")

    for files in allfiles:
        #this line which folder you want to capitalize
        if files not in filelist:
            os.rename(files,files.capitalize())
    
        anpath=os.path.splitext(files)[1]
        if anpath==format:            
            os.rename(files,f"{i}{format}")
            i+=1       
        




def user():
    path=input("Enter the path: ")    
    file=input("Enter the file name: ")
    format=input("Emter the format: ")
    solider(path,file,format)

user()    