class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attername):
        print('Trace: ' + attername)
        return  getattr(self.wrapped, attername)