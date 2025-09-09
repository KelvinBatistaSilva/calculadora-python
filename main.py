# main.py
# Projeto simples em Python - Calculadora básica (versão corrigida)

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

if __name__ == "__main__":
    while True:
        print("\n=== Calculadora Básica ===")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("0 - Sair")

        try:
            opcao = int(input("Digite a opção: "))
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

        if opcao == 0:
            print("Encerrando a calculadora...")
            break

        if opcao not in [1, 2, 3, 4]:
            print("Opção inválida!")
            continue

        try:
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")
            continue

        if opcao == 1:
            print("Resultado:", somar(x, y))
        elif opcao == 2:
            print("Resultado:", subtrair(x, y))
        elif opcao == 3:
            print("Resultado:", multiplicar(x, y))
        elif opcao == 4:
            print("Resultado:", dividir(x, y))
