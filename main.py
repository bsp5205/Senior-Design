import math
import javalang
import clang
import procedural_java
import evaluate_metrics as em
import mood
import re
import handle_request as hr
import utilities as util

def evaluate_abc(tree):
    # assignment
    assignments = len(util.custom_filter2(tree, 'Assignment')) + len([ele for ele in
                                                                      util.search2(tree, 'MemberReference',
                                                                                   'prefix_operators') + util.search2(
                                                                          tree, 'MemberReference', 'postfix_operators')
                                                                      if ele != [] and ele == ['++'] or ele == ['--']])

    # branches
    branches = len(util.custom_filter2(tree, 'StatementExpression')) + len(util.custom_filter2(tree, 'ClassCreator'))

    # conditions
    conditions = len(util.search2(tree, 'IfStatement', 'else_statement')) + len(
        [ele for ele in util.custom_filter2(tree, 'SwitchStatementCase')]) + len(
        util.custom_filter2(tree, 'TryStatement')) + len(util.custom_filter2(tree, 'CatchClause')) + len(
        [ele.operator for ele in util.custom_filter2(tree, 'BinaryOperation') if
         ele.operator == '<' or ele.operator == '>' or ele.operator == '<=' or ele.operator == '>=' or ele.operator == '==' or ele.operator == '!='])

    return round(math.sqrt(pow(assignments, 2) + pow(branches, 2) + pow(conditions, 2)), 2)

def calculate_McGabe_cyclomatic_complexity(tree):
    # https://www.theserverside.com/feature/How-to-calculate-McCabe-cyclomatic-complexity-in-Java
    cc = 1
    cc_list = []
    # Get relevant lists
    # method_list = util.custom_filter(tree, 'MethodDeclaration')

    method_list = util.custom_filter_javalang_tree(tree, 'javalang.tree.MethodDeclaration')

    for method_num in range(len(method_list)):

        # Turn cc_list into a tuple of the cc and the SLOC in the method for analysis
        # Create a dummy tree so calculate_SLOC works
        dummy_tree = javalang.parser.tree.CompilationUnit(package=0, imports=0, types=[method_list[method_num]])
        cc += len(util.custom_filter(dummy_tree, 'WhileStatement') + util.custom_filter(dummy_tree, 'ForStatement') + util.custom_filter(dummy_tree, 'IfStatement'))
        method_SLOC = calculate_SLOC(dummy_tree)

        cc_list.append((cc, method_SLOC))
        cc = 1
    return cc_list

def calculate_SLOC(tree):
    sloc = 0

    # All one line of code hence + 1 ('}' not included)
    # Handling imports
    if type(tree.imports) != int:
        sloc += len(tree.imports)

    # Filter out FormalParameters
    sloc += len(list(filter(lambda i: not (type(i) is javalang.tree.FormalParameter),
                    util.custom_filter_javalang_tree(tree, 'javalang.tree.Declaration'))))
    method_list = util.custom_filter_javalang_tree(tree, 'javalang.tree.MethodDeclaration')
    for method in method_list:
        for annotation in method.annotations:
            if annotation.name == 'Override':
                sloc += 1

    sloc += len(util.custom_filter_javalang_tree(tree, 'javalang.tree.Assignment'))
    sloc += len(util.custom_filter_javalang_tree(tree, 'javalang.tree.Invocation'))
    sloc += len(util.custom_filter_javalang_tree(tree, 'javalang.tree.BlockStatement'))
    sloc -= len(util.custom_filter_javalang_tree(tree, 'javalang.tree.ForStatement'))

    return sloc

def calculate_comment_percentage(tree, number_of_comments):
    sloc = calculate_SLOC(tree)
    if sloc > 0:
        return round((number_of_comments/sloc) * 100, 2)
    else:
        return 0

def calculate_weighted_method_per_class(tree):
    cc_list = calculate_McGabe_cyclomatic_complexity(tree)
    sum = 0
    for tup in cc_list:
        sum += tup[0]
    return sum

def recursive_check(tree, subtree, height):
    # print(subtree)
    # children_list = subtree.implements
    # print(children_list)
    if subtree.implements is not None:
        implement_list = subtree.implements
        for subtree_num in range(len(implement_list)):
            # print(subtree.name, 'implements', subtree.implements[0].name)
            class_list = util.custom_filter(tree, 'ClassDeclaration')
            for class_num in range(len(class_list)):
                # print('checking class', class_list[class_num].name)
                if class_list[class_num].name == subtree.implements[0].name:
                    subtree = class_list[class_num]
                    return recursive_check(tree, subtree, height + 1)
    elif subtree.extends is not None:
        extend_list = subtree.extends
        # tree of parent class
        class_name = next(iter(extend_list))[1].name

        for parent in util.custom_filter_javalang_tree(tree, 'javalang.tree.ClassDeclaration'):
            if class_name == parent.name:
                return recursive_check(tree, parent, height + 1)


    return height

def calculate_depth_of_inheritance(tree):
    dit = 0
    class_list = util.custom_filter_javalang_tree(tree, 'javalang.tree.ClassDeclaration')
    for class_num in range(len(class_list)):
        class_being_checked = class_list[class_num]
        dit_new = recursive_check(tree, class_being_checked, 0)
        if dit_new > dit:
            dit = dit_new

    return dit

def calculate_coupling_between_objects(tree, cbo_tuples):
    # count number of times a different class's methods or attributes are used in the class in question
    # get a list of all classes
    # for each ClassDeclaration.body[x], pull each MethodDeclaration, and then create an entry {ClassDeclaration:MethodDeclaration}
    # add using dictionary_name[key] = value
    cbo = 0
    # dictionaries to track {class name: method/attribute name}
    method_dict = {}
    attribute_dict = {}
    # get a list of the classes
    class_list = util.custom_filter(tree, 'ClassDeclaration')
    # check each class
    for class_num in range(len(class_list)):
        class_body = class_list[class_num].body
        # for each instance in each class
        for instance in class_body:
            # add each method to a dictionary as {name:type}
            if isinstance(instance, javalang.tree.MethodDeclaration):
                method_dict[class_list[class_num].name] = str(instance.name)
                # check if the new method type is in the dictionary and the new key/value does not already exist.
                # if the {class name: method name} does exist, then skip it. If the class name is in the dictionary, then the class type exists in another class
                if len(method_dict) > 0 and instance.name in method_dict.values() and (class_list[class_num].name, instance.name) not in method_dict.items():
                    cbo += 1
            elif isinstance(instance, javalang.tree.FieldDeclaration):
                attribute_dict[class_list[class_num].name] = str(instance.type.name)
                # check if the new attribute type is in the dictionary and the new key/value does not already exist.
                # if the {class name:attribute name} does exist, then skip it. If the class name is in the dictionary, then the class type exists in another class
                if len(attribute_dict) > 0 and instance.type.name in attribute_dict.values() and (class_list[class_num].name, instance.type.name) not in attribute_dict.items():
                    cbo += 1

    # print(method_dict)
    # print(attribute_dict)
    return cbo

def coupled_methods(class_name, couple):
    methods = 0

    path = 'TestAssignmentFiles/' + class_name + '.java'

    # if finding the file does not work
    try:
        concat_line, comment_count = util.read_file(path, 0)
        tree = javalang.parse.parse(concat_line)
        invoc_method_list = util.custom_filter_javalang_tree(tree, 'javalang.tree.MethodInvocation')
        for invoc_method_num in range(len(invoc_method_list)):
            cur_method = invoc_method_list[invoc_method_num]
            if (cur_method.qualifier == couple):
                methods = methods + 1
    finally:
        return methods


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

def main(path):
    # get the concat file
    concat_line, comment_count = util.read_file(path, 0)

    # check if the path contains .java to use the proper library
    if '.java' in path:
        # create the tree
        tree = javalang.parse.parse(concat_line)

        # script tests
        print('OO Metrics:')
        print('calculate_McGabe_cyclomatic_complexity:', calculate_McGabe_cyclomatic_complexity(tree))
        print('calculate_SLOC:', calculate_SLOC(tree))
        print('calculate_comment_percentage:', calculate_comment_percentage(tree, comment_count))
        print('calculate_weighted_method_per_class:', calculate_weighted_method_per_class(tree))
        print('calculate_depth_of_inheritance:', calculate_depth_of_inheritance(tree))
        # print('calculate_coupling_between_objects:', calculate_coupling_between_objects(tree, cbo_tuples))

        print('\ncalculate_method_hiding_factor:', mood.calculate_method_hiding_factor(tree))
        print('calculate_attribute_hiding_factor:', mood.calculate_attribute_hiding_factor(tree))
        print('calculate_method_inheritance_factor:', mood.calculate_method_inheritance_factor(tree))
        print('calculate_attribute_inheritance_factor:', mood.calculate_attribute_inheritance_factor(tree))
        print('calculate_coupling_factor:', mood.calculate_coupling_factor(tree))
        print('calculate_polymorphism_factor:', mood.calculate_polymorphism_factor(tree))

        print('\nProcedural Metrics:')
        procedural_java.main()

        print("\nMetric score evaluation")
        print("CP Result: ", em.comment_percentage(calculate_comment_percentage(tree, comment_count), 50))
        print("CC Result: ", em.mcgabe_cc(calculate_weighted_method_per_class(tree), 100, calculate_SLOC(tree)))
        print("CBO/DIT Result:", em.cbo_dit(calculate_depth_of_inheritance(tree), 50))
        print("--Mood Results--")
        print("MHF: ", em.mood_MHF(mood.calculate_method_hiding_factor(tree), 50))
        print("AHF: ", em.mood_AHF(mood.calculate_attribute_hiding_factor(tree), 50))
        print("MIF: ", em.mood_MIF(mood.calculate_method_inheritance_factor(tree), 50))
        print("AIF: ", em.mood_AIF(mood.calculate_attribute_inheritance_factor(tree), 50))
        print("CF: ", em.mood_CF(mood.calculate_coupling_factor(tree), 50))
        print("PF: ", em.mood_PF(mood.calculate_polymorphism_factor(tree), 50))


if __name__ == '__main__':
    main()
