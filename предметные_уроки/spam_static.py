class Spam:
    numinstances = 0
    def __init__(self):
        Spam.numinstances = Spam.numinstances + 1
    def printNuminstances():
        print('Number of instances created: %s' % Spam.numinstances)
    printNuminstances = staticmethod(printNuminstances)

class Sub(Spam):
    def printNuminstances():
        print("Extra stuff...")
        Spam.printNuminstances()
    printNuminstances = staticmethod(printNuminstances)

