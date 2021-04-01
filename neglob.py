def f1(N):
    def f2(M):
        return M**N
    return f2

a= f1(2)
print(a(3))
print(a(5))
b=f1(3)
print(b(6))
