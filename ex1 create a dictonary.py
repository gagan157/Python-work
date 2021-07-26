#ex1 create a dictonary and take the input from the user and return the meaning of words:
# json.loads()--------->  It is used to convert a json string to an dictonary
# json.dump()---------> It is used to convert a dictonary to an json string.
# josn.load()----------> It is used to read a file which contains an json object
import requests
import json

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
               
                






                            
                