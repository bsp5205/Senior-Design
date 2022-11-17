import javalang
import clang
import utilities as util

def calculate_McGabe_cyclomatic_complexity(tree):
    # https://www.theserverside.com/feature/How-to-calculate-McCabe-cyclomatic-complexity-in-Java
    cc = 1
    cc_list = []
    # get relevant lists
    method_list = util.custom_filter(tree, 'MethodDeclaration')
    # iterative_list = util.custom_filter(tree, 'WhileStatement') + util.custom_filter(tree, 'ForStatement')

    for method_num in range(len(method_list)):  # loop through if/else if/else statements
        body_list = method_list[method_num].body
        for body_list_num in range(len(body_list)):
            if isinstance(body_list[body_list_num], javalang.tree.IfStatement):
                # print('if')
                cc += 1  # if
            if isinstance(body_list[body_list_num], javalang.tree.IfStatement) and hasattr(body_list[body_list_num], 'else_statement'):
                # print('elseif')
                cc += 1  # else if
            if isinstance(body_list[body_list_num], javalang.tree.IfStatement) and hasattr(body_list[body_list_num], 'then_statement'):
                # print('else')
                cc += 1  # else

            if isinstance(body_list[body_list_num], javalang.tree.WhileStatement):
                # print('while')
                cc += 1  # WhileStatement

            if isinstance(body_list[body_list_num], javalang.tree.ForStatement):
                # print('for')
                cc += 1  # ForStatement

        cc_list.append(cc)
        cc = 1

    return cc_list

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
    if_statement_list = util.custom_filter(tree, 'MethodDeclaration')
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

    return sloc

def calculate_comment_percentage(tree, number_of_comments):
    sloc = calculate_SLOC(tree)
    if sloc > 0:
        return round((number_of_comments/sloc) * 100, 2)
    else:
        return 0

def calculate_weighted_method_per_class(tree):
    cc_list = calculate_McGabe_cyclomatic_complexity(tree)
    return sum(cc_list)

def recursive_check(tree, subtree, height):
    # print(subtree)
    # children_list = subtree.implements
    # print(children_list)
    implement_list = subtree.implements
    for subtree_num in range(len(implement_list)):
        # print(subtree.name, 'implements', subtree.implements[0].name)
        class_list = util.custom_filter(tree, 'ClassDeclaration')
        for class_num in range(len(class_list)):
            # print('checking class', class_list[class_num].name)
            if class_list[class_num].name == subtree.implements[0].name:
                subtree = class_list[class_num]
                return recursive_check(tree, subtree, height + 1)

    return height

def calculate_depth_of_inheritance(tree):
    dit = 0
    class_list = util.custom_filter(tree, 'ClassDeclaration')
    for class_num in range(len(class_list)):
        class_being_checked = class_list[class_num]
        dit_new = recursive_check(tree, class_being_checked, 0)
        if dit_new > dit:
            dit = dit_new

    return dit

def calculate_coupling_between_objects(tree):
    # count number of times a different class's methods or attributes are used in the class in question
    # get a list of all classes
    # for each ClassDeclaration.body[x], pull each MethodDeclaration, and then create an entry {ClassDeclaration:MethodDeclaration}
    # add using dictionary_name[key] = value
    cbo = 0
    method_dict = {}
    attribute_dict = {}
    class_list = util.custom_filter(tree, 'ClassDeclaration')
    for class_num in range(len(class_list)):
        class_body = class_list[class_num].body
        for instance in class_body:
            if isinstance(instance, javalang.tree.MethodDeclaration):
                method_dict[class_list[class_num].name] = str(instance.name)
                if len(method_dict) > 0 and instance.name in method_dict.values() and (class_list[class_num].name, instance.name) not in method_dict.items():
                    cbo += 1
            elif isinstance(instance, javalang.tree.FieldDeclaration):
                attribute_dict[class_list[class_num].name] = str(instance.type.name)
                if len(attribute_dict) > 0 and instance.type.name in attribute_dict.values() and (class_list[class_num].name, instance.type.name) not in attribute_dict.items():
                    cbo += 1

    # print(method_dict)
    # print(attribute_dict)
    return cbo

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
        print('calculate_McGabe_cyclomatic_complexity:', calculate_McGabe_cyclomatic_complexity(tree))
        print('calculate_SLOC:', calculate_SLOC(tree))
        print('calculate_comment_percentage:', calculate_comment_percentage(tree, comment_count))
        print('calculate_weighted_method_per_class:', calculate_weighted_method_per_class(tree))
        print('calculate_depth_of_inheritance:', calculate_depth_of_inheritance(tree))
        print('calculate_coupling_between_objects:', calculate_coupling_between_objects(tree))
if __name__ == '__main__':
    main()
