from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__, template_folder = 'templates')
app.secret_key = "password"

@app.route('/')
def index():
    return render_template('result.html',all_users=User.get_all())

@app.route('/new_user')
def new_user():
    return render_template('index.html')

@app.route('/create_user',methods=['POST'])
def create_user():
    print(request.form)
    User.save(request.form)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)