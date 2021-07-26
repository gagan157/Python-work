#You are given few sentences as a list (Python list of sentences). 
# Take a query string as an input from the user. 
# You have to pull out the sentences matching this query inputted by the user 
# in decreasing order of relevance after converting every word in the query and 
# the sentence to lowercase. Most relevant sentence is the one with the maximum 
# number of matching words with the query.

# Sentences = [“Python is cool”, “python is good”, “python is not python snake”]
# Input:
# Please input your query string
# “Python is”
# Output:
# 3 results found:
# python is not python snake
# python is good
# Python is cool


#please reatempt this code

lis=[]
user=input("Please input your query string: ")
user=user.split(" ")

def mean(sentence):
    match=0              
    
    line=sentence.split(" ")
    for use in user:
        for word in line:
            if use.lower()==word.lower():
                match+=1
                    
    return match
#                 lis.append(lines)
# lis.reverse()
# print(f"{match} results found:")
# # for li in lis:
# print(lis)
# for sentScore in sorted(zip(match, sentences), reverse=True):
#     if sentScore[0] !=0:
#         print(sentScore)
sentences = ["Python is cool","python is good", "python is not python snake"]
scores = [mean(sentence) for sentence in sentences]
# print(scores)

sortedSentScore = [sentScore for sentScore in sorted(
        zip(scores, sentences), reverse=True) if sentScore[0] !=0 ]

print(len(sortedSentScore))
for match,val in sortedSentScore:
    print(val)

