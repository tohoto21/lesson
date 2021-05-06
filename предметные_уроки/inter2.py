def intersect(*args):
    res = []
    for i in args[0]:
        if i in res: continue
        for j in args[1:]:
            if i not in j: break
        else:
            res.append(i)


def union(*args ):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res