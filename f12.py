def echo(post):
     print(post)


def f1(func,post):
    return(func(post))

f1(echo,'Хаюшки')
schedule =((echo,'hiiii'),(echo,'bUUU'))
for (func,arg) in schedule:
    func(arg)

def get(label):
    def echo(post):
        print(label+';'+ post)
    return echo
a=get('Go')
a('Hi!')
