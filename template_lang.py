import re

class InvalidSyntaxError(Exception):
    pass

class Node:
    def __init__(self):
        pass

    def evaluate(self):
        raise NotImplementedError()

class FunctionNode(Node):
    def __init__(self):
        pass

    def evaluate(self):
        raise NotImplementedError()

class IfNode(FunctionNode):
    def __init__(self, conditional, expression, elifs=[], else_clause=''):
        self.conditional = conditional
        self.expression = expression
        self.elifs = elifs
        self.else_clause = else_clause

    def evaluate(self):
        if self.conditional.evaluate():
            return self.expression.evaluate()
        else:
            flag = False
            for e in self.elifs:
                if e.evaluate() == True:
                    flag = True
                    return e.evaluate()
            if not flag:
                print('else')
                if self.else_clause:
                    return self.else_clause.evaluate()

class ElifNode(Node):
    def __init__(self, conditional, expression):
        self.conditional = conditional
        self.expression = expression
    def evaluate(self):
        if self.conditional.evaluate():
            self.expression.evaluate()

class ExpressionNode(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return eval(self.value)

class Parser:
    def __init__(self, tokens):
        self.root_node = None
        self.nodes = []
        if isinstance(tokens, list):
            self._tokens = tokens
        elif isinstance(tokens, str):
            self._tokens = list(re.sub(r'\s', '', tokens))
        else:
            try:
                self._tokens = list(tokens)
            except TypeError:
                raise TypeError('provide an iterable to Parser class')
        self._len = len(self._tokens)

    def _parse_command(self):
        if not self.peek() == '{%':
            raise InvalidSyntaxError('not a command')
        self.next()
        if self.peek() == 'if':
            self.next()
            node = self._parse_if()
        elif self.peek() == 'for':
            pass
        else:
            raise InvalidSyntaxError('missing command inside braces')
        return node

    def _parse_if(self):
        conditional_node = self._parse_expression()
        if not self.peek() == 'then':
            raise InvalidSyntaxError('\'if\' clause must be followed by \'then\'')
        self.next()
        expression_node = self._parse_expression()
        elif_nodes = []
        while self.peek() == 'elif':
            self.next()
            elif_nodes.append(self._parse_elif())
        else_node = None
        if self.peek() == 'else':
            self.next()
            else_node = self._parse_expression()
        node = IfNode(conditional_node, expression_node, elif_nodes, else_node)
        return node

    def _parse_elif(self):
        conditional = self._parse_expression()
        if not self.peek() == 'then':
            raise InvalidSyntaxError('\'elif\' clause must be followed by a \'then\'')
        self.next()
        expression = self._parse_expression()
        node = ElifNode(conditional, expression)
        return node

    def _parse_expression(self):
        node = ExpressionNode(self.peek())
        self.next()
        return node

    def evaluate(self):
        return self.root_node.evaluate()

    def parse(self):
        self.root_node = self._parse_command()
        return self.root_node

    def at_end(self):
        return not len(self._tokens) > 0

    def next(self):
        self._tokens = self._tokens[1:]

    def peek(self):
        return None if self.at_end() else self._tokens[0]

sample = [
    '{%',
    'if',
    'input(\'> \') == \'y\'',
    'then',
    'print(5 + 8)',
    'elif',
    'input(\'> \') == \'n\'',
    'then',
    'print(\'boop\')',
    'else',
    'print(\'hi\')',
    '%}'
]

if_str = '{% if input(\'> \') == \'y\' then print(5 + 8) elif input(\'> \') == \'n\' then print(\'boop\') else print(\'hi\') %}'
for_str = '{% for i in range(10) do %}'

# regex = r'{% (if (.+) then (.+) ?( elif (.+))* ?( else (.+))|for (\w+) in (.+) do (.+)) %}'

p = Parser(sample)
print(p.parse())
print(p.evaluate())

# <function> : {% <command> %}
# <command> : <if>|<for>
# <if> : if <expr> then <expr> (elif <expr> then <expr>)* (else <expr>)?
# <for> : for <name> in <expr> do <expr>(; <expr>)*
