import sys
import traceback
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
        self.__defaultStatus = "Please open a folder to map..."
        self.__debugLog = 'debugLog.txt'
        # Configure the GUIWindow
        self.__window = GUIWindow('Diskap - Disk Visualization Utility', 640,
                                  360, 'Resources/icon.png')
        # Configure the Tileframe
        self.__tileframe = TileFrame(self.__window)
        self.__window.setCentralWidget(self.__tileframe)
        self.__window.setMouseTracking(True)
        # Setup remaining GUI elements
        self.__setupMenu()
        self.__setupMouseEvents()
        self.__setupMenuItems()
        self.__window.setStatusBar(self.__defaultStatus)
        self.__window.show()

    def __setupMenu(self):
        '''Add all the menus used in the application to GUIWindow.'''
        self.__window.addMenu('File')
        self.__window.addMenu('Options')
        self.__window.addMenu('Settings')
        self.__window.addMenu('Help')

    def __setupMouseEvents(self):
        ''''''
        mouseEvents = []
        mouseEvents.append(self.__eventUpdateStatus)
        self.__window.updateMouseEvents(mouseEvents)

    def __setupMenuItems(self):
        '''Add all the menu items, along with their event functions, used in
        the application to GUIWindow.'''
        # Setup File menu items
        self.__window.addMenuItem('File', 'Map Folder', self.__eventMapFolder)
        self.__window.addMenuSeperator('File')
        self.__window.addMenuItem('File', 'Quit', self.__window.close)
        # Setup Option menu items
        self.__window.addMenuItem('Options', 'Screenshot',
                                  self.__eventScreenshot)
        self.__window.addMenuItem('Options', 'Clear Map', self.__eventClearMap)
        # Setup Settings menu items
        self.__window.addMenuItem('Settings', 'Toggle Gradient',
                                  self.__eventToggleGradient)
        self.__window.addMenuItem('Settings', 'Toggle Borders',
                                  self.__eventToggleBorders)
        # Setup Help menu items
        self.__window.addMenuItem('Help', 'About', self.__eventAbout)

    def __eventUpdateStatus(self, event):
        ''''''
        node = self.__tileframe.getHoveredNode(event)
        if node:
            path = node.key.path.replace('\\','/')
            self.__window.setStatusBar(path)

    def __eventToggleBorders(self):
        ''''''
        self.__tileframe.toggleBorders()

    def __eventToggleGradient(self):
        ''''''
        self.__tileframe.toggleGradient()

    def __eventScreenshot(self):
        ''''''
        filename = QtGui.QFileDialog.getSaveFileName(self.__window,
                                                     'Save Screenshot', '',
                                                     'Images (*.png)',
                                                     options=QtGui.
                                                     QFileDialog.
                                                     DontUseNativeDialog)
        if filename:
            if not filename.endswith('.png'):
                filename += '.png'
            self.__tileframe.screenshot(filename)

    def __eventMapFolder(self):
        ''''''
        flags = QtGui.QFileDialog.ShowDirsOnly | QtGui.QFileDialog.\
            DontUseNativeDialog
        folder = QtGui.QFileDialog.getExistingDirectory(None,
                                                        'Select a folder:',
                                                        'C:\\', flags)
        if folder:
            # Update the map and build the tiles
            self.__tileframe.updateMap(folder)
            self.__window.setStatusBar('')

    def __eventClearMap(self):
        ''''''
        message = "Are you sure you want to clear the visualization map?"
        result = QtGui.QMessageBox.question(self.__window, 'Message', message,
                                            QtGui.QMessageBox.Yes,
                                            QtGui.QMessageBox.No)
        if result == QtGui.QMessageBox.Yes:
            self.__tileframe.clearMap()
            self.__window.setStatusBar(self.__defaultStatus)

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
