chain = []

debug_links = False

class NoEntryNodeException(Exception):
    pass

class NodeNotFoundException(Exception):
    pass

def debug(s):
    if debug_links:
        print(s)

class NFA:
    def __init__(self):
        self.entry_node = None
        self.nodes = {}

    def add_node(self, name, is_accepting=False, is_entry=False):
        self.nodes[name] = NFANode(name, is_accepting)
        if is_entry:
            self.entry_node = self.nodes[name]
        return self.nodes[name]

    def add_link(self, start, end, label=''):
        if start in self.nodes:
            node = self.nodes[start]
        else:
            raise NodeNotFoundException("Node '%s' not found in NFA" % start)
        if end in self.nodes:
            other = self.nodes[end]
        else:
            raise NodeNotFoundException("Node '%s' not found in NFA" % end)
        node.add_edge(other, label)

    def set_entry_node(self, name):
        if name in self.nodes:
            self.entry_node = self.nodes[name]
        else:
            raise NodeNotFoundException("Node '%s' not found in NFA" % name)

    def parse(self, string):
        if self.entry_node is None:
            raise NoEntryNodeException('Set an entry point for the NFA')
        return self.entry_node.parse(string)


class NFANode:
    def __init__(self, name, is_accepting=False):
        self.correct = []
        self.name = name
        self.is_accepting = is_accepting
        self.edges = {}
        self.epsilons = []

    def __repr__(self):
        return '<Node \'' + self.name + '\'>'

    def accepts(self, string):
        if string in self.correct:
            return True
        else:
            return False

    def add_edge(self, node, label=''):
        if not label:
            self.epsilons.append(node)
        else:
            if label in self.edges:
                try:
                    self.edges[label] = (self.edges[label], node)
                except TypeError:
                    self.edges[label] = (self.edges[label], node)
            else:
                self.edges[label] = (node,)
            self.correct.append(label)

    def parse(self, string):
        if len(string) == 0:
            if self.is_accepting:
                return True
            else:
                return False
        for edge in self.edges:
            if edge == string[0]:
                for node in self.edges[edge]:
                    debug('linking from ' + repr(self) + ' to ' + repr(self.edges[edge]) + ' along link labelled \'' + edge + '\'')
                    if node.parse(string[1:]):
                        return True
        for node in self.epsilons:
            debug('linking from ' + repr(self) + ' to ' + repr(node) + ' along epsilon link')
            chain.append(self.name)
            chain.append('-')
            if node.parse(string):
                return True
        debug('no links labelled \'%s\' from node %s' % (string[0], repr(self)))
        return False

nfa = NFA()

nfa.add_node('q0', True, True)
nfa.add_node('q1')
nfa.add_node('q2')
nfa.add_link('q0', 'q1', 'b')  # q0 -> q1 over b
nfa.add_link('q0', 'q2')       # q0 -> q2 over epsilon
nfa.add_link('q1', 'q1', 'a')  # q1 -> q1 over b
nfa.add_link('q1', 'q2', 'a')  # q1 -> q2 over a
nfa.add_link('q1', 'q2', 'b')  # q1 -> q2 over b
nfa.add_link('q2', 'q0', 'a')  # q2 -> q0 over a

if __name__ == '__main__':
    while True:
        print(nfa.parse(input('> ')))
        chain = []
