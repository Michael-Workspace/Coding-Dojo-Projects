from flask import Flask, render_template

app = Flask(__name__, template_folder = 'template')

@app.route('/')
def welcome():
    return 'Welcome to the Table assigment. Input /list to start. Have Fun!'

@app.route('/list')
def render_list():
    user_info = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('index.html',users = user_info)

@app.route('/', defaults = {'path':''})
@app.route('/<path:path>')
def catch_all(path):
	return 'Nope, Try Again'

if __name__ == "__main__":
    app.run(debug=True, port = 5000)