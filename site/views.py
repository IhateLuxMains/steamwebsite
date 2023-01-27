from flask import Blueprint,request,render_template
import requests
views = Blueprint('views', __name__)

@views.route('/index')
def my_form():
    return render_template('index.html')

@views.route('/', methods=['POST'])
def my_form_post():
    if request.method == 'POST':
        id = request.form.get('variable')
        response  = requests.get("http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=FCA53F323070D2EF17EF9D969B43EAC4&steamid=%s&include_appinfo=true&format=json"% (id)).text
        return response