from flask import Flask, render_template, request, redirect, session

app = Flask(__name__, template_folder = 'template')
app.secret_key = "password"


@app.route('/')
def main():
    if 'count' not in session:
        session['count']=1
    else:
        session['count']+=1
    return render_template("index.html",count=session['count'])

@app.route('/count', methods=['POST'])
def addnclear():
    if request.form['update'] == 'add':
        session['count'] += 0
    elif request.form['update'] == 'add2':
        session['count'] += 1
    elif request.form['update'] == 'reset':
        session['count'] = 0
    return redirect('/')

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

@app.route('/', defaults = {'path':''})
@app.route('/<path:path>')
def catch_all(path):
	return 'Nope, Try Again'

if __name__ == "__main__":
    app.run(debug=True, port = 5000)