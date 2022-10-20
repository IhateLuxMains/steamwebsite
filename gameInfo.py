from urllib import response
import requests
import json
import app
import numpy as np

default = 76561198405626506


app.variable

# response  = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=FCA53F323070D2EF17EF9D969B43EAC4&steamid=%s&include_appinfo=true&format=json"% (id)).text
# response_info = json.loads(response)['response']['games']

# gamez = []
# time = []  
# for i in response_info:
#         if(i['playtime_forever'] > 4000): #comparasion in mnutes
#             gamez.append(i['name'])
#             time.append(i['playtime_forever'])
 
# np.column_stack((gamez,time))