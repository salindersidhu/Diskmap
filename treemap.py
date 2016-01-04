import os
from random import uniform
from node import Node
from file import File
from directory import Directory


class Treemap(object):
    '''A Treemap class.'''

    def __init__(self):
        '''(Treemap) -> NoneType
        Create a new Treemap.'''
        self.root = None

    def __randomColourHSV():
        '''(None) -> tuple
        Return a random colour using an aesthetically pleasing colour
        palette. The colour is in the form of 3-tupple with HSV values.'''
        goldenRatioConjugate = 0.618033988749895
        h = uniform(0, 1)
        h += goldenRatioConjugate
        h %= 1
        return (h, 0.5, 0.95)

    def __build(self, directory):
        '''(Treemap, str) -> Node.
        Return the root of a sub tree containing an arbitrary number of Nodes
        with keys representing all the files and folders in directory as File
        and Directory objects.'''
        dirNode = Node(Directory(directory, 0))
        dirSize = 0
        # Search for all files and folders within the directory
        for item in os.listdir(directory):
            itemPath = os.path.join(directory, item)
            itemSize = os.path.getsize(itemPath)
            # Check if item is a directory
            if os.path.isdir(itemPath):
                # Recursively obtain the Node and add it to the container of
                # the current Directory's Node.
                node = self.__build(itemPath)
                dirNode.add(node)
                dirSize += node.key.size
            else:
                # Create a File node and add it to the current Directory's Node
                node = Node(File(itemPath, itemSize, self.__randomColourHSV()))
                dirNode.add(node)
                dirSize += itemSize
        # Save new filesize to directory object
        dirNode.key.size = dirSize
        return dirNode

    def build(self, directory):
        '''(Treemap, str) -> NoneType
        Create a tree with the root associated with a Node with key Directory
        associated with directory and an arbitrary number of children Nodes
        with key associated with File and Directory objects.'''
        self.root = self.__build(directory)

    def getRoot(self):
        '''(Treemap) -> Node
        Return the root of the entire Treemap.'''
        return self.root

    def getFileInfo(self, path):
        '''(Treemap, str) -> list
        Return a tuple (file path, size and percentage relative to the total
        size of the Directory associated with the root of Treemap) of the File
        associated with path.'''
        totalSize = float(self.root.key.size)
        node = self._search(path, self.root)  # Find the correct Node
        percent = (node.key.size / totalSize) * 100
        size = node.key.size / 1024  # 1024 bytes equal exactly 1 KB
        return [path, size, percent]
