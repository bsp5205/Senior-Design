import javalang
import clang
import procedural
from enum import Enum

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
        return height+1


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

def recursive_parent_methods(tree):
    # method to assist polymorphism factor
    # Climbs up the subtree ladder
    # returns all methods possible to override
    add_methods = 0
    extend_list = tree.extends

    # tree of parent class
    class_name = next(iter(extend_list))[1].name

    path = class_name + '.java'
    concat_line, comment_count = util.read_file(path, 0)
    parent_tree = javalang.parse.parse(concat_line)
    # check if parent extends
    class_list = util.custom_filter(parent_tree, 'ClassDeclaration')
    for class_num in range(len(class_list)):
        cur_class = class_list[class_num]
        if cur_class.extends is not None:
            add_methods = recursive_parent_methods(cur_class)

    # add these methods to parent methods if not private
    parent_method_list = util.custom_filter(parent_tree, 'MethodDeclaration')
    for method_num in range(len(parent_method_list)):
        cur_method = parent_method_list[method_num]
        if next(iter(cur_method.modifiers)) != 'private':
            add_methods = add_methods + 1

    return add_methods

def coupled_methods(class_name, couple):
    methods = 0

    path = class_name + '.java'
    concat_line, comment_count = util.read_file(path, 0)
    tree = javalang.parse.parse(concat_line)

    invoc_method_list = util.custom_filter(tree, 'MethodInvocation')
    for invoc_method_num in range(len(invoc_method_list)):
        cur_method = invoc_method_list[invoc_method_num]
        if (cur_method.qualifier == couple):
            method = method + 1

    return methods

def calculate_method_hiding_factor(tree):
    # counts the number of hidden methods in a class
    # counts the total number of methods in a class
    # divides the numbers
    MHF = 0
    hidden_meth = 0
    total_meth = 0
    class_list = util.custom_filter(tree, 'ClassDeclaration')
    for class_num in range(len(class_list)):
        class_body = class_list[class_num].body
        for instance in class_body:
            if isinstance(instance, javalang.tree.MethodDeclaration):
                total_meth = total_meth + 1
                meth_vis = next(iter(instance.modifiers))
                if(meth_vis == 'private'):
                    hidden_meth = hidden_meth + 1

    MHF = hidden_meth/total_meth
    return MHF

def calculate_attribute_hiding_factor(tree):
    # counts the number of hidden attributes in a class
    # counts the total number of attributes in a class
    # divides the numbers
    AHF = 0
    hidden_attr = 0
    total_attr = 0
    class_list = util.custom_filter(tree, 'ClassDeclaration')
    for class_num in range(len(class_list)):
        class_body = class_list[class_num].body
        for instance in class_body:
            if isinstance(instance, javalang.tree.FieldDeclaration):
                total_attr = total_attr + 1
                attr_vis = next(iter(instance.modifiers))
                if(attr_vis == 'private'):
                    hidden_attr = hidden_attr + 1

    AHF = hidden_attr/total_attr
    return AHF

def calculate_method_inheritance_factor(tree):
    # counts the inherited methods
    # counts the total number of methods
    # divides the numbers
    MIF = 0
    # getting the methods defined in the class
    def_meth = 0
    tot_meth = 0
    inherit_meth = []
    def_method_list = util.custom_filter(tree, 'MethodDeclaration')
    for method_num in range(len(def_method_list)):
        def_meth = def_meth + 1
        if len(def_method_list[method_num].annotations) > 0:
            if def_method_list[method_num].annotations[0].name == "Override":
                inherit_meth.append(def_method_list[method_num].name)

    invoc_method_list = util.custom_filter(tree, 'MethodInvocation')
    for invoc_method_num in range(len(invoc_method_list)):
        cur_method = invoc_method_list[invoc_method_num]
        if(cur_method.qualifier != ''):
            cur_method_string = cur_method.qualifier + "." + cur_method.member
            if(cur_method_string not in inherit_meth):
                inherit_meth.append(cur_method_string)

    tot_meth = len(inherit_meth) + def_meth
    MIF = len(inherit_meth)/tot_meth
    return MIF

def calculate_attribute_inheritance_factor(tree):
    # counts the inherited attributes
    # counts the total number of attributes
    # divides the numbers
    AIF = 0
    def_attr = 0
    tot_attr = 0
    inherit_attr = []
    def_attr_list = util.custom_filter(tree, 'FieldDeclaration')
    for attr_num in range(len(def_attr_list)):
        def_attr = def_attr + 1

    invoc_attr_list = util.custom_filter(tree, 'MemberReference')
    for invoc_attr_num in range(len(invoc_attr_list)):
        cur_attr = invoc_attr_list[invoc_attr_num]
        if (cur_attr.qualifier != ''):
            cur_attr_string = cur_attr.qualifier + "'" + cur_attr.member
            if (cur_attr_string not in inherit_attr):
                inherit_attr.append(cur_attr_string)
    tot_attr = len(inherit_attr) + def_attr
    AIF = len(inherit_attr) / tot_attr
    return AIF

def calculate_coupling_factor(tree):
    CF = 0.0
    couples = 0
    max_couples = 0
    couple_meth = []
    coupled_class = []
    parent = ''

    class_list = util.custom_filter(tree, 'ClassDeclaration')
    for class_num in range(len(class_list)):
        cur_class = class_list[class_num]
        if cur_class.implements is not None:
            # coupling due to inheritance is not counted
            parent = cur_class.implements[0].name

        elif cur_class.extends is not None:
            # coupling due to inheritance is not counted
            extend_list = cur_class.extends
            parent = next(iter(extend_list))[1].name

        invoc_method_list = util.custom_filter(tree, 'MethodInvocation')
        for invoc_method_num in range(len(invoc_method_list)):
            cur_method = invoc_method_list[invoc_method_num]
            if (cur_method.qualifier != '' and cur_method.qualifier != parent):
                cur_method_string = cur_method.qualifier + "." + cur_method.member
                if cur_method.qualifier not in coupled_class and cur_method.qualifier != 'System.out':
                    coupled_class.append(cur_method.qualifier)
                if (cur_method_string not in couple_meth):
                    couple_meth.append(cur_method_string)

        for qualifier in coupled_class:
            print(qualifier)
            print("\n")
            print(cur_class.name)
            max_couples = coupled_methods(qualifier, cur_class.name)

    couples = len(couple_meth)
    if max_couples != 0:
        CF = couples/max_couples
    return CF

def calculate_polymorphism_factor(tree):
    POF = 0.0
    num_overrides = 0
    possible_overrides = 0
    class_list = util.custom_filter(tree, 'ClassDeclaration')
    for class_num in range(len(class_list)):
        cur_class = class_list[class_num]

        if cur_class.implements is not None:
            # if program compiles and class implements POF needs to be 1
            POF = 1.0

        elif cur_class.extends is not None:
            possible_overrides = recursive_parent_methods(cur_class)

        # if possible overrides are 0 POF is 0
        if possible_overrides != 0:
            # getting the overridden methods
            meth_list = util.custom_filter(tree, 'MethodDeclaration')
            for meth_num in range(len(meth_list)):
                cur_meth = meth_list[meth_num]
                if len(cur_meth.annotations) > 0:
                    if cur_meth.annotations[0].name == "Override":
                        num_overrides = num_overrides + 1
            POF = num_overrides/possible_overrides

    return POF

def main():
    # set the path
    path = 'main.java'

    # get the concat file
    concat_line, comment_count = util.read_file(path, 0)

    # check if the path contains .java to use the proper library
    if '.java' in path:
        # create the tree
        tree = javalang.parse.parse(concat_line)
        # print(tree)
        # demonstrate the 'search' function
        attribute_set = util.get_attribute_set(tree)
        value_list = []
        search_attr = 'name'
        for x in attribute_set:
            value_list = util.search(tree, x, search_attr)
        # print(value_list)

        # print the tree
        # util.pretty_print(tree)

        # script tests
        print('OO Metrics:')
        print('calculate_McGabe_cyclomatic_complexity:', calculate_McGabe_cyclomatic_complexity(tree))
        print('calculate_SLOC:', calculate_SLOC(tree))
        print('calculate_comment_percentage:', calculate_comment_percentage(tree, comment_count))
        print('calculate_weighted_method_per_class:', calculate_weighted_method_per_class(tree))
        print('calculate_depth_of_inheritance:', calculate_depth_of_inheritance(tree))
        print('calculate_coupling_between_objects:', calculate_coupling_between_objects(tree))

        print('\nMOOD Metrics:\ncalculate_method_hiding_factor:', calculate_method_hiding_factor(tree))
        print('calculate_attribute_hiding_factor:', calculate_attribute_hiding_factor(tree))
        print('calculate_method_inheritance_factor:', calculate_method_inheritance_factor(tree))
        print('calculate_attribute_inheritance_factor:', calculate_attribute_inheritance_factor(tree))
        print('calculate_coupling_factor:', calculate_coupling_factor(tree))
        print('calculate_polymorphism_factor:', calculate_polymorphism_factor(tree))

        print('\nProcedural Metrics:')
        procedural.main()


if __name__ == '__main__':
    main()