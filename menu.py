def concatenar_dados():
    d1 = input("Digite o primeiro dado: ")
    d2 = input("Digite o segundo dado: ")
    print("Resultado da concatenação:", d1 + d2)

def repetir_textos():
    texto = input("Digite um texto: ")
    vezes = int(input("Quantas vezes repetir? "))
    print(texto * vezes)

def operacoes_matematicas():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    op = input("Escolha a operação (+, -, *, /): ")
    if op == "+":
        print("Resultado:", num1 + num2)
    elif op == "-":
        print("Resultado:", num1 - num2)
    elif op == "*":
        print("Resultado:", num1 * num2)
    elif op == "/":
        print("Resultado:", num1 / num2)
    else:
        print("Operação inválida!")

def verificar_par_impar():
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")

def calcular_media():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    media = (n1 + n2 + n3) / 3
    print("A média é:", media)

def verificar_palindromo():
    palavra = input("Digite uma palavra: ").lower()
    if palavra == palavra[::-1]:
        print("É um palíndromo")
    else:
        print("Não é um palíndromo")

def menu():
    while True:
        print("\n=== MENU DE EXERCÍCIOS PYTHON ===")
        print("1 - Concatenar Dados")
        print("2 - Repetir Textos")
        print("3 - Operações Matemáticas Simples")
        print("4 - Verificar Par ou Ímpar")
        print("5 - Calcular Média de Notas")
        print("6 - Verificar Palíndromos")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            concatenar_dados()
        elif escolha == "2":
            repetir_textos()
        elif escolha == "3":
            operacoes_matematicas()
        elif escolha == "4":
            verificar_par_impar()
        elif escolha == "5":
            calcular_media()
        elif escolha == "6":
            verificar_palindromo()
        elif escolha == "0":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
