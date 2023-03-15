import canvas_api.main as ca

# takes a course id to launch the start page
def launch_page(domain, course_id):
    canvas_api = ca.get_api(domain)

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