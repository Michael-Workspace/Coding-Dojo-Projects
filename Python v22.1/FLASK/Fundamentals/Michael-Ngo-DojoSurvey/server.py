from flask import Flask, render_template, redirect, request

app = Flask(__name__, template_folder = 'template')
app.secret_key = 'password'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    print ("Submitted Info")
    print (request.form)
    return render_template('result.html', name=name, location=location, language=language, comment=comment)

@app.route('/restart')
def restart():
    session.pop('result')
    return redirect('/')

@app.route('/', defaults = {'path':''})
@app.route('/<path:path>')
def catch_all(path):
	return 'Nope, Try Again'

if __name__ == "__main__":
    app.run(debug=True, port = 5000)