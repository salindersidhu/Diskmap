import sys
from PyQt4 import QtGui, QtCore
from guiwindow import GUIWindow
from tileframe import TileFrame


class DiskmapApp(QtGui.QApplication):
    ''''''

    def __init__(self, args):
        '''Create a new DiskmapApp with arguments specified by arg.'''
        super(DiskmapApp, self).__init__(args)
        # Application variables
        self.__FPS = 60
        self.__defaultStatus = "Please open a directory..."
        # Configure the GUIWindow
        self.__window = GUIWindow('Diskap - Disk Visualization Utility', 640,
                                  360, 'Resources/icon.png')
        # Configure the Tileframe
        self.__tileframe = TileFrame(self.__window)
        self.__window.setCentralWidget(self.__tileframe)
        # Setup remaining GUI elements
        self.__setupMenu()
        self.__setupMenuItems()
        self.__window.setStatusBar(self.__defaultStatus)
        self.__window.show()

    def __setupMenu(self):
        '''Add all the menus used in the application to GUIWindow.'''
        self.__window.addMenu('File')
        self.__window.addMenu('Options')
        self.__window.addMenu('Help')

    def __setupMenuItems(self):
        '''Add all the menu items, along with their event functions, used in
        the application to GUIWindow.'''
        # Setup File menu items
        self.__window.addMenuItem('File', 'Load Directory', None)
        self.__window.addMenuSeperator('File')
        self.__window.addMenuItem('File', 'Quit', self.__window.close)
        # Setup Option menu items
        self.__window.addMenuItem('Options', 'Screenshot', None)
        self.__window.addMenuItem('Options', 'Clear Map', None)
        # Setup Help menu items
        self.__window.addMenuItem('Help', 'About', self.__eventAbout)

    def __eventAbout(self):
        '''Display an information dialog about the program languages and tools
        used to create this application and the name of the developer.'''
        message = 'Disk Space Visualization Utility\nPython 3 PyQ 4\n\n' + \
            'Developed by Salinder Sidhu'
        # Render the message box
        QtGui.QMessageBox.information(self.__window, 'About', message,
                                      buttons=QtGui.QMessageBox.Ok)

if __name__ == '__main__':
    # Pass command line arguments into application
    myApp = DiskmapApp(sys.argv)
    sys.exit(myApp.exec_())
