import javalang
"""
:param subtree - the current subtree root
Utility function to check if a class found in the tree belongs to javalang
"""
def check_class(subtree):
    if isinstance(subtree, javalang.tree.ClassDeclaration) or isinstance(subtree, javalang.tree.MethodDeclaration) \
            or isinstance(subtree, javalang.tree.FormalParameter) or isinstance(subtree, javalang.tree.StatementExpression) \
            or isinstance(subtree, javalang.tree.ReferenceType) or isinstance(subtree, javalang.tree.BinaryOperation) \
            or isinstance(subtree, javalang.tree.BasicType) or isinstance(subtree, javalang.tree.LocalVariableDeclaration) \
            or isinstance(subtree, javalang.tree.VariableDeclarator) or isinstance(subtree, javalang.tree.IfStatement) \
            or isinstance(subtree, javalang.tree.WhileStatement) or isinstance(subtree, javalang.tree.MemberReference) \
            or isinstance(subtree, javalang.tree.BlockStatement) or isinstance(subtree, javalang.tree.MethodInvocation) \
            or isinstance(subtree, javalang.tree.ForStatement) or isinstance(subtree, javalang.tree.ForControl)\
            or isinstance(subtree, javalang.tree.FieldDeclaration):
        return True
    else:
        return False

"""
:param tree - the tree
Recursive function that will print the tree structure
"""
def pretty_print(tree, indent=0):
    print(' ' * indent + type(tree).__name__ + ':')
    indent += 4
    for path, node in tree.__dict__.items():
        if '__dict__' in dir(node):
            pretty_print(node, indent)
        else:
            if isinstance(node, list):
                print(' ' * indent + path + '[{}]'.format(len(node)))
                for x in range(len(node)):
                    if check_class(node[x]):
                        pretty_print(node[x], indent+4)
                    elif isinstance(node, list):
                        print(' ' * (indent+4) + str(node))
                        # for y in range(len(node)):
                        #     print(' ' * (indent+4) + str(node[y]))
            else:
                print(' ' * indent + path + ': ' + str(node))

"""
:param tree - The tree returned from the library
:param param - The subclass you're looking for
:param field - The attribute name of the subclass
"""
def search(tree, param, field):
    return_list = []
    for x, v in tree.types[0]:
        if type(v).__name__ == param:
            # print('\tChecking', param, 'for', field)
            if hasattr(v, field):
                # print('\t\t' + str(getattr(v, field)))
                return_list.append(getattr(v, field))
    return return_list

"""
:param tree - the tree
:param param - the subclass that is being filtered for
"""
def custom_filter(tree, param):
    return_list = []
    for x, v in tree.types[0]:
        # print(v)
        if type(v).__name__ == param:
            return_list.append(v)
    return return_list

"""
:tree - The tree from javalang
This function will return a LIST of the attributes found inside the tree.types[0] (including duplicates)
"""
def get_attribute_list(tree):
    attribute_list = []
    for x, v in tree.types[0]:
        attribute_list.append(str(type(v).__name__))
    return attribute_list

"""
:param tree - The tree from javalang
This function will return a SET of the attributes found inside the tree.types[0] (excluding duplicates)
"""
def get_attribute_set(tree):
    attribute_set = []
    for x, v in tree.types[0]:
        attribute_set.append(str(type(v).__name__))

    return [*set(attribute_set)]

"""
:param list_to_convert the list that is to be converted to a set (remove duplicates)
This function will return a SET of the list elements
"""
def list_to_set(list_to_convert):
    return[*set(list_to_convert)]

"""
:param path - the path of the java code
This function will open the file and concat the text into one line to be used in javalang ast creation
"""
def read_file(path, comments):
    temp_file = open(path, 'r')
    lines = temp_file.readlines()
    concat_line = ''
    comment_count = 0

    in_comment_block = 0

    for line in lines:
        if in_comment_block:
            comment_count += 1
            concat_line += line.rstrip('\n')
            if '*/' in line:
                in_comment_block = 0
        else:
            # concat_line += line.rstrip('\n')
            if '//' in line and not comments:
                comment_count += 1
                cut_pos = line.index('//')
                line = line[:cut_pos]
                concat_line += line.rstrip('\n')
            elif '/*' in line and not comments:
                comment_count += 1
                in_comment_block = 1
                cut_pos = line.index('/*')
                #line = line[:cut_pos]
                concat_line += line.rstrip('\n')
            else:
                concat_line += line.rstrip('\n')
    temp_file.close()

    return concat_line, comment_count
