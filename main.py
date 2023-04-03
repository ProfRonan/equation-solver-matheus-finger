grau = int(input())
if grau < 1 or grau > 2:
    print("Grau inválido")
elif grau == 1:
    print('A equação é do primeiro grau')
    a = float(input())
    if a == 0:
        print('Valor de a inválido')
    else:
        b = float(input())
        raiz = (-b)/a
        print(f'{raiz:.2f}')
elif grau == 2:
    print('A equação é do segundo grau')
    a = float(input())
    if a == 0:
        print('Valor de a inválido')
    else:
        b = float(input())
        c = float(input())
        delta = (b ** 2) - 4 * a * c
        if delta < 0:
            print('A equação não possui raízes reais')
        elif delta == 0:
            print('A equação possui apenas uma raiz real')
            raiz = (-b) / (2 * a)
            print(f'{raiz:.2f}')
        else:
            print('A equação possui duas raízes reais')
            raiz1 = ((-b) + (delta ** 0.5)) / (2 * a)
            raiz2 = ((-b) - (delta ** 0.5)) / (2 * a)
            print(f'{raiz2:.2f}')
            print(f'{raiz1:.2f}')