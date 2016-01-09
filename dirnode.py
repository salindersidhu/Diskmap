from node import Node


class DirNode(Node):
    '''DirNode extends the Node class. It creates a DirNode which represents
    a directory's attributes within a filesystem such as directory path and
    size.'''

    def __init__(self, path, size):
        '''Create a new DirNode with an empty list of children and attributes
        specified by the parameters.'''
        super(DirNode, self).__init__()
        self.path = path            # The location of the file
        self.size = size            # The size of the file (in KB)

    def getPath(self):
        '''Return the path of the DirNode self.'''
        return self.path

    def getSize(self):
        '''Return the size of the DirNode self.'''
        return self.size

    def setSize(self, size):
        '''Set the size of the DirNode self.'''
        self.size = size
