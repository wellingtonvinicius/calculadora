print("\n######## Python calculadora ########")

def add(x, y):
    return x + y 

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y 

def divide(x, y):
    return x / y

print("\n Selecione a operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("\n  Qual operação quer realizar? (1/2/3/4: )")

num1 = int(input("\n Digite o número:"))
num2 = int(input("\n Digite o outro número"))

if escolha == '1':
    print("\n")
    print(num1, "+", num2, "=", add(num1, num2))
    print("\n")

elif escolha == '2':
    print("\n")
    print(num1, "-", num2, "=", subtract(num1, num2))
    print("\n")

elif escolha == '3':
    print("\n")
    print(num1, "*", num2, "=", multiply(num1, num2))
    print("\n")

elif escolha == '4':
    print("\n")
    print(num1, "/", num2, "=", divide(num1, num2))
    print("\n")

else:
    print("Opção invalida!")