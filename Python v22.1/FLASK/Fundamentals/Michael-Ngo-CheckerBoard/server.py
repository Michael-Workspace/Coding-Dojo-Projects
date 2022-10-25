from flask import Flask, render_template

app = Flask(__name__, template_folder = 'template')

@app.route('/')
def main():
    return(render_template('index.html', row=8, col=8, color1= 'red', color2 = 'black'))

@app.route('/<int:row>')
def justrow(row):
    return(render_template('index.html', row=row, col=8, color1= 'red', color2 = 'black'))

@app.route('/<int:row>/<int:col>')
def rowandcol(row,col):
    return(render_template('index.html', row=row, col=col, color1= 'red', color2 = 'black'))

@app.route('/<int:row>/<int:col>/<color1>/<color2>')
def color(row ,col ,color1, color2):
    return(render_template('index.html', row=row, col=col, color1= color1, color2 = color2))

@app.route('/', defaults = {'path':''})
@app.route('/<path:path>')
def catch_all(path):
	return 'Nope, Try Again'

if __name__ == "__main__":
    app.run(debug=True, port = 5000)