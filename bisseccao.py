from decimal import Decimal, ROUND_HALF_UP

gabarito_5_casas = Decimal('0.00001')

def f(x):
    return x**2 - Decimal(3)

def pontoM(a, b):
    return (a+b)/Decimal(2)

def distancia(atual, anterior):
    return abs(atual - anterior)

def bissecao(a: Decimal, b: Decimal, n, dados = None):

    if dados is None:
        dados = []
        a = a.quantize(gabarito_5_casas, rounding=ROUND_HALF_UP)
        b = b.quantize(gabarito_5_casas, rounding=ROUND_HALF_UP)
        
    

    fa = f(a).quantize(gabarito_5_casas, rounding=ROUND_HALF_UP)
    fb = f(b).quantize(gabarito_5_casas, rounding=ROUND_HALF_UP)

    if fa*fb > 0:
        return dados

        
    x = pontoM(a,b).quantize(gabarito_5_casas, rounding=ROUND_HALF_UP)
    fx = f(x).quantize(gabarito_5_casas, rounding=ROUND_HALF_UP)

    if fx == 0:
        dados.append([n, a, b, x, fx, Decimal(0).quantize(gabarito_5_casas, rounding=ROUND_HALF_UP)])
        return dados

    dist = None

    if n != 0:
        dist = distancia(x, dados[n - 1][3]).quantize(gabarito_5_casas, rounding=ROUND_HALF_UP)

        if dist < Decimal('0.1'):
            dados.append([n, a, b, x, fx, dist])
            return dados


    dados.append([n, a, b, x, fx, dist])

    if fa*fx > 0:
        return bissecao(x, b, n+1, dados)
    else:
        return bissecao(a, x, n+1, dados)


