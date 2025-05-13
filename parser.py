import ast

def parse_code(code):
    try:
        tree=ast.parse(code)
        return tree
    except SyntaxError as e:
        print('Syntax error')
        return None
if __name__=='__main__':
    sample_code = '''
    x = 10
    def greet():
        print("Hello")
    '''
    tree = parse_code(sample_code)
    print(ast.dump(tree))