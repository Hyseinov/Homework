class Node:

    def __init__(self, name, perent):
        self.name = name
        self.parent = perent



nobe1 = Node("Joobasar", None)
nobe2 = Node("Tenesh", nobe1)
nobe3 = Node("Kary", nobe2)
nobe4 = Node("tokol", nobe3)
nobe5 = Node("Baytugol", nobe4)
nobe6 = Node("Apytai", nobe5)
nobe7 = Node("Ajibek", nobe6)

n = nobe7
while n.parent is not None:
    print(n.name)
    n = n.parent

