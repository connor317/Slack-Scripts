import requests
import json
url = "https://slack.com/api/pins.list"
querystring = {"channel":"<your channel ID here>"}
headers = {
    'Authorization': "Bearer <your API Token Here>",
    'User-Agent': "PostmanRuntime/7.16.3",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "<your postman token here>",
    'Host': "slack.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    
response = requests.request("GET", url, headers=headers, params=querystring)
response = response.json()['items'][0]['message']['reactions']

present = []
for reaction in response:
    for user in reaction['users']:
        if user not in present:
            present.append(user)
            
url = "https://slack.com/api/users.list"
attendance = []
response = requests.request("GET", url, headers=headers)
users = response.json()['members']
for user in users:
    for person in present:
        if user['id'] == person:
            attendance.append(user['real_name'])
            
count = 0
for person in attendance:
    print(person)
    count = count + 1
    
print("total attendance: " + str(count))
