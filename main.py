from bisseccao import bissecao
from decimal import Decimal

def main():
    a, b = map(Decimal, input("Digite a e b:").split())

    dados_obtidos = bissecao(a, b, 0)
    dados_obtidos.insert(0, ['n','a','b','x','f(x)','e'])

    if dados_obtidos != False:
        for linha in dados_obtidos:
            linha_formatada = [str(item) if item is not None else "-" for item in linha]
            print(f"{linha_formatada[0]:^5} | {linha_formatada[1]:^10} | {linha_formatada[2]:^10} | {linha_formatada[3]:^10} | {linha_formatada[4]:^10} | {linha_formatada[5]:^10}")
    else:
        print("f(a)*f(b) > 0")


if __name__ == "__main__":
    main()