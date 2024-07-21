def menu():
  print('====== menu =======')
  print('1 - Temperaturas')
  print('2 - Distancias')
  print('3 - Pesos')
  print('4 - Sair')

def qual_temperatura():
  input('Qual temperatura vai inserir?')

  print('1 - Celsius (C°)')
  print('2 - Fahrenheit (F)')
  print('3 - Kelvin')

def qual_distancia():
  input('Qual distancia vai inserir?')

  print('1 - Metros (M)')
  print('2 - Kilometros (Km)')
  print('3 - Centimetros (Cm)')

def qual_peso():
  input('Qual peso vai inserir?')

  print('1 - Gramas (g)')
  print('2 - Kilos (Kg)')
  print('3 - Miligrama (Mg)')

def celsius_conversao(y):
  print((y * 9/5) + 32)


def conversao_de_temperatura():
  x = qual_temperatura()

  if x == 1:
    y = float(input('Insira quantos os graus Celsius: '))
    celsius_conversao(y)




def main ():
  while(1):
    menu()
    opc = int(input('-> '))

    if opc == 1:
      x = qual_temperatura()
    

main()