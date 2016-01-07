class Node(object):
    '''A Node in a tree with an arbitrary number of children (an arbitrary
    branching factor).'''

    def __init__(self, obj):
        '''Create a new node with a key obj and an empty list of children.'''
        self.key = obj
        self.children = []

    def add(self, node):
        '''Append node as a child to the parent self.'''
        self.children.append(node)
