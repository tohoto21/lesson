def min(*args):
    res = args[0]
    for i in args[1:]:
        if i < res:
            res=i
    return res

