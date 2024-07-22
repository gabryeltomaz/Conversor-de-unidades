def menu():
    print('====== Menu =======')
    print('1 - Temperaturas')
    print('2 - Distâncias')
    print('3 - Pesos')
    print('4 - Sair')

def qual_temperatura():
    print('Qual temperatura deseja converter?')
    print('1 - Celsius (C°)')
    print('2 - Fahrenheit (F)')
    print('3 - Kelvin')
    x = int(input('-> '))
    if x == 1:
        celsius_conversao()
    elif x == 2:
        fahrenheit_conversao()
    elif x == 3:
        kelvin_conversao()

def qual_distancia():
    print('Qual distância deseja converter?')
    print('1 - Metros (M)')
    print('2 - Quilômetros (Km)')
    print('3 - Centímetros (Cm)')
    x = int(input('-> '))
    if x == 1:
        distancia_conversao('metros')
    elif x == 2:
        distancia_conversao('quilômetros')
    elif x == 3:
        distancia_conversao('centímetros')

def distancia_conversao(tipo):
    if tipo == 'metros':
        valor = float(input('Insira os metros: '))
    elif tipo == 'quilômetros':
        valor = float(input('Insira os quilômetros: ')) * 1000
    elif tipo == 'centímetros':
        valor = float(input('Insira os centímetros: ')) / 100

    km = valor / 1000
    hm = valor / 100
    dam = valor / 10
    dm = valor * 10
    cm = valor * 100
    mm = valor * 1000

    print(f'{km:.2f} km - {hm:.2f} hm - {dam:.2f} dam - {valor:.2f} m - {dm:.2f} dm - {cm:.2f} cm - {mm:.2f} mm')

def qual_peso():
    print('Qual peso deseja converter?')
    print('1 - Gramas (g)')
    print('2 - Quilos (Kg)')
    print('3 - Miligrama (Mg)')
    x = int(input('-> '))
    if x == 1:
        peso_conversao('gramas')
    elif x == 2:
        peso_conversao('quilos')
    elif x == 3:
        peso_conversao('miligramas')

def peso_conversao(tipo):
    if tipo == 'gramas':
        valor = float(input('Insira as gramas: '))
    elif tipo == 'quilos':
        valor = float(input('Insira os quilos: ')) * 1000
    elif tipo == 'miligramas':
        valor = float(input('Insira os miligramas: ')) / 1000

    kg = valor / 1000
    mg = valor * 1000

    print(f'{kg:.2f} kg - {valor:.2f} g - {mg:.2f} mg')

def celsius_conversao():
    c = float(input('Quantos Celsius: '))
    f = (c * 9/5) + 32
    k = c + 273.15
  
    print(f'{k:.5} K - {c:2} °C - {f:2} °F')


def fahrenheit_conversao():
    f = float(input('Quantos Fahrenheit: '))
    c = (f - 32) / 1.8
    k = c + 273.15

    print(f'{k:.2} K - {c:2} °C - {f:2} °F')

def kelvin_conversao():
    k = float(input('Quantos Kelvin: '))
    c = k - 273.15
    f = k * (9/5) - 459.67
    
    print(f'{k:.2} K - {c:2} °C - {f:2} °F')

def main():
    while True:
        menu()
        opc = int(input('-> '))
        if opc == 1:
            qual_temperatura()
        elif opc == 2:
            qual_distancia()
        elif opc == 3:
            qual_peso()
        elif opc == 4:
            print('Saindo...')
            break
        else:
            print('Opção inválida, tente novamente.')

main()
