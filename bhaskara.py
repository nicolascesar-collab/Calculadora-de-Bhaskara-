import math

while True:

    print("Calculadora de Bhaskara")
    print(" " * 30)

    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    print(" " * 30)
    delta = b**2 - 4*a*c
    print("Delta =", delta)
    print(" " * 30)

    if delta < 0:
        print("A equação não possui raízes reais")
        print(" " * 30)

    elif delta == 0:
        x = -b / (2*a)
        print("A equação possui uma raiz:")
        print("x =", x)
        print(" " * 30)

    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        print("A equação possui duas raízes:")
        print("x1 =", x1)
        print("x2 =", x2)
        print(" " * 30)

    resposta = input("\nDeseja calcular outra equação? (sim/nao): ").lower().strip()
    print(" " * 30)

    if resposta.lower() == "nao":
        print("Encerrando programa...")
        break
