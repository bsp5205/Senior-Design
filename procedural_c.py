import clang.cindex as ci
import sys
import math

def pretty_print(cursor):
    print(f'{cursor.spelling}', end=" ")
    
    if cursor.access_specifier is not clang.cindex.AccessSpecifier.INVALID:
        print(cursor.access_specifier, end=" ")
    
    for token in cursor.get_tokens():
        print(token.spelling, end=" ")

# Find all references to the type named 'typename'
def find_typerefs(cursor, typename):
    count = 0
    if cursor.kind.is_reference():
        ref_cursor = cursor.referenced
        if ref_cursor.spelling == typename:
            print('Found %s [line=%s, col=%s]' % (
                typename, cursor.location.line, cursor.location.column))
            count += 1
    
    # Recurse for children of this cursor
    for c in cursor.get_children():
        count += find_typerefs(c, typename)
    
    return count

def find_type(cursor, typename):
      
    print("Tokens:")
    for t in cursor.get_tokens():
        print(f"{t.spelling} | {t.kind} | {t.cursor.type}")
            
        
    # print(f"{cursor.kind} {cursor.type}")
    # for c in cursor.get_children():
    #     find_type(c, typename)
        
def find_token_amount(cursor, token):
    print(find_type(cursor, token))
    return

# Calculate lines of code (ELOC)
def effective_lines_of_code(filename):
    file = open(filename, "r")
    lines = file.readlines()
    return len(lines)

# Calculate lines of code (KLOC)
def kilo_lines_of_code(filename):
    return effective_lines_of_code(filename) / 1000

# Calculate amount of assignments, branches, and conditionals (ABC)
def assignments_branches_conditionals(cursor):
    assignments = branches = conditionals = 0
    
    # find_token_amount(cursor, "Person")
    
    return

# Calculate program length (N)
def halstead_program_length(cursor):
    return total_operands(cursor) + total_operators(cursor)

def total_operands(cursor):
    count = 0
    
    for c in cursor.get_children():
        if (c.kind == ci.CursorKind.DECL_REF_EXPR and c.type.spelling != "<overloaded function type>"
            or c.kind == ci.CursorKind.STRING_LITERAL
            or c.kind == ci.CursorKind.INTEGER_LITERAL
            or c.kind == ci.CursorKind.VAR_DECL ):
                count += 1
        count += total_operands(c)
    
    return count

def cursor_operators(cursor):
    count = 0
    
    for c in cursor.get_children():
        if (c.kind == ci.CursorKind.DECL_REF_EXPR and c.type.spelling == "<overloaded function type>"
            or c.kind == ci.CursorKind.FUNCTION_DECL
            or c.kind == ci.CursorKind.DECL_STMT):
                count += 1
        count += cursor_operators(c)
    
    return count

def token_operators(cursor):
    count = 0
    for vocab in cursor.get_tokens():
        if (vocab.kind == ci.TokenKind.PUNCTUATION):
            if vocab.spelling != ")" and vocab.spelling != "}" and vocab.spelling != "]":
                count += 1
    return count

def total_operators(cursor):
    return cursor_operators(cursor) + token_operators(cursor)

def distinct_operators(cursor):
    
    count = 0
    
    for c in cursor.get_children():
        if (c.kind == ci.CursorKind.DECL_REF_EXPR and c.type.spelling == "<overloaded function type>"
            or c.kind == ci.CursorKind.FUNCTION_DECL
            or c.kind == ci.CursorKind.DECL_STMT):
                count += 1
        count += cursor_operators(c)
    
    return count
    
    pass

def distinct_operands(cursor):
    pass

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
    return V

# Calculates difficulty (D)
def halstead_difficulty(cursor):
    pass

# Calculate token count (TC)
def token_count(cursor):
    count = 0
    
    for i in cursor.get_tokens():
        if i.kind != ci.TokenKind.COMMENT:
            count += 1
        
    return count

# Print all of the procedural function calculations
def print_all():
    # Create 
    index = ci.Index.create()
    tu = index.parse(sys.argv[1])
    filename = tu.spelling
    
    print(f"ELOC: {effective_lines_of_code(filename)}")
    print(f"KLOC: {kilo_lines_of_code(filename)}")
    print(f"ABC: {assignments_branches_conditionals(tu.cursor)}")
    print(f"N: {halstead_program_length(tu.cursor)}")
    print(f"n: {halstead_program_vocabulary(tu.cursor)}")
    print(f"V: {round(halstead_program_volume(tu.cursor), 2)}")
    print(f"TC: {token_count(tu.cursor)}")

# Main function
def main():
    print_all()
    
# Make sure doesn't run on import
if __name__ == '__main__':
    main()