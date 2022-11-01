from flask import render_template, request, redirect
from flask_app import app
from flask_app.models import ninja, dojo


@app.route('/add_ninja')
def add_ninja():
    return render_template('add_ninja.html', dojos = dojo.Dojo.get_all())

@app.route('/create_ninja',methods=["POST"])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/')

