import clang.cindex
import sys

def pretty_print(node):
    print(f'{node.spelling}', end=" ")
    
    if node.access_specifier is not clang.cindex.AccessSpecifier.INVALID:
        print(node.access_specifier)
    
    for token in node.get_tokens():
        print(token.spelling)
    
    # for c in node.get_children():
    #     pretty_print(c)

def find_typerefs(node, typename):
    """ Find all references to the type named 'typename'
    """
    if node.kind.is_reference():
        ref_node = node.referenced
        if ref_node.spelling == typename:
            print('Found %s [line=%s, col=%s]' % (
                typename, node.location.line, node.location.column))
    # Recurse for children of this node
    for c in node.get_children():
        find_typerefs(c, typename)

def main():
    index = clang.cindex.Index.create()
    tu = index.parse(sys.argv[1])
    print('Translation unit:', tu.spelling)
    pretty_print(tu.cursor)
    find_typerefs(tu.cursor, sys.argv[2])
    

if __name__ == '__main__':
    main()