import ast

class interpret(ast.NodeVisitor):
    def __init__(self):
        self.env={}
    def visit_Assign(self, node):
        val_name=node.targets[0].id
        val=self.visit(node.value)
        self.env[val_name]=val
        print(f'{val_name}:{val}')
    def visit_Expression(self, node):
        return self.visit(node.value)
    def visit_Constant(self, node):
        return node.value
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            return self.env.get(node.id, f"<undefined:{node.id}>")
        return node.id
    def visit_BinOp(self, node):
        left=self.visit(node.left)
        right=self.visit(node.right)
        if left and right:
            op=type(node.op)
            if op==ast.Add:
                return left + right
            elif op==ast.Sub:
                c=left-right
                return c
            elif op==ast.Mult:
                c=left*right
                return c
            elif op==ast.Div:
                c=left/right
                return c
            else:
                raise Exception('Unsupported operation')
    def visit_Call(self, node):
        func=node.func.id
        args=[self.visit(i) for i in node.args]

        if func=='print':
            print(*args)
        else:
            print(f"Call to undefined function: {func}")
    def interpret(self,tree):
        if tree:
            for stmt in tree.body:
                self.visit(stmt)
        else:
            raise SyntaxError
if __name__=='__main__':
    import parser

    code = """
    x = 10
    y = 20
    print(x+y)
    """
    tree = parser.parse_code(code)
    inter = interpret()
    inter.interpret(tree)