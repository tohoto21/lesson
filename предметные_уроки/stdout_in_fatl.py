import sys

def f1():
    sys.stdout = open('nottext.txt','a')
    print('pervi')
    f2()

def f2():
    print('vtor')
    f3()

def f3():
    print('three')
    sys.stdout.close()
    pass

if __name__ == '__main__' :
    f1()

