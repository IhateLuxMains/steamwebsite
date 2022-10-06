from re import S
from bs4 import BeautifulSoup
import requests
import json

key = "C:\\Users\\Julian\\Desktop\\steamAPIkey\\sAPIkey.txt"
with open(key, 'r') as file:
    key = file.read()

id =  76561198405626506
    # FIX KEY IN API HTML, OPEN FROM DOC 
page = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=FCA53F323070D2EF17EF9D969B43EAC4&steamid=76561198401753028&include_appinfo=true&format=json" # % (key, id)
soup = BeautifulSoup(requests.get(page).text, "html.parser")

data = json.loads(soup.text)['response']['games']
gamez = []
time = []  
for i in data:
        if(i['playtime_forever'] > 0):
            gamez.append(i['name'])
            time.append(i['playtime_forever'])

print(gamez)
print(time)
    



