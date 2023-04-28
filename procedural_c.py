import os.path
import clang.cindex as ci
import math

operator_dict = {}
operands_dict = {}

def pretty_print(cursor):
    print(f'{cursor.spelling}', end=" ")
    
    if cursor.access_specifier is not ci.AccessSpecifier.INVALID:
        print(cursor.access_specifier, end=" ")
    
    for token in cursor.get_tokens():
        print(token.spelling)


def pretty_print_tokens(cursor):
    print(f'{cursor.spelling}', end=" ")

    if cursor.access_specifier is not ci.AccessSpecifier.INVALID:
        print(cursor.access_specifier)

    for token in cursor.get_tokens():
        tokenKind = token.kind
        print(f"{token.spelling} {tokenKind.name}")


def pretty_print_cursors(cursor):
    num = 0
    for i in cursor.get_children():
        print(i.kind.name, end=" ")
        for item in i.get_tokens():
            print(item.spelling, end=" ")
        print()
        pretty_print_cursors(i)


# Finds all Cursors with the given kind
# ex: "VAR_DECL"
def find_cursor_kinds_by_type(cursor, kind):
    num = 0
    for i in cursor.get_children():
        if i.kind.name == kind:
            num += 1
        num += find_cursor_kinds_by_type(i, kind)
    return num


# Calculate lines of code (ELOC)
def effective_lines_of_code(filename):
    file = open(filename, "r")
    lines = file.readlines()
    in_comment = False
    count = 0
    for line in lines:
        first_two = line.strip()[:2]
        whole_line = line.strip()
        if whole_line == "":
            blank_line = True
        else:
            blank_line = False
        if '/*' in line:
            in_comment = True
        if '*/' in line:
            in_comment = False
        if ('//' != first_two and '/*' != first_two and '*/' != first_two and not in_comment and not blank_line and
                '{' != whole_line and '}' != whole_line):
            count += 1
    return count


# Calculate lines of code (KLOC)
def kilo_lines_of_code(filename):
    return effective_lines_of_code(filename) / 1000


# Calculate amount of assignments, branches, and conditionals (ABC)
def assignments_branches_conditionals(cursor):
    assignments = branches = conditionals = 0

    assignments += (find_cursor_kinds_by_type(cursor, "VAR_DECL")
                    + find_cursor_kinds_by_type(cursor, "UNARY_OPERATOR")
                    + find_cursor_kinds_by_type(cursor, "COMPOUND_ASSIGNMENT_OPERATOR")
                    + find_cursor_kinds_by_type(cursor, "BINARY_OPERATOR"))

    branches += (find_cursor_kinds_by_type(cursor, "CALL_EXPR")
                 + find_cursor_kinds_by_type(cursor, "CXX_NEW_EXPR")
                 + find_cursor_kinds_by_type(cursor, "CXX_DELETE_EXPR")
                 + find_cursor_kinds_by_type(cursor, "GOTO_STMT"))

    conditionals += (find_cursor_kinds_by_type(cursor, "CXX_CATCH_STMT")
                 + find_cursor_kinds_by_type(cursor, "CXX_TRY_STMT")
                 + find_cursor_kinds_by_type(cursor, "CASE_STMT")
                 + find_cursor_kinds_by_type(cursor, "DEFAULT_STMT"))

    return assignments + branches + conditionals


# Calculate program length (N)
def halstead_program_length(cursor):
    return total_operands(cursor) + total_operators(cursor)


def total_operands(cursor):
    count = 0
    
    count += (find_cursor_kinds_by_type(cursor, "DECL_REF_EXPR")
              + find_cursor_kinds_by_type(cursor, "VAR_DECL")
              + find_cursor_kinds_by_type(cursor, "INTEGER_LITERAL"))

    count -= find_cursor_kinds_by_type(cursor, "CALL_EXPR")

    for t in cursor.get_tokens():
        if '"' in t.spelling:
            count += 1

    return int(count)


def total_operators(cursor):
    count = 0

    count += (find_cursor_kinds_by_type(cursor, "FUNCTION_DECL")
              + find_cursor_kinds_by_type(cursor, "CALL_EXPR")
              + find_cursor_kinds_by_type(cursor, "DECL_STMT"))

    for t in cursor.get_tokens():
        kind = str(t.kind)
        spelling = t.spelling
        if kind == "TokenKind.PUNCTUATION" and spelling != ")" and spelling != "}" and spelling != "]":
            count += 1
    return count


def get_cursor_distinct_operators(cursor):
    count = 0

    for i in cursor.get_children():
        kind_name = i.kind.name

        if kind_name == "FUNCTION_DECL" or kind_name == "DECL_STMT" or kind_name == "CALL_EXPR":
            gen = i.get_tokens()
            value = next(gen).spelling

            if value not in operator_dict:
                operator_dict[value] = 0
        get_cursor_distinct_operators(i)
    return


def distinct_operators(cursor):
    count = get_cursor_distinct_operators(cursor)

    for t in cursor.get_tokens():
        kind = str(t.kind)
        spelling = t.spelling
        if kind == "TokenKind.PUNCTUATION" and spelling != ")" and spelling != "}" and spelling != "]":
            operator_dict[spelling] = 0

    return len(operator_dict.values())


def get_cursor_distinct_operands(cursor):
    count = 0

    for i in cursor.get_children():
        kind_name = i.kind.name

        if (kind_name == "VAR_DECL" or
                kind_name == "INTEGER_LITERAL" or kind_name == "STRING_LITERAL"):
            gen = i.get_tokens()
            token = next(gen)
            while str(token.kind) == "TokenKind.KEYWORD":
                token = next(gen)
            value = token.spelling
            if value not in operands_dict:
                operands_dict[value] = 0
        get_cursor_distinct_operands(i)

    return


def distinct_operands(cursor):
    get_cursor_distinct_operands(cursor)
    return len(operands_dict.values())


# Calculate program vocabulary (n)
def halstead_program_vocabulary(cursor):
    vocab_list = []
    
    for vocab in cursor.get_tokens():
        if vocab.spelling == ")" or vocab.spelling == "}" or vocab.spelling == "]":
            continue
        try:
            vocab_list.index(vocab.spelling)
        except:
            vocab_list.append(vocab.spelling)
            pass
    
    return len(vocab_list)


# Calculates program volume (V)
def halstead_program_volume(cursor):
    N = halstead_program_length(cursor)
    n = halstead_program_vocabulary(cursor)
    V = N * math.log(n, 2)
    return round(V, 2)


# Calculates difficulty (D)
def halstead_difficulty(cursor):
    return round(distinct_operators(cursor)/2 * (total_operands(cursor) / distinct_operands(cursor)), 2)


def halstead_level(cursor):
    return round(1 / halstead_difficulty(cursor))


def halstead_effort(cursor):
    return round(halstead_program_volume(cursor) * halstead_difficulty(cursor), 2)


def halstead_bugs(cursor):
    return round(halstead_program_volume(cursor) / 3000, 2)


# Calculate token count (TC)
def token_count(cursor):
    count = 0
    
    for i in cursor.get_tokens():
        if i.kind != ci.TokenKind.COMMENT:
            count += 1
        
    return count


# Print all the procedural function calculations
def print_all(filename):
    # Create 
    index = ci.Index.create()
    tu = index.parse(filename)
    cursor = tu.cursor

    print(f"ELOC: {effective_lines_of_code(filename)}")
    print(f"KLOC: {kilo_lines_of_code(filename)}")
    print(f"ABC: {assignments_branches_conditionals(tu.cursor)}")
    print(f"N: {halstead_program_length(tu.cursor)}")
    print(f"n: {halstead_program_vocabulary(tu.cursor)}")
    print(f"V: {halstead_program_volume(tu.cursor)}")
    print(f"D: {halstead_difficulty(cursor)}")
    print(f"L: {halstead_level(cursor)}")
    print(f"E: {halstead_effort(cursor)}")
    print(f"B: {halstead_bugs(cursor)}")
    print(f"TC: {token_count(tu.cursor)}")


# Main function
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    ci.Config.set_library_file(dir_path + '/libclang.dll')
    print_all('TestAssignmentFiles/even.c')


# Make sure doesn't run on import
if __name__ == '__main__':
    main()
