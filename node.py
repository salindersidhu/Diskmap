class Node:
    '''A Node in a tree with an arbitrary number of children (an arbitrary
    branching factor).'''

    def __init__(self):
        '''Create a new node with an empty list of children.'''
        self.children = []

    def add(self, node):
        '''Append node as a child to the parent self.'''
        self.children.append(node)

    def getChildren(self):
        '''Return the list of children of the parent self.'''
        return self.children
