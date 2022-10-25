from ast import Num
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<str:name>')
def say(name):
    print(name)
    return "Hi, " + name

@app.route('/repeat/<int:num>/<str:text>')
def repeat(text, num):
    repeat_word = ""
    for i in range(0,num):
        repeat_word += f'<p>{text}</p>'
    return repeat_word

@app.route('/', defaults = {'path':''})
@app.route('/<path:path>')
def catch_all(path):
	return 'Nope, Try Again'

if __name__ == "__main__":
    app.run(debug=True, port = 5000)