
from re import S
from bs4 import BeautifulSoup
import requests
import json

key = "C:\\Users\\Julian\\Desktop\\steamAPIkey\\sAPIkey.txt"
with open(key, 'r') as file:
    key = file.read()

def cause_app_to_do_something():
    import app
    id =  app.steamID

    # FIX KEY IN API HTML, OPEN FROM DOC 
page = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=FCA53F323070D2EF17EF9D969B43EAC4&steamid=steamID&include_appinfo=true&format=json" # % (key, id)
soup = BeautifulSoup(requests.get(page).text, "html.parser")

data = json.loads(soup.text)['response']['games']
gamez = []
time = []  
for i in data:
        if(i['playtime_forever'] > 0):
            gamez.append(i['name'])
            time.append(i['playtime_forever'])

def index():
    return (gamez)
print(time)
    



