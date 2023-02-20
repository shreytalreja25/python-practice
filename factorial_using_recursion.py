# Lets find out factorial of a number using recursion

def Facto(n):
    if n == 0:
        return 1
    elif n != 0:
        return n * Facto(n-1)

print(Facto(5))

# Without using recursion
def altFacto(n):
    Factorial = 1
    if n == 0:
        return 1
    elif n != 0:
        for i in range(1,n+1):
            Factorial = Factorial * i

    return Factorial

print(altFacto(4))