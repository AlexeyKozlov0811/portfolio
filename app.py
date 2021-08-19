"""
module app.py contains main portfolio code
dont forget to set up ENV variables FLASK_APP, FLASK_ENV before run
"""

from flask import Flask, request, render_template

app = Flask(__name__)

"""
data base entities section
"""


"""
routes section
"""
@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
