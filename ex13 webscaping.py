import re
import requests
from bs4 import BeautifulSoup

url="https://www.flipkart.com/audio-video/~cs-53mrbtcuf5/pr?sid=0pm&collection-tab-name=Audio+And+Video&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&fm=neo%2Fmerchandising&iid=M_a2f3918c-813f-49d4-880b-3c28a04711fc_1_372UD5BXDFYS_MC.9JGNW7M0TUHD&otracker=hp_rich_navigation_1_1.navigationCard.RICH_NAVIGATION_Electronics%7EAudio%7EAll_9JGNW7M0TUHD&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_1_L2_view-all&cid=9JGNW7M0TUHD&page=1"
response=requests.get(url)

htmlcnt=response.content

soup = BeautifulSoup(htmlcnt,'html.parser')

# for image in soup.find_all('img'):
#     print(image.get('src'))

# imagelist=[]
# namelis=[]
# pricelie=[]
def webscrap():
    eleco={}
    count=1
    for alls in soup.find_all('div',attrs={'class':'_4ddWXP'}):    
        images=alls.find('img',attrs={'class':'_396cs4 _3exPp9'})
        imu=images.get('src')
        # imagelist.append(imu)

        title = alls.find('a',attrs={'class','s1Q9rs'})
        tit=str(title.get('title'))
        # namelis.append(tit)

        prices = alls.find('div',attrs={'class','_30jeq3'})
        prc=prices.string
        prcs = str(prc)
        

        # pricelie.append(prc)

        # eleco.update({'img':imu,'title':tit,'price':prc})
        eleco['img']=imu
        eleco['title']=tit
        eleco['prices'] = prcs
        
        file_name="webscrap_data.txt"
        with open(file_name,"a" ,encoding="utf-8") as crefile:   
            
            for el in eleco:                
                key=el
                val= eleco[el]
                
                crefile.write(f"{key} = {val}\n")
                if el=='prices':
                    crefile.write("************************************\n")
            
                

            

    print("Data sucess")    
            


if __name__=="__main__":
    webscrap()
           
    


