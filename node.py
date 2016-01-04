class Node(object):
    '''A Node in a tree with an arbitrary number of children (an arbitrary
    branching factor).'''

    def __init__(self, obj):
        '''(Node, object) -> NoneType
        Create a new node with a key obj and an empty list of children.'''
        self.key = obj
        self.children = []

    def add_child(self, node):
        '''(Node, Node) -> NoneType
        Append node as a child to the parent self.'''
        self.children.append(node)
