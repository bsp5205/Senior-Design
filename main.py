import javalang
import clang

import utilities as util

def calculate_McGabe_cyclomatic_complexity(tree):
    # https://www.theserverside.com/feature/How-to-calculate-McCabe-cyclomatic-complexity-in-Java
    cc = 1

    # get relevant lists
    method_list = util.custom_filter(tree, 'IfStatement')
    iterative_list = util.custom_filter(tree, 'WhileStatement') + util.custom_filter(tree, 'ForStatement')

    for method_num in range(len(method_list)):  # loop through if/else if/else statements
        if hasattr(method_list[method_num], 'else_statement') and type(method_list[method_num].else_statement).__name__ == 'IfStatement':
            cc += 1 # else if
        elif hasattr(method_list[method_num], 'then_statement') and type(method_list[method_num].else_statement).__name__ == 'BlockStatement':
            cc += 1 # else
        else:
            cc += 1 # if

    for iter_num in range(len(iterative_list)): # loop through list of for loops and while loops
        cc += 1

    print('calculate_McGabe_cyclomatic_complexity:', cc)
    return cc

def calculate_SLOC(tree):
    sloc = 0

    # ClassDeclaration +2
    class_list = util.custom_filter(tree, 'ClassDeclaration')
    for class_num in range(len(class_list)):
        sloc += 2

    # MethodDeclaration +2
    method_list = util.custom_filter(tree, 'MethodDeclaration')
    for method_num in range(len(method_list)):
        sloc += 2

    # StatementExpression
    statement_list = util.custom_filter(tree, 'StatementExpression')
    for statement_num in range(len(statement_list)):
        sloc += 1

    # LocalVariableDeclaration + 1
    local_var_declaration_list = util.custom_filter(tree, 'LocalVariableDeclaration')
    for local_var_num in range(len(local_var_declaration_list)):
        sloc += 1

    # IfStatement +2, ElseStatement +=1
    if_statement_list = util.custom_filter(tree, 'IfStatement')
    for if_statement_num in range(len(if_statement_list)):
        if hasattr(if_statement_list[if_statement_num], 'else_statement') and type(if_statement_list[if_statement_num].else_statement).__name__ == 'IfStatement':
            sloc += 2
        elif hasattr(method_list[if_statement_num], 'then_statement') and type(if_statement_list[if_statement_num].else_statement).__name__ == 'BlockStatement':
            sloc += 1
        else:
            sloc += 2

    # ForStatement + 2
    for_statement_list = util.custom_filter(tree, 'ForStatement')
    for for_num in range(len(for_statement_list)):
        sloc += 2

    # WhileStatement +2
    while_statement_list = util.custom_filter(tree, 'WhileStatement')
    for while_num in range(len(while_statement_list)):
        sloc += 2

    print('calculate_SLOC:', sloc)
    return sloc

def calculate_comment_percentage(tree, number_of_comments):
    sloc = calculate_SLOC(tree)
    print('calculate_comment_percentage:', (number_of_comments/sloc) * 100)
    if sloc > 0:
        return (number_of_comments/sloc) * 100
    else:
        return 0

def calculate_weighted_method_per_class(tree):
    # total the CC of all of a class's methods
    # get a list of all methods using filter
    # for each method, calculate the CC
    return 0

def calculate_depth_of_inheritance(tree):
    # assuming inheritance has something to do with the modifier attribute?
    return 0

def calculate_coupling_between_objects(tree):
    # count number of times a different class's methods or attributes are used in the class in question
    # maybe something to do with member attribute?
    return 0

def main():
    # set the path
    path = 'main.java'

    # get the concat file
    concat_line, comment_count = util.read_file(path, 0)

    # check if the path contains .java to use the proper library
    if '.java' in path:
        # create the tree
        tree = javalang.parse.parse(concat_line)
        print(tree)
        # demonstrate the 'search' function
        attribute_set = util.get_attribute_set(tree)
        value_list = []
        search_attr = 'value'
        for x in attribute_set:
            value_list = util.search(tree, x, search_attr)

        # print the tree
        util.pretty_print(tree)
        calculate_McGabe_cyclomatic_complexity(tree)
        calculate_SLOC(tree)
        calculate_comment_percentage(tree, comment_count)

if __name__ == '__main__':
    main()
