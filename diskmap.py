import os
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from guiwindow import GUIWindow
from tileframe import TileFrame


class DiskmapApp(QtWidgets.QApplication):
    '''DiskmapApp extends the QtWidgets.QApplication class. This class creates
    the GUI for the Diskmap application and provides functions for all of the
    application's events. It uses TileFrame and GUIWindow to create a window,
    menu, status bar and the frame where the Treemap tiles are rendered.'''

    def __init__(self, args):
        '''Create a new DiskmapApp with arguments specified by args.'''
        super(DiskmapApp, self).__init__(args)
        # Application variables
        self.__defaultStatus = "Please open a folder to map..."
        self.__mappedDir = ''
        self.__currentFile = ''
        # Configure the GUIWindow
        self.__window = GUIWindow('Diskmap - Disk Visualization Utility',
                                  640,
                                  360,
                                  'assets/icon.svg')
        # Configure the Tileframe
        self.__tileframe = TileFrame(self.__window)
        self.__window.setCentralWidget(self.__tileframe)
        self.__window.setMouseTracking(True)
        # Setup remaining GUI elements
        self.__setupMenu()
        self.__setupMouseEvents()
        self.__setupMenuItems()
        self.__window.setStatusBar(self.__defaultStatus)
        # Render the window
        self.__window.show()

    def __setupMenu(self):
        '''Add all the menus used in the application to GUIWindow.'''
        self.__window.addMenu('File')
        self.__window.addMenu('Options')
        self.__window.addMenu('Settings')
        self.__window.addMenu('Help')

    def __setupMouseEvents(self):
        '''Bind event functions for mouse movement, mouse click and mouse
        release events to GUIWindow.'''
        moveEvents = []
        clickEvents = []
        releaseEvents = []
        # Add function to mouse event lists
        moveEvents.append(self.__eventUpdateStatus)
        clickEvents.append(self.__eventPopupMenu)
        # Bind the mouse functions to the mouse events
        self.__window.updateMouseEvents(moveEvents, clickEvents, releaseEvents)

    def __setupMenuItems(self):
        '''Add all the menu items, along with their event functions, used in
        the application to GUIWindow.'''
        # Setup File menu items
        self.__window.addMenuItem('File', 'Map Folder', self.__eventMapFolder)
        self.__window.addMenuSeperator('File')
        self.__window.addMenuItem('File', 'Quit', self.__window.close)
        # Setup Option menu items
        self.__window.addMenuItem('Options',
                                  'Screenshot',
                                  self.__eventScreenshot)
        self.__window.addMenuItem('Options', 'Clear Map', self.__eventClearMap)
        # Setup Settings menu items
        self.__window.addCheckableMenuItem('Settings',
                                           'Gradient',
                                           False,
                                           self.__eventToggleGradient)
        self.__window.addCheckableMenuItem('Settings',
                                           'Borders',
                                           True,
                                           self.__eventToggleBorders)
        # Setup Help menu items
        self.__window.addMenuItem('Help', 'About', self.__eventAbout)

    def __showException(self, exception):
        '''Show a popup message box with the exception that occured.'''
        message = "An unexpected error occured:\n\n {}".format(str(exception))
        QtWidgets.QMessageBox.critical(self.__window,
                                       'Error',
                                       message,
                                       buttons=QtWidgets.QMessageBox.Ok)

    def __eventUpdateStatus(self, event):
        '''Set the status bar text to the file path of the currently mouse
        hovered FileNode from the TileFrame. Set the mouse cursor to a hand
        pointer if a path exists, set the mouse cursor to the standard
        arrow otherwise.'''
        path = self.__tileframe.getHoveredNodePath(event)
        if path:
            # Set the cursor to pointing hand cursor
            self.setOverrideCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            # Replace the backslash with forward slash in the file path
            self.__filename = path.replace('\\', '/')
            self.__window.setStatusBar(self.__filename)
        else:
            # Restore cursor back to arrow cursor
            self.setOverrideCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def __eventPopupMenu(self, event):
        '''Create a popup menu iff a visualization map exists and the right
        mouse click event occured. The popup menu contains options to rename,
        move and delete the currently selected file.'''
        # If mouse right click and map is created
        if event.button() == QtCore.Qt.RightButton and \
           self.__tileframe.isMapped():
            menu = QtWidgets.QMenu()
            # Create menu items and bind events to them
            renameFileAction = QtWidgets.QAction('Rename', self)
            moveFileAction = QtWidgets.QAction('Move', self)
            deleteFileAction = QtWidgets.QAction('Delete', self)
            renameFileAction.triggered.connect(self.__eventMenuRenameFile)
            moveFileAction.triggered.connect(self.__eventMenuMoveFile)
            deleteFileAction.triggered.connect(self.__eventMenuDeleteFile)
            # Add actions to menu and create menu
            menu.addAction(renameFileAction)
            menu.addAction(moveFileAction)
            menu.addAction(deleteFileAction)
            menu.exec_(self.__window.mapToGlobal(event.pos()))

    def __getOnlyFilename(self):
        '''Return the name of the file, as a string, from the file's full
        path.'''
        return self.__filename[self.__filename.rfind('/') + 1:]

    def __getOnlyParentFolder(self):
        '''Return the path of the file up to the parent directory, as a string,
        from the file's full path.'''
        return self.__filename[:self.__filename.rfind('/')]

    def __eventMenuRenameFile(self):
        '''Rename a selected file to a new specified name.'''
        message = 'Enter a new name for file: ' + self.__getOnlyFilename()
        text, result = QtWidgets.QInputDialog.getText(self.__window,
                                                      'Message',
                                                      message)
        # If ok was selected and text is no empty
        if result and text:
            # Rename the file and remap the directory
            newFilename = self.__getOnlyParentFolder() + '/' + text
            try:
                os.rename(self.__filename, newFilename)
                self.__tileframe.updateMap(self.__mappedDir, False)
            except OSError as error:
                # Exception raised, display message and terminate
                self.__showException(error)
                self.__window.close()

    def __eventMenuMoveFile(self):
        '''Move a selected file to a new specified folder.'''
        flags = QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.\
            DontUseNativeDialog
        folder = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                            'Select a folder:',
                                                            'C:\\', flags)
        # If a folder was selected
        if folder:
            # Move the file to the new destination and remap the directory
            newFileDestination = folder + '/' + self.__getOnlyFilename()
            try:
                os.rename(self.__filename, newFileDestination)
                self.__tileframe.updateMap(self.__mappedDir, False)
            except OSError as error:
                # Exception raised, display message and terminate
                self.__showException(error)
                self.__window.close()

    def __eventMenuDeleteFile(self):
        '''Delete a selected file.'''
        message = 'Are you sure you want to delete ' + \
            self.__getOnlyFilename() + '?'
        result = QtWidgets.QMessageBox.question(self.__window,
                                                'Message',
                                                message,
                                                QtWidgets.QMessageBox.Yes,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            try:
                # Delete the file and remap the directory
                os.remove(self.__filename)
                self.__tileframe.updateMap(self.__mappedDir, False)
            except OSError as error:
                # Exception raised, display message and terminate
                self.__showException(error)
                self.__window.close()

    def __eventToggleBorders(self):
        '''Toggle rendering borders in the TileFrame.'''
        self.__tileframe.toggleBorders()

    def __eventToggleGradient(self):
        '''Toggle rendering gradients in the TileFrame.'''
        self.__tileframe.toggleGradient()

    def __eventScreenshot(self):
        '''Prompt the user to save a screenshot of the visualization map and
        save the screenshot as a .PNG file.'''
        # If a map is created
        if self.__tileframe.isMapped():
            fname, _ = QtWidgets.QFileDialog.getSaveFileName(
                self.__window,
                'Save Screenshot',
                '',
                'Images (*.png)',
                options=QtWidgets.QFileDialog.DontUseNativeDialog)
            if fname:
                if not fname.endswith('.png'):
                    fname += '.png'
                self.__tileframe.screenshot(fname)

    def __eventMapFolder(self):
        '''Prompt the user to select a folder to use for creating the
        visualization map. Build the visualization if the user has selected a
        valid folder.'''
        flags = QtWidgets.QFileDialog.ShowDirsOnly | QtWidgets.QFileDialog.\
            DontUseNativeDialog
        folder = QtWidgets.QFileDialog.getExistingDirectory(None,
                                                            'Select a folder:',
                                                            'C:\\', flags)
        # If a folder was selected
        if folder:
            # Store the mapped folder
            self.__mappedDir = folder
            try:
                # Reset checkable menu items
                self.__window.setCheckedMenuItem('Gradient', False)
                self.__window.setCheckedMenuItem('Borders', True)
                # Update the map and build the tiles
                self.__tileframe.updateMap(folder)
            except (Exception) as error:
                # Exception raised, display message and terminate
                self.__showException(error)
                self.__window.close()
            finally:
                self.__window.setStatusBar('')

    def __eventClearMap(self):
        '''Prompt the user to clear the visualization map. Clear the map, reset
        the checkable menu items and set the default status text iff the user
        confirmed Yes to the message prompt.'''
        # If a map is created
        if self.__tileframe.isMapped():
            message = 'Are you sure you want to clear the visualization map?'
            result = QtWidgets.QMessageBox.question(self.__window,
                                                    'Message',
                                                    message,
                                                    QtWidgets.QMessageBox.Yes,
                                                    QtWidgets.QMessageBox.No)
            if result == QtWidgets.QMessageBox.Yes:
                # Reset checkable menu items
                self.__window.setCheckedMenuItem('Gradient', False)
                self.__window.setCheckedMenuItem('Borders', True)
                self.__tileframe.clearMap()
                self.__window.setStatusBar(self.__defaultStatus)

    def __eventAbout(self):
        '''Display an information dialog about the program languages and tools
        used to create this application and the name of the developer.'''
        message = 'Disk Space Visualization Utility\n\nPython 3, PyQt 5\n' + \
            '\nCreated by Salinder Sidhu'
        # Render the message box
        QtWidgets.QMessageBox.information(self.__window,
                                          'About',
                                          message,
                                          buttons=QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    # Pass command line arguments into application
    myApp = DiskmapApp(sys.argv)
    sys.exit(myApp.exec_())
