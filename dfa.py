class Node:
    def __init__(self, links={}, is_accepting=False):
        self.correct = []
        self.is_accepting = is_accepting
        self.edges = {}
        if links:
            self._parse_links(links)

    def _parse_links(self, links):
        for link in links:
            if links[link] == '~':
                self.edges[link] = self
            else:
                self.edges[link] = links[link]

    def accepts(self, string):
        if string in self.correct:
            return True
        else:
            return False

    def add_edge(self, label, node):
        self.edges[label] = node
        self.correct.append(label)

    def parse(self, string):
        if len(string) == 0:
            if self.is_accepting:
                return True
            else:
                return False
        for edge in self.edges:
            if edge == string[0]:
                if self.edges[edge].parse(string[1:]):
                    return True
        return False

d = Node({'a': '~', 'b': '~'})
c = Node({'a': d, 'b': d}, True)
b = Node({'b': c, 'a': d})
a = Node({'a': '~', 'b': b})

while True:
    print(a.parse(input('> ')))
