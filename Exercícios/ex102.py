import math


def fatorial(n, show=False):
    if not show:
        x = math.factorial(n)
        return x
    else:
        for c in range(n, 0, -1):
            print(c, end='')
            if c == 1:
                print(' = ', end='')
            else:
                print(' x ', end='')
        x = math.factorial(n)
        return x


print(fatorial(10, show=True))
