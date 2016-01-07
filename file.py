from filesystem import FileSystem


class File(FileSystem):
    '''A File class which inherits from FileSystem.'''

    def __init__(self, path, size, colour):
        '''Create a new File with path, size and colour.'''
        FileSystem.__init__(self, path, size, colour)
