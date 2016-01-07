from filesystem import FileSystem


class File(FileSystem):
    '''A File class which inherits from FileSystem.'''

    def __init__(self, path, size):
        '''Create a new File with path and size.'''
        FileSystem.__init__(self, path, size)
