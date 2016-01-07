from filesystem import FileSystem


class Directory(FileSystem):
    '''A Directory class which inherits from FileSystem.'''

    def __init__(self, path, size, colour=None):
        '''Create a new Directory with path and size.'''
        FileSystem.__init__(self, path, size, colour)
