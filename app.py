from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/about/<string:name>')
def about(name):
    return 'about' + name


if __name__ == '__main__':
    app.run(debug=True)
