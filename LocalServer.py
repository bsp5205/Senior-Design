import subprocess

import flask
from flask import Flask, request, jsonify, render_template_string, render_template

from flask_cors import CORS
app = Flask(__name__)
# cors = CORS(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    print(flask.request.method)
    print(flask.request.values)
    return render_template('home.html')

    # return render_template_string(HTML String from Airium)


"""
def postME():
    data = request.get_json()
    data = jsonify(data)
    print(data.get_json())
    return data
"""

if __name__ == "__main__":
    app.run(debug=True)
