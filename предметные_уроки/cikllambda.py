def f1():
    a=[]
    j=0
    for i in range(5):
        j=j+1
        a.append(lambda x,j=j:j**x)
        print(j)
    return a
b=f1()
print(b[1](2))


