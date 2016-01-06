class FileSystem(object):

    def __init__(self, path, size):
        '''(FileSystem, str, int, tuple) -> NoneType
        Create a new FileSystem with path and size.'''
        self.path = path
        self.size = size
