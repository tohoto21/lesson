class MyList(list):
    def __getitem__(self, item):
        print('(indexing %s at %s)' % (self,item))
        return list.__getitem__(self, item - 1)

if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')
    print(x)
    print(x[1])