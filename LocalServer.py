import subprocess
import canvas_api.main as ca
import flask
import handle_request as hr
from flask import Flask, request, jsonify, render_template_string, render_template
#import report

#from flask_cors import CORS
app = Flask(__name__)
#cors = CORS(app)


@app.route("/", methods=['GET', 'POST'])
def index():
    print('\nThis is an example of the launch request sent by someone:')
    print(flask.request.method)
    print(flask.request.form)
    if flask.request.method == "POST":
        assigns, course, api = hr.launch_page(flask.request.form['custom_canvas_api_domain'], flask.request.form['custom_canvas_course_id'])
        print(assigns[0].attributes)

        # this will be modularized
        assign_id = assigns[0].attributes['id']
        subs = hr.launch_assignment(course, assign_id)
        # ^once launched foreach grab and remove the files to build the metrics dict
        attachments = subs[0].attributes['attachments']

        cur_ass = assigns[0]
        assignment_info = {}

        print(course.attributes)
        # course section
        course_name = course.attributes['name']
        course_code = course.attributes['course_code']
        assign_name = cur_ass.attributes['name']
        canvas_date = cur_ass.attributes['due_at']

        assignment_info["course_name"] = course_name
        assignment_info["course_code"] = course_code
        assignment_info["assign_name"] = assign_name
        assignment_info["due_date"] = canvas_date

        # get the students info
        student_info = []
        for submission in subs:
            student_id = submission.attributes['user_id']
            student = api.get_user(student_id)
            student_info.append((student.attributes['id'], student.attributes['name'], submission.attributes['id']))

        # generating the metrics for all files. May take some time
        report_metrics = hr.analyze_submissions(subs)

        # first submission and files
        cur_files = hr.get_submission_file(attachments)
        print(cur_files)

        # generate the air file
        # report.air_file(cur_files, student_info, assignment_info, report_metrics)

        # Put a "your session has been opened in a separate tab" page here?
        return render_template('home.html')
    # Possibly send to error page
    return render_template('airFile.html')

    # return render_template_string(HTML String from Airium)


def run_app():
    # Call this function in the main to run the app
    app.run(debug=True)


"""
def postME():
    data = request.get_json()
    data = jsonify(data)
    print(data.get_json())
    return data
"""

if __name__ == "__main__":
    app.run(debug=True)
