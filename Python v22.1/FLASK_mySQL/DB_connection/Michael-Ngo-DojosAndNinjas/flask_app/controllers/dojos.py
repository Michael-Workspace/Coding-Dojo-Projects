from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/add_dojo')

@app.route('/add_dojo')
def add_dojo():
    return render_template('add_dojo.html', all_dojos = Dojo.get_all())

@app.route('/create_dojo',methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/add_dojo')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        'id':id
    }
    return render_template('ninja_in_dojo.html',dojo = Dojo.get_all_ninjas(data))