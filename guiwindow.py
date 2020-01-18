from PyQt5 import QtGui, QtWidgets


class GUIWindow(QtWidgets.QMainWindow):
    '''GUIWindow the extends the QtWidgets.QMainWindow class. It creates a
    basic window that contains a MenuBar and a StatusBar, both of which are
    modifiable. The window includes advanced functionality such as appearing in
    the center of the screen binding of key and mouse events.'''

    def __init__(self, winTitle, winWidth, winHeight, winIcon):
        '''Create a new GUIWindow with a specific window title, width, height
        and window icon.'''
        super(GUIWindow, self).__init__()
        # Exceptions
        self.__menuExistsException = Exception(
            'The specified menu already exists!')
        self.__menuNotFoundException = Exception(
            'The specified menu was not found!')
        # GUIWindow variables
        self.__menubar = self.menuBar()         # Menu Bar
        self.__menuDict = {}                    # Map of Menus for Menubar
        self.__statusLabel = QtWidgets.QLabel()  # New Status label
        self.__keyInputDict = {}                # Map of key events
        self.__checkableActions = {}            # Map of checkable QActions
        self.__mouseMoveEvents = []             # List of mouse move events
        self.__mouseClickEvents = []            # List of mouse click events
        self.__mouseReleaseEvents = []          # List of mouse release events
        # Configure the window's properties
        self.setGeometry(0, 0, winWidth, winHeight)
        self.setMinimumSize(winWidth / 2, winHeight / 2)
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

    def mouseMoveEvent(self, event):
        '''Handle and process all mouse movement events.'''
        for func in self.__mouseMoveEvents:
            func(event)

    def mousePressEvent(self, event):
        '''Handle and process all mouse click events.'''
        for func in self.__mouseClickEvents:
            func(event)

    def mouseReleaseEvent(self, event):
        '''Handle and process all mouse release events.'''
        for func in self.__mouseReleaseEvents:
            func(event)

    def __centerOnScreen(self):
        '''Move the position of the window so that it is positioned perfectly
        in the center of the screen.'''
        res = QtWidgets.QDesktopWidget().screenGeometry()
        move_width = (res.width() / 2) - (self.frameSize().width() / 2)
        move_height = (res.height() / 2) - (self.frameSize().height() / 2)
        self.move(move_width, move_height)

    def updateMouseEvents(self, moveEvents, clickEvents, releaseEvents):
        '''Update the mouse event lists for movement, clicking and releasing as
        specified by the events in the lists from the parameters.'''
        self.__mouseMoveEvents = moveEvents
        self.__mouseClickEvents = clickEvents
        self.__mouseReleaseEvents = releaseEvents

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

    def addMenuItem(self, menuTitle, menuItemName, evtFunction=None):
        '''Add a new menu item to an existing menu with a title specified by
        menuTitle. Connect an event function to the menu item if the specified
        value is not None.'''
        # Check if menuTitle exists
        if menuTitle in self.__menuDict:
            # Create the menu item
            menuItem = QtWidgets.QAction('&' + menuItemName, self)
            if evtFunction:
                menuItem.triggered.connect(lambda: evtFunction())
            # Add the menu items to the menu item dictionary
            self.__menuDict[menuTitle].addAction(menuItem)
        else:
            raise self.__menuNotFoundExceptionException

    def addCheckableMenuItem(self, menuTitle, menuItemName, isChecked,
                             evtFunction=None):
        '''Add a new checkable menu item to an existing menu with a title
        specified by menuTitle. Connect an event function to the checkable menu
        item if the specified value is not None. The checkable menu item is
        checked if the value of isChecked is True, unchecked if False.'''
        # Check if menuTitle exists
        if menuTitle in self.__menuDict:
            # Create the checkable menu item and set the check flag
            menuItem = QtWidgets.QAction(
                '&' + menuItemName, self, checkable=True)
            menuItem.setChecked(isChecked)
            # Store menu action item
            self.__checkableActions[menuItemName] = menuItem
            if evtFunction:
                menuItem.triggered.connect(lambda: evtFunction())
            # Add the menu items to the menu item dictionary
            self.__menuDict[menuTitle].addAction(menuItem)
        else:
            raise self.__menuNotFoundExceptionException

    def setCheckedMenuItem(self, menuItem, isChecked):
        '''Set a checkable menu menu item, specified by menuItem to checked
        if isChecked is True, unchecked if False.'''
        # Check if checkable menu item exists
        if menuItem in self.__checkableActions:
            # Set the checked menu item to the value of isChecked
            self.__checkableActions[menuItem].setChecked(isChecked)
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
