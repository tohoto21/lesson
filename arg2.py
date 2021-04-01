def f(*g):
    print(g)

f(1,2,3,4)

def f1(a,b,c,d):
    print(a,b,c,d)


args = (1,2,3,4)
#args += (3,4)
f1(*args)