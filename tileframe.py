from PyQt4 import QtGui, QtCore
from treemap import Treemap


class TileFrame(QtGui.QFrame):
	''''''

	def __init__(self, parentWindow, width, height):
		''''''
		super(TileFrame, self).__init__(parentWindow)
		# TileFrame variables
		self.__treemap = None
		# Set strong policy for focusing keyboard events to Tileframe
		self.setFocusPolicy(QtCore.Qt.StrongFocus)

	def clearMap(self):
		''''''
		self.__treemap = None

	def updateMap(self, treemap):
		''''''
		self.__treemap = treemap

	def paintEvent(self, event):
		''''''
		# By default, if there is no loaded Treemap, then switch to default
		# display. Gray rectangle with darker grey text called "Visualizer".
		if self.__treemap:
			pass
		else:
			pass
