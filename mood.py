import javalang
import main as home_file
import utilities as util


def recursive_parent_methods(tree):
    # method to assist polymorphism factor
    # Climbs up the subtree ladder
    # returns all methods possible to override
    add_methods = 0
    extend_list = tree.extends

    # tree of parent class
    class_name = next(iter(extend_list))[1].name

    path = 'TestAssignmentFiles/' + class_name + '.java'

    try:
        concat_line, comment_count = util.read_file(path, 0)
        parent_tree = javalang.parse.parse(concat_line)
        # check if parent extends
        class_list = util.custom_filter_javalang_tree(parent_tree, 'javalang.tree.ClassDeclaration')
        for class_num in range(len(class_list)):
            cur_class = class_list[class_num]

            if cur_class.extends is not None:
                add_methods += recursive_parent_methods(cur_class)

        # add these methods to parent methods if not private
        parent_method_list = util.custom_filter_javalang_tree(parent_tree, 'javalang.tree.MethodDeclaration')
        for method_num in range(len(parent_method_list)):
            cur_method = parent_method_list[method_num]
            if next(iter(cur_method.modifiers)) != 'private':
                add_methods = add_methods + 1
    finally:
        return add_methods


def calculate_method_hiding_factor(tree):
    # counts the number of hidden methods in a class
    # counts the total number of methods in a class
    # divides the numbers
    MHF = 0
    hidden_meth = 0
    total_meth = 0
    class_list = util.custom_filter_javalang_tree(tree, 'javalang.tree.ClassDeclaration')
    for class_num in range(len(class_list)):
        class_body = class_list[class_num].body
        for instance in class_body:
            if isinstance(instance, javalang.tree.MethodDeclaration):
                total_meth = total_meth + 1

                # methods without access modifiers in java are public
                if len(instance.modifiers) > 0:
                    for meth_vis in iter(instance.modifiers):
                        if (meth_vis == 'private'):
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
    class_list = util.custom_filter_javalang_tree(tree, 'javalang.tree.ClassDeclaration')
    for class_num in range(len(class_list)):
        class_body = class_list[class_num].body
        for instance in class_body:
            if isinstance(instance, javalang.tree.FieldDeclaration):
                total_attr = total_attr + 1

                # methods without access modifiers in java are public?
                if len(instance.modifiers) > 0:
                    attr_vis = next(iter(instance.modifiers))
                    if (attr_vis == 'private' or attr_vis == 'protected'):
                        hidden_attr = hidden_attr + 1

    # local variables are not attributes
    if total_attr == 0:
        AHF = 0.0
    else:
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
    def_method_list = util.custom_filter_javalang_tree(tree, 'javalang.tree.MethodDeclaration')
    for method_num in range(len(def_method_list)):
        def_meth = def_meth + 1
        if len(def_method_list[method_num].annotations) > 0:
            if def_method_list[method_num].annotations[0].name == "Override":
                inherit_meth.append(def_method_list[method_num].name)

    invoc_method_list = util.custom_filter(tree, 'MethodInvocation')
    for invoc_method_num in range(len(invoc_method_list)):
        cur_method = invoc_method_list[invoc_method_num]
        if(cur_method.qualifier != '' and cur_method.qualifier != None):
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
    def_attr_list = util.custom_filter_javalang_tree(tree, 'javalang.tree.FieldDeclaration')
    for attr_num in range(len(def_attr_list)):
        def_attr = def_attr + 1

    invoc_attr_list = util.custom_filter_javalang_tree(tree, 'javalang.tree.MemberReference')
    for invoc_attr_num in range(len(invoc_attr_list)):
        cur_attr = invoc_attr_list[invoc_attr_num]
        if (cur_attr.qualifier != '' and cur_attr.qualifier != None):
            cur_attr_string = cur_attr.qualifier + "'" + cur_attr.member
            if (cur_attr_string not in inherit_attr):
                inherit_attr.append(cur_attr_string)
    tot_attr = len(inherit_attr) + def_attr

    if tot_attr == 0:
        AIF = 0.0
    else:
        AIF = len(inherit_attr) / tot_attr

    return AIF


def calculate_coupling_factor(tree):
    CF = 0.0
    couples = 0
    max_couples = 0
    couple_meth = []
    coupled_class = []
    parent = ''

    class_list = util.custom_filter_javalang_tree(tree, 'javalang.tree.ClassDeclaration')
    for class_num in range(len(class_list)):
        cur_class = class_list[class_num]
        if cur_class.implements is not None:
            # coupling due to inheritance is not counted
            parent = cur_class.implements[0].name

        elif cur_class.extends is not None:
            # coupling due to inheritance is not counted
            extend_list = cur_class.extends
            parent = next(iter(extend_list))[1].name

        invoc_method_list = util.custom_filter_javalang_tree(tree, 'javalang.tree.MethodInvocation')
        for invoc_method_num in range(len(invoc_method_list)):
            cur_method = invoc_method_list[invoc_method_num]
            if (cur_method.qualifier != '' and cur_method.qualifier != parent and cur_method.qualifier != None):
                cur_method_string = cur_method.qualifier + "." + cur_method.member
                if cur_method.qualifier not in coupled_class and cur_method.qualifier != 'System.out':
                    coupled_class.append(cur_method.qualifier)
                if (cur_method_string not in couple_meth):
                    couple_meth.append(cur_method_string)

        for qualifier in coupled_class:
            max_couples = home_file.coupled_methods(cur_class.name, qualifier)
    couples = len(couple_meth)
    if max_couples != 0:
        CF = couples/max_couples
    return CF


def calculate_polymorphism_factor(tree):
    POF = 0.0
    num_overrides = 0
    possible_overrides = 0
    class_list = util.custom_filter_javalang_tree(tree, 'javalang.tree.ClassDeclaration')
    for class_num in range(len(class_list)):
        cur_class = class_list[class_num]

        if cur_class.implements is not None:
            # if program compiles and class implements POF needs to be 1
            POF = 1.0

        if cur_class.extends is not None:
            possible_overrides = recursive_parent_methods(cur_class)

        # if possible overrides are 0 POF is 0
        if possible_overrides != 0:
            # getting the overridden methods
            meth_list = util.custom_filter_javalang_tree(class_list[class_num], 'javalang.tree.MethodDeclaration')
            for meth_num in range(len(meth_list)):
                cur_meth = meth_list[meth_num]
                if len(cur_meth.annotations) > 0:
                    if cur_meth.annotations[0].name == "Override":
                        num_overrides = num_overrides + 1
            POF = num_overrides/possible_overrides

    return POF


def main():
    print("f")


if __name__ == "__main__":
    main()