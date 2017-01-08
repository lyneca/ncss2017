import re

class Node:
    def __init__(self, left, right):
        self.right = right
        self.left = left

    def evaluate(self):
        raise NotImplementedError()

class AddNode(Node):
    def evaluate(self):
        return self.left.evaluate() + self.right.evaluate()

    def __str__(self):
        return '{%s + %s}' % (self.left, self.right)

class SubNode(Node):
    def evaluate(self):
        return self.left.evaluate() - self.right.evaluate()

    def __str__(self):
        return '{%s - %s}' % (self.left, self.right)

class MultNode(Node):
    def evaluate(self):
        return self.left.evaluate() * self.right.evaluate()

    def __str__(self):
        return '{%s * %s}' % (self.left, self.right)

class DivideNode(Node):
    def evaluate(self):
        return self.left.evaluate() / self.right.evaluate()

    def __str__(self):
        return '{%s / %s}' % (self.left, self.right)

class LiteralNode(Node):
    def __init__(self, value):
        super().__init__(None, None)
        self.value = value

    def evaluate(self):
        return self.value

    def __str__(self):
        return str(self.value)

class Parser:
    NUMBER = re.compile('-?[0-9]+')
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



    def _parse_e1(self):
        char = self.peek()
        node = self._parse_e2()
        if self.peek() == '+':
            self.next()
            node2 = self._parse_e1()
            node = AddNode(node, node2)
        return node

    def _parse_e2(self):
        char = self.peek()
        node = self._parse_e3()
        if self.peek() == '*':
            self.next()
            node2 = self._parse_e2()
            node = MultNode(node, node2)
        return node

    def _parse_e3(self):
        char = self.peek()
        node = None
        if self.NUMBER.match(char):
            node = LiteralNode(int(char))
            self.next()
        elif char == '(':
            self.next()
            node = self._parse_e1()
            if not self.peek() == ')':
                raise Exception("Unbalanced Parantheses")
            self.next()
        return node

    def evaluate(self):
        return self.root_node.evaluate()

    def parse(self):
        self.root_node = self._parse_e1()
        return self.root_node

    def at_end(self):
        return not len(self._tokens) > 0

    def next(self):
        self._tokens = self._tokens[1:]

    def peek(self):
        return None if self.at_end() else self._tokens[0]

p = Parser('5*4*2')
print(p.parse())
print(p.evaluate())

# <e1> ::= <e2> ( "+" <e1> )?
# <e2> ::= <e3> ( "*" <e2> )?
# <e3> ::= "-"? ( "0" | "1" | ... | "9" )+
# <e3> ::= "(" <e1> ")"
