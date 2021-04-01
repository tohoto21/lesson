def tester (start) :
    state = [start]
    def nested(label):
        #nonlocal state # Запоминает из объемлющей области видимости
        print(label, state[0])
        state[0] += 1 # Нелокальную переменную разрешено изменять

    return nested
a=tester(0)
print(a('s'))
print(a('n'))
print(a('s'))
print(a.label)