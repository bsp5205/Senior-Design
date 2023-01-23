import javalang
import clang
import utilities as util
import math

file_name = 'main.java'

# Calculate kilo lines of code (KLOC)
def calculate_KLOC(tree):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    file.close()
    return len(lines) / 1000

# Calculate effective lines of code (ELOC)
def calculate_ELOC(tree):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    count = 0
    for line in lines:
        if not line.isspace():
            count += 1
    file.close()
    return str(count)

# Calculate the number of assignments, branches, and conditions (ABC)
def calculate_ABC(tree):
    # Find prefixes and postfixes for A and unary for C
    fix_list = util.search(tree, 'MemberReference', 'postfix_operators') + util.search(tree, 'MemberReference', 'prefix_operators')
    fix_count = 0
    unary_count = 0

    for fix in fix_list:
        if fix:
            op = fix.pop()
            if op == '++' or op == '--':
                fix_count += 1
            else:
                unary_count += 1

    # Find binary operators for C
    binary_list = util.search(tree, 'BinaryOperation', 'operator')
    binary_count = 0
    for operation in binary_list:
        if '=' in operation or '<' in operation or '>' in operation:
            binary_count += 1

    # Finds else statement count for C
    statement_list = util.custom_filter(tree, 'IfStatement')
    else_count = 0
    for statement in statement_list:
        if statement.attrs[3]:
            if type(getattr(statement, statement.attrs[3])) is javalang.tree.BlockStatement:
                else_count += 1

    # Find ABC amounts for metric
    a = len(util.custom_filter(tree, 'VariableDeclarator') + util.custom_filter(tree, 'Assignment')) + fix_count
    b = len(util.custom_filter(tree, 'MethodInvocation') + util.custom_filter(tree, 'ClassCreator'))
    c = len(util.custom_filter(tree, 'TryStatement') + util.custom_filter(tree, 'CatchClause') + util.custom_filter(tree, 'SwitchStatement')) + unary_count + binary_count + else_count
    abc = math.sqrt(pow(a, 2) + pow(b, 2) + pow(c, 2))

    # Assess quality
    if(abc <= 10):
        quality = "Best"
    elif(abc <= 20):
        quality = "Good"
    elif(abc <= 40):
        quality = "Needs refactoring"
    elif(abc <= 60):
        quality = "Needs justifying"
    else:
        quality = "Unacceptable"

    return '{0:.3g} '.format(abc) + '{' + 'A: {}, B: {}, C: {}'.format(a, b, c) + '} ' + quality

# Halstead metrics

# Calculate Halstead operators and operands
def calculate_Halstead_ops(tree):
    global operators, operands, n1, n2, N1, N2
    operators, operands = {}, {}
    N1, N2 = 0, 0

    # Add operator to list
    add_symbol_operators()
    add_operator(tree, javalang.tree.ReferenceType, 'name')
    add_operator(tree, javalang.tree.Invocation, 'member')
    add_operator(tree, javalang.tree.Declaration, 'modifiers')
    add_operator(tree, javalang.tree.MethodDeclaration, 'name')
    add_operator(tree, javalang.tree.MethodDeclaration, 'return_type')
    add_operator(tree, javalang.tree.BasicType, 'name')

    statement_list = util.custom_filter(tree, 'ClassDeclaration')
    for statement in statement_list:
        if operators.get('class'):
            operators['class'] += 1
        else:
            operators['class'] = 1


    # Add operand to list
    add_operand(tree, javalang.tree.VariableDeclarator, 'name')
    add_operand(tree, javalang.tree.FormalParameter, 'name')
    add_operand(tree, javalang.tree.Literal, 'value')
    add_operand(tree, javalang.tree.MemberReference, 'member')

    for item in operands.values():
        N2 += item

    for item in operators.values():
        N1 += item

    n1 = len(operators)
    n2 = len(operands)

    # print(operators)
    # print(operands)
    # print('N1: {} N2: {} n1: {} n2: {}'.format(N1, N2, n1, n2))

    return

def add_operand(tree, param, attribute):
    operand_list = tree.filter(param)
    for o, operand in operand_list:
        try:
            value_set = getattr(operand, attribute)
            if operands.get(value_set):
                operands[value_set] += 1
            else:
                operands[value_set] = 1
        except:
            pass
    return

def add_operator(tree, param, attribute):
    operator_list = tree.filter(param)
    for o, operator in operator_list:
        try:
            value_set = getattr(operator, attribute)
            if operators.get(value_set):
                operators[value_set] += 1
            else:
                operators[value_set] = 1
        except:
            try:
                value_set = getattr(operator, attribute)
                for value in value_set:
                    if operators.get(value):
                        operators[value] += 1
                    else:
                        operators[value] = 1
            except:
                pass
            pass

# Find all parenthesis and curly brackets and add to dictionary
def add_symbol_operators():
    with open('main.java', 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line.find('{') != -1:
            if operators.get('{'):
                operators['{'] += line.count('{')
            else:
                operators['{'] = line.count('{')
        if line.find('(') != -1:
            if operators.get('('):
                operators['('] += line.count('(')
            else:
                operators['('] = line.count('(')
        if line.find('[') != -1:
            if operators.get('['):
                operators['['] += line.count('[')
            else:
                operators['['] = line.count('[')
        if line.find(';') != -1:
            if operators.get(';'):
                operators[';'] += line.count(';')
            else:
                operators[';'] = line.count(';')

    file.close()

# Calculate Halstead program length (N)
def calculate_Halstead_program_length():
    global N
    N = N1 + N2
    return N

# Calculate Halstead program vocabulary (n)
def calculate_Halstead_program_vocabulary():
    global n
    n = n1 + n2
    return n

# Calculate Halstead program volume (V)
def calculate_Halstead_program_volume():
    global V
    V = N * math.log(n, 2)
    return V

# Calculate Halstead program difficulty (D)
def calculate_Halstead_program_difficulty():
    global D
    D = (n1 / 2) * (N2 / n2)
    return D

# Calculate Halstead program level (L)
def calculate_Halstead_program_level():
    global L
    L = 1 / D
    return L

# Calculate Halstead program effort (E)
def calculate_Halstead_program_effort():
    global E
    E = V * D
    return E

# Calculate Halstead number of delivered bugs (B)
def calculate_Halstead_number_of_bugs():
    global B
    B = V / 3000
    return B

# Calculate token count (TC)
def calculate_token_count():
    return n

# Calculate cyclomatic complexity (MCC)
def calculate_MMCC(tree):
    return 12

# Prints all metrics
def print_all(tree):
    print('KLOC: ' + str(calculate_KLOC(tree)) + ' Lines')
    print('ELOC: ' + str(calculate_ELOC(tree)) + ' Lines')
    print('ABC: ' + str(calculate_ABC(tree)))
    calculate_Halstead_ops(tree)
    print('N: ' + '{0:.3g} '.format(calculate_Halstead_program_length()))
    print('n: ' + '{0:.3g} '.format(calculate_Halstead_program_vocabulary()))
    print('V: ' + '{0:.3g} '.format(calculate_Halstead_program_volume()))
    print('D: ' + '{0:.3g} '.format(calculate_Halstead_program_difficulty()))
    print('L: ' + '{0:.3g} '.format(calculate_Halstead_program_level()))
    print('E: ' + '{0:.3g} '.format(calculate_Halstead_program_effort()))
    print('B: ' + '{0:.3g} '.format(calculate_Halstead_number_of_bugs()))
    print('TC: ' + '{0:.3g} '.format(calculate_token_count()))
    # print('MCC: ' + str(calculate_MMCC(tree)))
def main():
    path = 'main.java'

    concat_line, comment_count = util.read_file(path, 0)
    tree = javalang.parse.parse(concat_line)

    print_all(tree)

if __name__ == "__main__":
    main()
