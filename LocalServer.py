import subprocess
import canvas_api.main as ca
import flask
from flask import Flask, request, jsonify, render_template_string, render_template

from flask_cors import CORS
app = Flask(__name__)
# cors = CORS(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    print('\nThis is an example of the launch request sent by canvas:')
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
    current_canvas_ip = '10.32.24.64'
    response = ca.send_request(current_canvas_ip)
    print("This is an Example of sending canvas a request.")
    print("This is a self request:")
    print(response.attributes)

    app.run(debug=True)
