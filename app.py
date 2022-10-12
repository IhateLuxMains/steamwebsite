from flask import Flask, request, render_template

app = Flask(__name__)

test =1234


@app.route('/stats', methods=['GET', 'POST'])
def foo():
    steamID = request.form['steamID']
    return steamID

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()