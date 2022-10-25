from flask import Flask, render_template

app = Flask(__name__, template_folder = 'templates_html')

@app.route('/')
def welome():
    return('Welcome to Playground assignment. Input /play or /play/<#> or /play/<#>/color. Have Fun!')

@app.route('/play')
def play1():
    return render_template('index_play.html', num = 3, color ='#A6C4F4')

@app.route('/play/<int:num>')
def play2(num):
    return render_template('index_play.html', num = num, color ='#A6C4F4')

@app.route('/play/<int:num>/<string:color>')
def play3(num, color):
    return render_template('index_play.html', num= num, color = color)

@app.route('/', defaults = {'path':''})
@app.route('/<path:path>')
def catch_all(path):
	return 'Nope, Try Again'

if __name__ == "__main__":
    app.run(debug=True, port = 5000)