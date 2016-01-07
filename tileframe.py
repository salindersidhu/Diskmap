from PyQt4 import QtGui, QtCore
from random import uniform
from treemap import Treemap


class TileFrame(QtGui.QFrame):
    ''''''

    def __init__(self, parentWindow):
        ''''''
        super(TileFrame, self).__init__(parentWindow)
        # TileFrame variables
        self.__treemap = None
        self.__fillCol = QtGui.QColor(0, 0, 0)
        self.__bgCol = QtGui.QColor(64, 64, 64)
        self.__txtCol = QtGui.QColor(38, 38, 38)
        self.__txtFont = QtGui.QFont('CopperBlack', 60, QtGui.QFont.Bold)
        self.__txt = "Visualizer"
        # Set strong policy for focusing keyboard events to Tileframe
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def __randomColourHSV():
        '''Return a random colour using an aesthetically pleasing colour
        palette. The colour is in the form of a 3-tupple with HSV values.'''
        goldenRatioConjugate = 0.618033988749895
        h = uniform(0, 1)
        h += goldenRatioConjugate
        h %= 1
        return (h, 0.5, 0.95)

    def __buildTiles(self, painter, node, size, location):
        ''''''
        pass

    def screenshot(self, filename):
        ''''''
        QtGui.QPixmap.grabWindow(self.winId()).save(filename, 'png')

    def clearMap(self):
        ''''''
        self.__treemap = None

    def updateMap(self, directory):
        ''''''
        self.__treemap = Treemap()
        self.__treemap.build(directory)

    def paintEvent(self, event):
        ''''''
        painter = QtGui.QPainter(self)  # Used to draw on the frame
        # Clear all drawings on the GridFrame
        painter.eraseRect(0, 0, self.width(), self.height())
        if self.__treemap:
            # Set the initial conditions and render the Treemap
            size = [self.width(), self.height()]
            location = [0, 0]
            self.__buildTiles(painter, self.__treemap, size, location)
        else:
            # Draw the default background
            painter.fillRect(0, 0, self.width(), self.height(), self.__bgCol)
            # Draw the default text
            painter.setPen(self.__txtCol)
            painter.setFont(self.__txtFont)
            painter.drawText(event.rect(), QtCore.Qt.AlignCenter, self.__txt)
