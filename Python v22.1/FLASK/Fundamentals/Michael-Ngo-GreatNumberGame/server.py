from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__, template_folder = 'template')
app.secret_key = 'password'

@app.route('/')
def main():
    if 'target' not in session:
        session['target'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if int(request.form['input']) == session['target']:
        session['result'] = "correct"
    elif int(request.form['input']) > session['target']:
        session['result'] = "high"
    elif int(request.form['input']) < session['target']:
        session['result'] = "low"
    return redirect('/')

@app.route('/replay')
def play_again():
    session.pop('target')
    session.pop('result')
    return redirect('/')

@app.route('/', defaults = {'path':''})
@app.route('/<path:path>')
def catch_all(path):
	return 'Nope, Try Again'

if __name__ == "__main__":
    app.run(debug=True, port = 5000)