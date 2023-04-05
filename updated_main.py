import main
import handle_request
import os
import mood
import utilities as util
import javalang
import main as m
import procedural_c as proc
import clang.cindex as ci
import sys

file_list = {}

def find_all_file_metrics(filename):
    return file_list[filename]

def find_file_metric(filename, metric):
    return file_list[filename][metric]

# Assess every file in given directory
def assess_every_file(directory):

    for file in os.listdir(directory):
        path = directory + "/" + file
        concat_line, comment_count = util.read_file(path, 0)

        if file.endswith(".java"):

            tree = javalang.parse.parse(concat_line)

            attribute_list = {
                # Mood Metrics
                'AHF': mood.calculate_attribute_hiding_factor(tree),
                'MHF': mood.calculate_method_hiding_factor(tree),
                'MIF': mood.calculate_method_inheritance_factor(tree),
                'AIF': mood.calculate_attribute_inheritance_factor(tree),
                'POF': mood.calculate_polymorphism_factor(tree),
                'COF': mood.calculate_coupling_factor(tree),

                # OO Metrics
                'CC': m.calculate_McGabe_cyclomatic_complexity(tree),
                'SLOC': m.calculate_SLOC(tree),
                'CP': m.calculate_comment_percentage(tree, comment_count),
                'WMC': m.calculate_weighted_method_per_class(tree),
                'DIT': m.calculate_depth_of_inheritance(tree)
                # attribute_list['CBO'] = main.calculate_coupling_between_objects(tree)
            }
            file_list[file] = attribute_list
        elif file.endswith(".cpp") or file.endswith(".c"):
            # Clang setup
            index = ci.Index.create()
            tu = index.parse(file)
            filename = tu.spelling

            attribute_list = {
                'ELOC': proc.effective_lines_of_code(filename),
                'KLOC': proc.kilo_lines_of_code(filename),
                'ABC': proc.assignments_branches_conditionals(tu.cursor),
                'N': proc.halstead_program_length(tu.cursor),
                'n': proc.halstead_program_vocabulary(tu.cursor),
                'V': proc.halstead_program_volume(tu.cursor),
                'D': proc.halstead_difficulty(tu.cursor),
                'L': proc.halstead_level(tu.cursor),
                'E': proc.halstead_effort(tu.cursor),
                'B': proc.halstead_bugs(tu.cursor),
                'TC': proc.token_count(tu.cursor)
            }

            # Procedural Metrics

            file_list[file] = attribute_list

    for item in file_list:
        print(item)
        for metric in file_list[item]:
            print(metric, end=" ")
            print(file_list[item][metric], end="\n")
        print(end="\n")


def main():
    assess_every_file('TestAssignmentFiles')

    # Example of find_all_file_metrics
    print(find_all_file_metrics('DNA.java'))

    # Example of find_file_metric
    print(find_file_metric('DNA.java', 'MIF'))

if __name__ == '__main__':
    main()