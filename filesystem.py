class FileSystem(object):

    def __init__(self, path, size, color=None):
        '''(FileSystem, str, int, [tuple]) -> NoneType
        Create a new FileSystem with path, size and color.'''
        self.path = path
        self.size = size
        self.color = color
