# Meta Characters
# [] A set of characters
# \ Signals a special sequence (can also be used to escape special characters)
# . Any character (except newline character)
# ^ Starts with
# $ Ends with
# * Zero or more occurrences
# + One or more occurrences
# {} Exactly the specified number of occurrences
# | Either or
# () Capture and group
# Special Sequences
# \A Returns a match if the specified characters are at the beginning of the string
# \b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word

# \d Returns a match where the string contains digits (numbers from 0-9)
# \D Returns a match where the string DOES NOT contain digits
# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character
# \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# \W Returns a match where the string DOES NOT contain any word characters
# \Z Returns a match if the specified characters are at the end of the string
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
# with open(file_name,'r') as readda:
#     emaildata=readda.read()
#     print(emaildata)