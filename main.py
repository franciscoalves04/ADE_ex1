import leitura as lei
import aritemeticas as arit
import resultados as result



while True:
    print("Menu:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Fatorial")
    print("4. Sair")

    option = int(input("O que quer fazer?"))

    if option == 1:
        a = lei.ler_inteiro()
        b = lei.ler_inteiro()
        total = arit.soma(a,b)
        result.mostrar_resultado(total)

    elif option == 2:
        a = lei.ler_inteiro()
        b = lei.ler_inteiro()
        total = arit.subtracao(a, b)
        result.mostrar_resultado(total)

    elif option == 3:
        a = lei.ler_inteiro_positivo()
        arit.fatorial(a)
        total = arit.fatorial(a)
        result.mostrar_resultado(total)

    elif option == 4:
        break

    else:
        print("Opção invalida ")



