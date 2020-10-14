class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self):
        return f'Node: {self.value}'

    def add_child(self, node):
        self.children.append(node)

    def __iter__(self):
        return iter(self.children)


root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child2)
root.add_child(child1)

for child in root:
    print(child1.value)