from node import Node


class FileNode(Node):
    '''FileNode extends the Node class. It create a FileNode which represents
    a file's attributes within a filesystem such as the filepath and size. It
    also contains the following visual representation data: gradient colours
    and mouse hover colours.'''

    def __init__(self, path, size, tColour, bColour=None, hColour=None):
        '''Create a new FileNode with an empty list of children and attributes
        specified by the parameters.'''
        super(FileNode, self).__init__()
        self.path = path            # The location of the file
        self.size = size            # The size of the file (in KB)
        self.tColour = tColour      # The top colour of the gradient
        self.bColour = bColour      # The bottom colour of the gradient
        self.hColour = hColour      # The mouse hover colour

    def getPath(self):
        '''Return the path of the FileNode self.'''
        return self.path

    def getSize(self):
        '''Return the size of the FileNode self.'''
        return self.size

    def getTColour(self):
        '''Return the top colour of the FileNode self.'''
        return self.tColour

    def getBColour(self):
        '''Return the bottom colour of the FileNode self.'''
        return self.bColour

    def getHColour(self):
        '''Return the mouse hover colour of the FileNode self.'''
        return self.hColour
