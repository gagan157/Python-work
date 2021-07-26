from os import name
from requests import status_codes
from win32com.client import Dispatch
import requests
import json
    
    

# data=requests.post(url=urls,)
# json.loads()--------->  It is used to convert a json string to an dictonary
# json.dump()---------> It is used to convert a dictonary to an json string.
# josn.load()----------> It is used to read a file which contains an json object


def speak(spk):
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(spk)
    

def getnews():
    
    category=["business","entertainment","general","health","science","sports","technology"]
    for ind,cat in enumerate(category):                   
        print(f"{ind}.{cat}",end=" || ")
    
    catlog=int(input("\nWhich category you want to read news: "))
    for ind,cat in enumerate(category):
        dex=ind
        log=cat
        if catlog == dex:        
            url=f"https://newsapi.org/v2/top-headlines?language=en&country=in&category={log}&apiKey=cf0e3928ac1c47d094aa2d5153ed2828"
            break
    urls=requests.get(url)
    print(urls.status_code)
    data=json.loads(urls.text)
    # data["articles"]  
    # main=data["articles"]
    i=1
    for indexo in range(10):        
        heads=data["articles"][indexo]["title"]
        urlnews=data["articles"][indexo]["url"]
        if indexo>0 and indexo<9:
            speak("next news is")
        elif indexo==9:
            speak("last news is") 
        print(f"{i}. {heads}")        
        speak(heads)
        print("check full news: ",urlnews,end="\n\n")
        i+=1
                   
        
        
        


if __name__=="__main__":
    getnews()


   