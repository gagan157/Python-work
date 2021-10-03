import requests

url = "https://d7sms.p.rapidapi.com/secure/send"

payload = "{\r\n    \"coding\": \"8\",\r\n    \"from\": \"SMSInfo\",\r\n    \"hex-content\": \"00480065006c006c006f\",\r\n    \"to\": 971562316353\r\n}"
headers = {
    'content-type': "application/json",
    'authorization': "undefined",
    'x-rapidapi-host': "d7sms.p.rapidapi.com",
    'x-rapidapi-key': "ddeccbe1f3msh650612f7533c589p1175dajsn272f108ae4df"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)















# *******************************************************************************
# import requests
# import json

# url = "https://weatherapi-com.p.rapidapi.com/current.json"

# querystring = {"q":"Punjab,India"}

# headers = {
#     'x-rapidapi-host': "weatherapi-com.p.rapidapi.com",
#     'x-rapidapi-key': "ddeccbe1f3msh650612f7533c589p1175dajsn272f108ae4df"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# r=json.loads(response.text)

# name = r['location']['name']
# country = r['location']['country']
# tempc = r['current']['temp_c']
# tempf = r['current']['temp_f']
# # country = r['location']['country']
# print(r['location'])
   
