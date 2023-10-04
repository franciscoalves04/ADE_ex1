def ler_inteiro():
    try:
        num = int(input("Digite um número inteiro: "))
        return num
    except ValueError:
        print("Erro: Isto não é um número inteiro")
        return ler_inteiro()

def ler_inteiro_positivo():
    try:
        num = int(input("Digite um número inteiro positivo: "))
        if num >= 0:
            return num
        else:
            print("Erro: O número é negativo")
            return ler_inteiro_positivo()
    except ValueError:
        print("Erro: Isso não é um número inteiro positivo")
        return ler_inteiro_positivo()
