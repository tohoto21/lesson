class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, item):
        print('Trace: ' + item)
        return getattr(self.wrapped, item, 7)

x= Wrapper([1,2,3])
