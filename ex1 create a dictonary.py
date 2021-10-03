#ex1 create a dictonary and take the input from the user and return the meaning of words:
# json.loads()--------->  It is used to convert a json string to an dictonary
# json.dump()---------> It is used to convert a dictonary to an json string.
# josn.load()----------> It is used to read a file which contains an json object
import json
import requests

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

querystring = {"term":"table"}

headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "ddeccbe1f3msh650612f7533c589p1175dajsn272f108ae4df"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data=json.loads(response.text)
dics=data["list"]
for da in dics:
        print(da['definition'] ," ")

















worddic={"immutable":"meaning is cantnot change the value ex tuple","muttable":"meaning is can change the value",
        "Gagan":"that name meaning is sky","pc":"this world meaing is personal computer"}

#note : check how to typecast tuple to dict
# def dic_lower(user_key):
#         for key_word,val_mean in worddic.items():
#                 key_word_up=key_word.upper()
#                 val_mean_up=val_mean.upper()
#                 if key_word_up==user_key:                          
#                         return key_word_up,val_mean_up   
                
                       
        
# if __name__=="__main__":
#         try:
#                 print("Dictionary")        
#                 print("Enter the word :")
#                 user_key=input()
#                 user_key_up=user_key.upper()
#                 key_lower,value_upper=dic_lower(user_key_up)                               
        
#                 print(f"{key_lower} : {value_upper}")
#         except Exception as e:
#                 print("This word is not availble in our Dictionary")      
               
                






                            
                