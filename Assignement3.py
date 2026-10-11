from math import exp
def Trap_Method(f,a,b):
    return ((b-a)/(2))*(f(a)+f(b))


def Trap_Composite_Method(f,a,b,comp):
    h=(b-a)/(comp)
    som=f(a)+f(b)
    x=a
    for i in range(1,comp):
        x+=h
        som+=2*f(x)
    som*=h/2
    return som

def Simpson_Composite_Method(f,a,b,comp):
    h=(b-a)/(comp)
    som=f(a)+f(b)
    x=a+2*h
    for i in range(2,comp-1,2):
        som+=2*f(x)
        x+=2*h

    x=a+h
    for i in range(1,comp,2):
            som+=4*f(x)
            x+=2*h
            

    som*=h/3
    return som





def fon(x):
    return exp(-x**2)


print("La methode trapesoidale:")
print("n=4",Trap_Composite_Method(fon,0,1,4))
print("n=6",Trap_Composite_Method(fon,0,1,6))
print("La methode Simpson:")
print("n=4",Simpson_Composite_Method(fon,0,1,4))
print("n=6",Simpson_Composite_Method(fon,0,1,6))


