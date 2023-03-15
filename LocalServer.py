import subprocess
import canvas_api.main as ca
import flask
import handle_request
from flask import Flask, request, jsonify, render_template_string, render_template

#from flask_cors import CORS
app = Flask(__name__)
#cors = CORS(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    print('\nThis is an example of the launch request sent by someone:')
    print(flask.request.method)
    print(flask.request.form)
    if flask.request.method == "POST":
        handle_request.launch_page(flask.request.form['custom_canvas_api_domain'], flask.request.form['custom_canvas_course_id'])
        return render_template('home.html')
    # Possibly send to error page
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
    #current_canvas_ip = '10.32.68.158'
    #response = ca.send_request(current_canvas_ip)
    #print("This is an Example of sending canvas a request.")
    #print("This is a self request:")
    #print(response.attributes)

    app.run(debug=True)
