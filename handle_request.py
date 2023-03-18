import dotenv
import os
import canvasapi
import requests
import zipfile
import io


# gets the canvas api from an ip address
# From the canvasapi library https://github.com/ucfopen/canvasapi
def get_api(canvas_ip):
    dotenv.load_dotenv(dotenv.find_dotenv())

    TOKEN = os.environ.get('CANVAS_API_TOKEN')
    BASEURL = 'http://' + canvas_ip  #VMWare IP

    canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

    return canvas_api


# takes a course id to launch the start page
def launch_page(domain, course_id):
    canvas_api = get_api(domain)

    print(course_id)
    print(domain)

    course = canvas_api.get_course(course_id)
    print(course)

    # List of assignments in the course
    # user will select from the assignments to go to the assessor
    assignments = course.get_assignments()

    for assign in assignments:
        # create links to each assignment in the html (Check to see if they can even be assessed)
        print(assign.attributes)
        # if 'submission_types' contains 'online_upload'?
    launch_assignment(course, 1)
    return


# takes an assignment id to launch the quality assessor
def launch_assignment(course, assign_id):
    assignment = course.get_assignment(assign_id)
    submissions = assignment.get_submissions()

    for sub in submissions:
        print(sub.attributes)
    return


# get attach the files to use
def get_submission_files(url):
    # gets the request from url
    req = requests.get(url)

    # if the file is good unzip and send to AssignmentFiles
    if req.ok:
        zip = zipfile.ZipFile(io.BytesIO(req.content))
        zip.extractall('AssignmentFiles')
    else:
        print ("There was an error in the submission download request")

    # Return the list of unzipped files
    files = os.listdir('AssignmentFiles')
    return files


# remove the submission files from the temporary directory after use
def remove_submission_files(files):
    for file in files:
        os.remove('AssignmentFiles/' + file)
