from node import Node
from random import randint
from colorsys import hsv_to_rgb


class FileNode(Node):
    '''FileNode extends the Node class. It create a FileNode which represents
    a file's attributes within a filesystem such as the filepath and size. It
    also contains the following visual representation data: gradient colours
    and mouse hover colours.'''

    def __init__(self, path, size):
        '''Create a new FileNode with an empty list of children and attributes
        specified by the parameters.'''
        super(FileNode, self).__init__()
        self.path = path            # The location of the file
        self.size = size            # The size of the file (in KB)
        self.tColour = None         # The top colour of the gradient
        self.bColour = None         # The bottom colour of the gradient
        self.hColour = None         # The mouse hover colour
        # Set the colours for the FileNode
        self.__setRandomColours()

    def __setRandomColours(self):
        '''Set the gradient and mouse hover colours using an aesthetically
        pleasing HSV colour palette. The same hue value is used for all colours
        with varying degrees of saturation to generate different shades.'''
        hue = randint(0, 360) / 360
        self.tColour = tuple(i * 255 for i in hsv_to_rgb(hue, 0.6, 0.95))
        self.bColour = tuple(i * 255 for i in hsv_to_rgb(hue, 1, 0.95))
        self.hColour = tuple(i * 255 for i in hsv_to_rgb(hue, 0.3, 0.95))

    def __getRandomColour(self, sat, val):
        '''Return a random colour in the form of an RGB 3-tupple based on a
        random hue and specified saturation and value parameters.'''
        hue = random.randint(0, 360) / 360
        sat /= 100
        val /= 100
        return tuple(i * 255 for i in colorsys.hsv_to_rgb(hue, sat, val))

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
