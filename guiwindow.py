from PyQt4 import QtGui


class GUIWindow(QtGui.QMainWindow):
    '''GUIWindow the extends the QtGui.QMainWindow class. It creates a basic
    window that contains a MenuBar and a StatusBar, both of which are
    modifiable. The window includes advanced functionality such as appearing in
    the center of the screen binding of key press and release events.'''

    def __init__(self, winTitle, winWidth, winHeight, winIcon):
        '''Create a new GUIWindow with a specific window title, width, height
        and window icon.'''
        super(GUIWindow, self).__init__()
        # Exceptions
        self.__menuExistsException = Exception('The specified menu already' +
                                               ' exists!')
        self.__menuNotFoundException = Exception('The specified menu was ' +
                                                 'not found!')
        # GUIWindow variables
        self.__menubar = self.menuBar()         # Define a Menu Bar
        self.__menuDict = {}                    # Define a map of Menus
        self.__statusLabel = QtGui.QLabel()     # Define a new status label
        self.__keyInputDict = {}                # Define a map of key events
        # Configure the window's properties
        self.setGeometry(0, 0, winWidth, winHeight)
        self.setFixedSize(winWidth, winHeight)
        self.setWindowTitle(winTitle)
        self.setWindowIcon(QtGui.QIcon(winIcon))
        # Bind the QLabel to the Status Bar
        self.statusBar().addWidget(self.__statusLabel, 1)
        # Set the window to appear in the center of the screen
        self.__centerOnScreen()
        # Configure the remaining GUI elements for the window

    def keyPressEvent(self, event):
        '''Handle and process all key press events.'''
        eventKey = event.key()
        if eventKey in self.__keyInputDict:
            self.__keyInputDict[eventKey][0]()

    def keyReleaseEvent(self, event):
        '''Handle and process all key release events.'''
        eventKey = event.key()
        if eventKey in self.__keyInputDict:
            self.__keyInputDict[eventKey][1]()

    def __centerOnScreen(self):
        '''Move the position of the window so that it is positioned perfectly
        in the center of the screen.'''
        res = QtGui.QDesktopWidget().screenGeometry()
        move_width = (res.width() / 2) - (self.frameSize().width() / 2)
        move_height = (res.height() / 2) - (self.frameSize().height() / 2)
        self.move(move_width, move_height)

    def updateKeyBindings(self, keyBindings):
        '''Change the current value of the keys and their events for keypress
        and keyrelease to the ones specified by keyBindings.'''
        self.__keyInputDict = keyBindings.copy()

    def setStatusBar(self, statusText):
        '''Change the current value of the StatusBar's text.'''
        self.__statusLabel.setText(statusText)

    def addMenu(self, menuTitle):
        '''Add a new menu with a title specified by menuTitle to the window's
        MenuBar.'''
        # Check if menuTitle does not exist (prevent duplicates)
        if menuTitle in self.__menuDict:
            raise self.__menuExistsException
        else:
            self.__menuDict[menuTitle] = \
                self.__menubar.addMenu('&' + menuTitle)

    def addMenuItem(self, menuTitle, menuItem, evtFunction=None):
        '''Add a new menu item to an existing menu with a title specified by
        menuTitle. Connect an event function to the menu item if the specified
        value is not None.'''
        # Check if menuTitle exists
        if menuTitle in self.__menuDict:
            # Create the menu item
            menuItem = QtGui.QAction('&' + menuItem, self)
            if evtFunction:
                menuItem.triggered.connect(lambda: evtFunction())
            # Add the menu items to the menu item dictionary
            self.__menuDict[menuTitle].addAction(menuItem)
        else:
            raise self.__menuNotFoundExceptionException

    def addMenuSeperator(self, menuTitle):
        '''Add a seperator item to an existing menu with a title specified by
        menuTitle.'''
        # Check if menuTitle exists
        if menuTitle in self.__menuDict:
            self.__menuDict[menuTitle].addSeparator()
        else:
            raise self.__menuNotFoundExceptionException
