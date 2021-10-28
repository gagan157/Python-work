import re
import requests
from bs4 import BeautifulSoup

url="https://matrix.abor.com/Matrix/Public/Portal.aspx?ID=0-1717879991-10#1"
response=requests.get(url)

htmlcnt=response.content

soup = BeautifulSoup(htmlcnt,'html.parser')

def web_scap():
    data = {}
    file_name="MLS_web_scraping.txt"
    with open(file_name,"w" ,encoding="utf-8") as crefile:
        
        for alls in soup.find_all('div',attrs={'class':'row d-paddingTop--6 d-paddingBottom--6 d-bgcolor--systemLightest d-marginBottom--4 d-marginLeft--4 d-marginRight--4 d-marginTop--4'}): 
            image = alls.find('img',attrs={'img-responsive ivrImg'})
            img=image.get('src')
            data.update({'img':img})

            p=alls.find('span',attrs={'d-text d-fontSize--largest d-color--brandDark'})
            pri=str(p.text)
            data.update({'pri':pri})

            statuss=alls.find('span',attrs={'Status_ACT'})
            sts=str(statuss.text)
            data.update({'status':sts})

            mls=alls.find('span',attrs={'d-text d-fontWeight--bold d-paddingRight--4'})            
            if mls is not None:                
                code = f"{str(mls.text)} {str(mls.next_sibling.text)}"
                data.update({'code':code})
                
            add = alls.find('div',attrs={'col-sm-12 d-fontSize--largest d-text d-color--brandDark'})
            address =str(add.a.text)
            data.update({'add':address})

            add_bot=alls.find('div',attrs={'col-sm-12 d-fontSize--small d-textSoft d-paddingBottom--8'})
            addressbot=str(add_bot.text)
            data.update({'add_bot':addressbot})
           

            info = alls.find_all('div',attrs={'class':'col-xs-6 J_sect'})
            bed=info[0].text
            bath=info[1].text
            sqft=info[2].text
            yearbult=info[3].text
            acres=info[4].text
            data.update({'bed':bed})
            data.update({'bath':bath})
            data.update({'sqft':sqft})
            data.update({'yearbult':yearbult})
            data.update({'acres':acres})
            
               
            for dat in data:                   
                
                crefile.write(f'{dat} = {data[dat]}, \n')
                if dat == 'acres':
                    crefile.write(f'============================================\n')
            print("Sucess")    
               

       
            
        
    
if __name__=='__main__':
    web_scap()