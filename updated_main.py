import main
import os
import mood
import utilities as util
import javalang
import main as m
import procedural_c as proc
import clang.cindex as ci
import sys
import evaluate_metrics as em
import LocalServer
import procedural_java as pj


def config_set():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    ci.Config.set_library_file(dir_path + '/libclang.dll')
    return

# Assess every file in given directory
def assess_every_file(directory):
    attribute_list = {}
    for file in os.listdir(directory):
        path = directory + "/" + file
        concat_line, comment_count = util.read_file(path, 0)

        if file.endswith(".java"):

            try:
                tree = javalang.parse.parse(concat_line)


                # print(file + str(m.calculate_comment_percentage(tree, comment_count)))
                attribute_list[file] = {
                    # Mood Metrics
                    'AHF': em.mood_AHF(mood.calculate_attribute_hiding_factor(tree), 50),
                    'MHF': em.mood_MHF(mood.calculate_method_hiding_factor(tree), 50),
                    'MIF': em.mood_MIF(mood.calculate_method_inheritance_factor(tree), 50),
                    'AIF': em.mood_AIF(mood.calculate_attribute_inheritance_factor(tree), 50),
                    'POF': em.mood_PF(mood.calculate_polymorphism_factor(tree), 50),
                    'COF': em.mood_CF(mood.calculate_coupling_factor(tree), 50),

                    # OO Metrics
                    'CC': em.mcgabe_cc(m.calculate_weighted_method_per_class(tree), 100, m.calculate_SLOC(tree)),
                    'SLOC': em.sloc(m.calculate_SLOC(tree), 50),
                    'CP': em.comment_percentage(m.calculate_comment_percentage(tree, comment_count), 50),
                    'WMC': em.mcgabe_cc(m.calculate_weighted_method_per_class(tree), 100, m.calculate_SLOC(tree)),
                    'DIT': em.cbo_dit(m.calculate_depth_of_inheritance(tree), 50),
                    'TC': pj.calculate_token_count(tree),
                    'ABC': pj.calculate_ABC(tree),
                    #'CBO': main.calculate_coupling_between_objects(tree, cbo_tuples)

                    'class': m.evaluate_class_names(tree),
                    'var': m.evaluate_variable_names(tree),
                    'meth': m.evaluate_method_names(tree)

                    # attribute_list['CBO'] = main.calculate_coupling_between_objects(tree)
                }
            except Exception as e:
                print("Java Analysis Failed")
                print(e)
                exec_type, exec_obj, exec_tb = sys.exc_info()
                fname = os.path.split(exec_tb.tb_frame.f_code.co_filename)[1]
                print(exec_type, fname, exec_tb.tb_lineno)
                print(path)

            # file_list[file] = attribute_list
        elif file.endswith(".cpp") or file.endswith(".c"):
            try:
                # Clang setup
                index = ci.Index.create()
                tu = index.parse("TestAssignmentFiles/" + file)
                filename = tu.spelling

                attribute_list[file] = {
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
            except Exception as e:
                print(e)
                print("C/C++ Analysis Failed")
                exec_type, exec_obj, exec_tb = sys.exc_info()
                fname = os.path.split(exec_tb.tb_frame.f_code.co_filename)[1]
                print(exec_type, fname, exec_tb.tb_lineno)
            # file_list[file] = attribute_list

    for item in attribute_list:
        print(item)
        for metric in attribute_list[item]:
            print(metric, end=" ")
            print(attribute_list[item][metric], end="\n")
            pass
        print(end="\n")
    print(attribute_list)
    return attribute_list


def main():
    # Launch the application generates the airium original html
    LocalServer.run_app()

    # m.main('TestAssignmentFiles/simple.java')
    assess_every_file('TestAssignmentFiles')


if __name__ == '__main__':
    main()
