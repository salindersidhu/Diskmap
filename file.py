from filesystem import FileSystem


class File(FileSystem):
    '''A File class which inherits from FileSystem.'''

    def __init__(self, path, size, color):
        '''(File, str, int, tuple) -> NoneType
        Create a new File with path, size and color.'''
        FileSystem.__init__(self, path, size, color)
