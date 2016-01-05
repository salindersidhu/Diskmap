import sys
from PyQt4 import QtGui, QtCore
from guiwindow import GUIWindow


class DiskmapApp(QtGui.QApplication):
    ''''''

    def __init__(self, args):
        '''Create a new DiskmapApp with arguments specified by arg.'''
        super(DiskmapApp, self).__init__(args)
        # Application variables
        self.__FPS = 60
        self.__defaultStatus = "Please open a directory..."
        # Configure the GUIWindow
        self.__window = GUIWindow('Diskmap', 640, 360, 'Resources/icon.png')
        # Setup remaining GUI elements
        self.__setupMenu()
        self.__window.setStatusBar(self.__defaultStatus)
        self.__window.show()

    def __setupMenu(self):
        '''Add all the menus used in the application to GUIWindow.'''
        self.__window.addMenu('File')
        self.__window.addMenu('Help')

if __name__ == '__main__':
    # Pass command line arguments into application
    myApp = DiskmapApp(sys.argv)
    sys.exit(myApp.exec_())
