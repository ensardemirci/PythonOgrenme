
def f(i):
    c=1
    while i>0:
        c=i*c
        i=i-1
    return c

def sinus(x):
    k = -1
    u = -3
    t= 0
    while k <= 80:
        u=u+4
        k=k+4
        b = (x**(u))/ f(u)
        c = -((x**(k))/ f(k))
        t=b+c+t
        print(t)
    return t

pi=3.141592653589793
print(sinus(pi/2))



