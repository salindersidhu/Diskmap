from treemap import Treemap
from filenode import FileNode
from PyQt5 import QtGui, QtCore, QtWidgets


class TileFrame(QtWidgets.QFrame):
    '''TileFrame extends the QtGui.QFrame class. It is used to render the
    Treemap data structure, each node in the Treemap is rendered as
    rectanglular tiles with a fixed colour or gradient colours. Hovered tiles
    are rendered using a lighter fixed colour.'''

    def __init__(self, parentWindow):
        '''Create a new TileFrame.'''
        super(TileFrame, self).__init__(parentWindow)
        # TileFrame variables
        self.__treemap = None
        self.__isBorders = True
        self.__isGradient = False
        self.__rectNodes = []
        self.__selectedNode = None
        self.__borderCol = QtGui.QColor(0, 0, 0)
        self.__bgCol = QtGui.QColor(64, 64, 64)
        self.__txtCol = QtGui.QColor(38, 38, 38)
        self.__txtFont = QtGui.QFont('CopperBlack', 60, QtGui.QFont.Bold)
        self.__txt = "Visualizer"
        # Set strong policy for focusing keyboard events to Tileframe
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setMouseTracking(True)

    def __buildTiles(self, painter, node, size, location):
        '''Render the Treemap Node by Node. Render the DirNode as borders
        with the border colour and render the FileNodes as rectangular tiles.
        Render the FileNodes with gradient colours iff gradients are enabled
        and render with a fixed colour otherwise.'''
        borderRect = QtCore.QRect(location[0], location[1], size[0], size[1])
        # If rendering borders is enabled
        if self.__isBorders:
            # Shift the dimensions of the rectangle
            location[0] += 1
            location[1] += 1
            size[0] -= 2
            size[1] -= 2
        totalSize = max(node.getSize(), 1)  # Prevent ZeroDivisionError
        for item in node.getChildren():
            percent = item.getSize() / totalSize
            itemArea = (size[0] * size[1]) * percent
            # Calculate dimensions of the rectangle
            if size[1] > size[0]:
                width = size[0]
                height = itemArea / width
                # Draw rectangle
                if self.__isGradient:
                    self.__drawGradientRectangle(painter,
                                                 item,
                                                 [width, height],
                                                 location)
                else:
                    self.__drawRectangle(painter,
                                         item,
                                         [width, height],
                                         location)
                location[1] += height
            else:
                height = size[1]
                width = itemArea / height
                # Draw rectangle
                if self.__isGradient:
                    self.__drawGradientRectangle(painter,
                                                 item,
                                                 [width, height],
                                                 location)
                else:
                    self.__drawRectangle(painter,
                                         item,
                                         [width, height],
                                         location)
                location[0] += width
        # If rendering borders is enabled
        if self.__isBorders:
            # Draw the border around the rectangle
            painter.setBrush(QtCore.Qt.NoBrush)
            painter.setPen(self.__borderCol)
            painter.drawRect(borderRect)

    def __drawGradientRectangle(self, painter, node, size, location):
        '''Render a Node of type FileNode as a rectangular gradient
        proportional to the size of the file represented by FileNode. Render
        the FileNode with its hover colour iff it's mouse hovered, otherwise
        render the FileNode with the top and bottom gradient colours.'''
        if isinstance(node, FileNode):
            # Obtain the components of a rectangle
            x1 = location[0]
            y1 = location[1]
            x2 = size[0] + 1
            y2 = size[1] + 1
            # Store a map of the file nodes and their display rectangle tiles
            rect = QtCore.QRect(x1, y1, x2, y2)
            self.__rectNodes.append((rect, node))
            # Set the top and bottom gradient colours to the Node's hover
            # colours if the file's node is selected, otherwise obtain the top
            # and bottom gradient colours from node
            if self.__selectedNode == node:
                topCol = botCol = node.getHColour()
            else:
                topCol = node.getTColour()
                botCol = node.getBColour()
            # Obtain the components of rectanglular gradient
            gradX1 = location[0]
            gradY1 = location[1] + size[0]
            gradX2 = (location[0] + size[0]) - size[0]
            gradY2 = location[1] + size[1]
            # Render the tile as a gradient
            grad = QtGui.QLinearGradient(gradX1, gradY1, gradX2, gradY2)
            grad.setColorAt(0.0, QtGui.QColor(topCol[0], topCol[1], topCol[2]))
            grad.setColorAt(1.0, QtGui.QColor(botCol[0], botCol[1], botCol[2]))
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(QtGui.QBrush(grad))
            painter.drawRect(rect)
        # Recursively render the next tile in the Treemap
        self.__buildTiles(painter, node, size, location[:])

    def __drawRectangle(self, painter, node, size, location):
        '''Render a Node of type FileNode as a rectangular tile proportional to
        the size of file represented by the FileNode. Render the FileNode with
        its hover colour iff it's mouse hovered, otherwise render the FileNode
        with the top gradient colour.'''
        if isinstance(node, FileNode):
            # Obtain the components of a rectangle
            x1 = location[0]
            x2 = location[1]
            y1 = size[0] + 1
            y2 = size[1] + 1
            # Store a map of the file nodes and their display rectangle tiles
            rect = QtCore.QRect(x1, x2, y1, y2)
            self.__rectNodes.append((rect, node))
            # Obtain the file's hover colour if it is selected otherwise obtain
            # it's regular top gradient colour
            if self.__selectedNode == node:
                col = node.getHColour()
            else:
                col = node.getTColour()
            painter.fillRect(rect, QtGui.QColor(col[0], col[1], col[2]))
        # Recursively render the next tile in the Treemap
        self.__buildTiles(painter, node, size, location[:])

    def getHoveredNodePath(self, mousePos):
        '''Return the path of a file, as a string, from a Node that is mouse
        hovered.'''
        mX = mousePos.x()
        mY = mousePos.y() - self.y()  # Account for location of widget
        # Iterate through all the rectangles
        for item in self.__rectNodes:
            rX = item[0].x()
            rY = item[0].y()
            rW = item[0].width()
            rH = item[0].height()
            if (mX >= rX and mX <= (rX + rW)) and (mY >= rY and mY <= (rY +
                                                                       rH)):
                # Store the hovered node as the selected node and update
                self.__selectedNode = item[1]
                self.update()
                # Return the path of the file represented by the FileNode
                return item[1].getPath()

    def isMapped(self):
        '''Return true if Treemap exists, False otherwise.'''
        return self.__treemap

    def toggleBorders(self):
        '''Enable drawing of borders if drawing borders was dissabled and
        dissable drawing of borders if it was previously enabled.'''
        if self.isMapped():
            # Toggle borders and update the tile rendering
            self.__isBorders = not self.__isBorders
            self.update()

    def toggleGradient(self):
        '''Enable drawing of gradients if drawing gradients was dissabled and
        dissable drawing of gradients if they were previously enabled.'''
        if self.isMapped():
            # Toggle gradient and update the tile rendering
            self.__isGradient = not self.__isGradient
            self.update()

    def screenshot(self, filename):
        '''Obtain a pixel map of the current window and save it as a .PNG
        file with the name specified by filename.'''
        QtGui.QPixmap.grabWindow(self.winId()).save(filename, 'png')

    def clearMap(self):
        '''Reset the visual map variables and clear the Treemap.'''
        # Reset the toggle variables
        self.__isBorders = True
        self.__isGradient = False
        # Clear the node rectangles
        self.__rectNodes = {}
        # Clear the Treemap
        self.__treemap = None

    def updateMap(self, directory, resetMap=True):
        '''Rebuild the Treemap at the specified directory and clear the map
        iff resetMap is True.'''
        # Clear the map if reset is True
        if resetMap:
            self.clearMap()
        # Build a new Treemap
        self.__treemap = Treemap()
        self.__treemap.build(directory)

    def paintEvent(self, event):
        '''Handle and process all of the drawing for the Treemap. Render the
        Treemap if it's loaded, otherwise render a grey background with darker
        grey text centered on the window.'''
        self.__rectNodes = []  # Clear all the rectangle node list
        painter = QtGui.QPainter(self)  # Used to draw on the frame
        # Clear all drawings on the TileFrame
        painter.eraseRect(0, 0, self.width(), self.height())
        if self.isMapped():
            # Set the initial conditions and render the Treemap
            size = [self.width(), self.height()]
            location = [0, 0]
            self.__buildTiles(painter,
                              self.__treemap.getRoot(),
                              size,
                              location)
        else:
            # Draw the default background
            painter.fillRect(0, 0, self.width(), self.height(), self.__bgCol)
            # Draw the default text
            painter.setPen(self.__txtCol)
            painter.setFont(self.__txtFont)
            painter.drawText(event.rect(), QtCore.Qt.AlignCenter, self.__txt)
