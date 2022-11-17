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

    return cc

def calculate_SLOC(tree):
    # class.name +2
    # method.name +2
    #   (for each method body):
    #       LocalVariableDeclaration +1
    #       IfStatement +2
    #       ElseIfStatement (represented as nested IfStatement) +2
    #       ElseStatement +1
    #       StatementExpression +1
    #       ForStatement +2
    #       WhileStatement +2
    #
    return 0

def calculate_comment_percentage(tree):
    # maybe something with the "labels"?
    # number of comments / LOC
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
    concat_line = util.read_file(path)

    # check if the path contains .java to use the proper library
    if '.java' in path:
        # create the tree
        tree = javalang.parse.parse(concat_line)
        # print(tree)
        # demonstrate the 'search' function
        attribute_set = util.get_attribute_set(tree)
        value_list = []
        search_attr = 'value'
        for x in attribute_set:
            value_list = util.search(tree, x, search_attr)
            # if value_list:
            #     print('Your set of returned values is', value_list)

        # print the tree
        util.pretty_print(tree)
        calculate_McGabe_cyclomatic_complexity(tree)

if __name__ == '__main__':
    main()
