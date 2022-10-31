from flask import render_template, request, redirect
from flask_app.models.user import User
from flask_app import app

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

@app.route ('/show_user/<int:id>')
def show(id):
    data = {
        'id': id
    }
    return render_template('/show.html', user=User.get_one(data))

@app.route('/edit_user/<int:id>')
def edit_user(id):
    data = {
        'id':id
    }
    return render_template('/edit.html',user=User.get_one(data))

@app.route('/update_user',methods=['POST'])
def update():
    User.edit(request.form)
    return redirect('/')

@app.route('/delete_user/<int:id>')
def delete_user(id):
    data = {
        'id':id
    }
    User.delete(data)
    return redirect ('/')