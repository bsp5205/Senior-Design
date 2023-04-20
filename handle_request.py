import dotenv
import os
import canvasapi
import requests
import zipfile
import io
import updated_main as um


# gets the canvas api from an ip address
# From the canvasapi library https://github.com/ucfopen/canvasapi
def get_api(canvas_ip):
    dotenv.load_dotenv(dotenv.find_dotenv())

    TOKEN = 'ddEEiCh4OyBn07BQJ8X0kNXWwOTXnsFoH3CYcMqDFM7roSfltf3PTKTz8nqIpppL'
    BASEURL = 'http://' + canvas_ip  #VMWare IP

    canvas_api = canvasapi.Canvas(BASEURL, TOKEN)

    return canvas_api
# takes a course id to launch the start page
def launch_page(domain, course_id):
    canvas_api = get_api(domain)

    course = canvas_api.get_course(course_id)

    # List of assignments in the course
    # user will select from the assignments to go to the assessor
    assignments = course.get_assignments()

    for assign in assignments:
        # create links to each assignment in the html (Check to see if they can even be assessed)
        pass
        #print(assign.attributes)
        # if 'submission_types' contains 'online_upload'?

    return assignments, course, canvas_api


# takes an assignment id to launch the quality assessor
# returns a list of canvasapi submission objects
def launch_assignment(course, assign_id):
    assignment = course.get_assignment(assign_id)
    submissions = assignment.get_submissions()

    for sub in submissions:
        print(sub.attributes)

    # open the page here with the first student

    return submissions

# takes a list of canvasapi attachment objects from a submission
# returns a list of strings denoting the names of the files for an assignment submission
def get_submission_file(attachments):

    files = []
    for file in attachments:
        # gets the request from url
        req = requests.get(file['url'])

        # if the file is good unzip and send to TestAssignmentFiles
        if req.ok:
            file_path = 'TestAssignmentFiles/' + file['display_name']
            open(file_path, 'wb').write(req.content)
            # if zip file
            # zip_sub = zipfile.ZipFile(io.BytesIO(req.content))
            # zip_sub.extractall('TestAssignmentFiles')
        else:
            print("There was an error in the submission download request")

        files.append((file['display_name'], file['url']))

    # Return the tuple list files
    return files

# this method will leverage other methods to generate the metrics dict
def analyze_submissions(subs):
    report_metrics = {}
    for sub in subs:
        if sub.attributes['submission_type'] == 'online_upload':
            attachs = sub.attributes['attachments']
            files = get_submission_file(attachs)

            report_metrics = um.assess_every_file('TestAssignmentFiles')
            # remove_submission_files(files)

    return report_metrics

# remove the submission files from the temporary directory after use
def remove_submission_files(files):
    for file in files:
        os.remove('TestAssignmentFiles/' + file[0])
    return 1
