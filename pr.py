# import subprocess

# data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
# profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
# for i in profiles:
#     results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
#     results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#     try:
#         print ("{:<30}|  {:<}".format(i, results[0]))
#     except IndexError:
#         print ("{:<30}|  {:<}".format(i, ""))
# input("")

import requests
import urllib.request
def download_video_series(video_links): 

    for link in video_links: 

        '''iterate through all links in video_links 
        and download them one by one'''

        # obtain filename by splitting url and getting  
        # last string 
        file_name = link.split('/')[-1]    

        print ("Downloading file:%s"%file_name) 

        # create response object 
        
        r = requests.get(link, stream = True) 

        # download started 
        with open(file_name, 'wb') as f: 
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    f.write(chunk) 

        print ("%s downloaded!\n"%file_name )

    print ("All videos downloaded!")
    return



link_o="https://fvs.io/redirector?token=SDBNL2lyZitWdmlSN2I2cFRBN2JCeE5ncnNqZEU3cFZualBzVXFTNHJwbjVvTGp2b0liSERySTErb0JvenRtd2xlKytyN3UzR0lEN1E5dnJ5T09jMS9Wd1dSUmkyKzNRcjZHK1ZxOGpxT2NDOStJdWJtMXhEY29DRy8xQlNKMnM4aElXTnpHanB2VUdCQnBGaUtORUFodWd4NUhhUUFFY3BEdEI6S29oZUJoUWtMcmtZcnVJU256ZDJ3UT09"
filename = link_o.split("/")[-1] 
r = requests.get(link_o,stream=True)
with open(filename, 'wb') as f: 
            for chunk in r.iter_content(chunk_size = 1024*1024): 
                if chunk: 
                    # f.write(chunk) 
                    pass