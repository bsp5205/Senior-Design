import utilities as util
import re

def evaluate_class_names(tree):
    class_list = util.custom_filter2(tree, 'ClassDeclaration')
    good_count = 0
    count = 0
    for class_ in class_list:
        if re.search('^[A-Z][a-zA-Z0-9]*$', class_.name):
            good_count += 1

        count += 1

    print((good_count/count)*100)
    return int(round((good_count / count) * 100, 0))


def evaluate_method_names(tree):
    method_list = util.custom_filter2(tree, 'MethodDeclaration')
    good_count = 0
    count = 0
    for method_ in method_list:
        if (re.search('([a-z]+[A-Z]|[A-Z]+(?![a-z]))[a-zA-Z]*', method_.name) and len(method_.name) > 10) or (
                len(method_.name) < 10 and re.search('^[a-z]+$', method_.name)):
            good_count += 1

        count += 1

    return int(round((good_count / count) * 100, 0))


def evaluate_variable_names(tree):
    variable_list = util.custom_filter2(tree, 'VariableDeclarator')
    # print(class_list)
    good_count = 0
    count = 0
    for variable_ in variable_list:
        if re.search('([a-z]+[A-Z]|[A-Z]+(?![a-z]))[a-zA-Z]*', variable_.name) or (
                re.search('^[a-z]+$', variable_.name) and len(variable_.name) < 10):
            good_count += 1

        count += 1

    return int(round((good_count / count) * 100, 0))


def evaluate_line_length(file_path, length=80):
    with open(file_path, 'r') as file:
        good_count = 0
        count = 0
        for line in file:
            if len(line) < length:
                good_count += 1
            count += 1

    return int(round((good_count / count) * 100, 0))