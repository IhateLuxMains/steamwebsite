from urllib import response
import requests
import json
import app

default = 76561198405626506
id = default

response  = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=FCA53F323070D2EF17EF9D969B43EAC4&steamid=%s&include_appinfo=true&format=json"% (id)).text
response_info = json.loads(response)

print(response_info)