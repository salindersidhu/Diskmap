from treemap import Treemap
from filenode import FileNode
from PyQt4 import QtGui, QtCore


class TileFrame(QtGui.QFrame):
    ''''''

    def __init__(self, parentWindow):
        ''''''
        super(TileFrame, self).__init__(parentWindow)
        # TileFrame variables
        self.__treemap = None
        self.__isBorders = True
        self.__isGradient = False
        self.__rectNodes = []
        self.__borderCol = QtGui.QColor(0, 0, 0)
        self.__bgCol = QtGui.QColor(64, 64, 64)
        self.__txtCol = QtGui.QColor(38, 38, 38)
        self.__txtFont = QtGui.QFont('CopperBlack', 60, QtGui.QFont.Bold)
        self.__txt = "Visualizer"
        # Set strong policy for focusing keyboard events to Tileframe
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setMouseTracking(True)

    def __buildTiles(self, painter, node, size, location):
        ''''''
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
                    self.__drawGradientRectangle(painter, item, [width,
                                                                 height],
                                                 location)
                else:
                    self.__drawRectangle(painter, item, [width, height],
                                         location)
                location[1] += height
            else:
                height = size[1]
                width = itemArea / height
                # Draw rectangle
                if self.__isGradient:
                    self.__drawGradientRectangle(painter, item, [width,
                                                                 height],
                                                 location)
                else:
                    self.__drawRectangle(painter, item, [width, height],
                                         location)
                location[0] += width
        # If rendering borders is enabled
        if self.__isBorders:
            # Draw the border around the rectangle
            painter.setBrush(QtCore.Qt.NoBrush)
            painter.setPen(self.__borderCol)
            painter.drawRect(borderRect)

    def __drawGradientRectangle(self, painter, node, size, location):
        ''''''
        if isinstance(node, FileNode):
            # Store a map of the file nodes and their display rectangle tiles
            rect = QtCore.QRect(location[0], location[1], size[0], size[1])
            self.__rectNodes.append((rect, node))
            # Obtain the top and bottom gradient colours from node
            topColour = node.getTColour()
            botColour = node.getBColour()
            colourSlope = [0, 0, 0]
            rawColour = [0, 0, 0]
            segColour = [0, 0, 0]
            # Obtain the components of a rectangle
            x1 = location[0]
            y1 = location[1]
            x2 = location[0] + size[0]
            y2 = location[1] + size[1]
            deltaY = max(y2 - y1, 1)  # Prevent ZeroDivisionError
            # Calculate the rate of change of each colour component
            colourSlope[0] = round(botColour[0] - topColour[0]) / deltaY
            colourSlope[1] = round(botColour[1] - topColour[1]) / deltaY
            colourSlope[2] = round(botColour[2] - topColour[2]) / deltaY
            # Use linear interpolation to calculate the colour of each line
            for seg in range(int(y1), int(y2)):
                for i in range(3):
                    rawColour[i] = topColour[i] + (colourSlope[i] * (seg - y1))
                    # Adjust the colour if < 0 or > 255
                    segColour[i] = min(max(rawColour[i], 0), 255)
                # Render the line segment with the segment colour
                colour = QtGui.QColor(segColour[0], segColour[1], segColour[2])
                painter.setPen(QtGui.QPen(colour, 1, QtCore.Qt.SolidLine))
                painter.drawLine(x1, seg, x2, seg)
        # Recursively render the next level of tiles
        self.__buildTiles(painter, node, size, location[:])

    def __drawRectangle(self, painter, node, size, location):
        ''''''
        if isinstance(node, FileNode):
            # Store a map of the file nodes and their display rectangle tiles
            rect = QtCore.QRect(location[0], location[1], size[0], size[1])
            self.__rectNodes.append((rect, node))
            # Obtain the file's colour and render the tile
            rgb = node.getTColour()
            painter.fillRect(rect, QtGui.QColor(rgb[0], rgb[1], rgb[2]))
        # Recursively render the next level of tiles
        self.__buildTiles(painter, node, size, location[:])

    def getHoveredNodePath(self, mousePos):
        ''''''
        mX = mousePos.x()
        mY = mousePos.y()
        # Iterate through all the rectangles
        for item in self.__rectNodes:
            rX = item[0].x()
            rY = item[0].y()
            rW = item[0].width()
            rH = item[0].height()
            if (mX >= rX and mX <= (rX + rW)) and (mY >= rY and mY <= (rY +
                                                                       rH)):
                return item[1].getPath()

    def isMapped(self):
        ''''''
        return self.__treemap

    def toggleBorders(self):
        ''''''
        if self.isMapped():
            # Toggle borders and update the tile rendering
            self.__isBorders = not self.__isBorders
            self.update()

    def toggleGradient(self):
        ''''''
        if self.isMapped():
            # Toggle gradient and update the tile rendering
            self.__isGradient = not self.__isGradient
            self.update()

    def screenshot(self, filename):
        ''''''
        QtGui.QPixmap.grabWindow(self.winId()).save(filename, 'png')

    def clearMap(self):
        ''''''
        # Reset the toggle variables
        self.__isBorders = True
        self.__isGradient = False
        # Clear the node rectangles
        self.__rectNodes = {}
        # Clear the Treemap
        self.__treemap = None

    def updateMap(self, directory, resetMap=True):
        ''''''
        # Clear the map if reset is True
        if resetMap:
            self.clearMap()
        # Build a new Treemap
        self.__treemap = Treemap()
        self.__treemap.build(directory)

    def paintEvent(self, event):
        ''''''
        self.__rectNodes = []  # Clear all the rectangle node list
        painter = QtGui.QPainter(self)  # Used to draw on the frame
        # Clear all drawings on the GridFrame
        painter.eraseRect(0, 0, self.width(), self.height())
        if self.isMapped():
            # Set the initial conditions and render the Treemap
            size = [self.width(), self.height()]
            location = [0, 0]
            self.__buildTiles(painter, self.__treemap.getRoot(), size,
                              location)
        else:
            # Draw the default background
            painter.fillRect(0, 0, self.width(), self.height(), self.__bgCol)
            # Draw the default text
            painter.setPen(self.__txtCol)
            painter.setFont(self.__txtFont)
            painter.drawText(event.rect(), QtCore.Qt.AlignCenter, self.__txt)
