#um conversor de varias coisas

import requests as re
import json

cotacoes = re.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
dolar_c = float(cotacoes['USDBRL']["bid"])
euro_c = float (cotacoes['EURBRL']["bid"])



print('''O que deseja converter? 
          [1] Metros para Centrimetros
          [2] Horas para Minutos
          [3] Moeda
          [4] Sair 
          ''')
opcao = 0
while opcao != 4:
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        metros = input('Digite para converte de metros para cm:').replace(',', '.')
        m = float(metros)
        cm = m * 100
        print(f'{m} metros em minutos é: {cm} ')
    elif opcao == 2:
      horas = input(f'Digite para converte de horas para minutos: ').replace(':', '.')
      h = horas[0:2]
      m = horas[3:5]
      hf = float(h) 
      mf = float(m)
      hr = hf * 60
      mt = mf + hr
      print(f'{h}:{m} horas em minutos é: {mt:.0f}')
    elif opcao == 3:
        print('''
              [1] Dolar para Real
              [2] Euro para Real
              [3] Menu Anterior''')
        opcao = 0
        while opcao !=3:
            opcao = int(input("Qual Moeda? "))
            if opcao == 1:
                dolar = input("Quantos dolares? ").replace(',', '.')
                dolarf = float(dolar)
                real = dolarf * dolar_c
                
                print(f'Hoje a cotação do dolar está {dolar_c:.2f}, então {dolarf:.2f} Dolares em Reais é: {real:.2f}')
            elif opcao == 2:
                euro = input("Quantos Euros? ").replace(',', '.')

                eurof = float(euro)
                real = eurof * euro_c
            
                print(f'{eurof} Euros em Reais é: {real:.2f}')
                
    elif opcao == 4:
        print('Finalizando')
            
    else:
        print('Opção Invdálida, tente novamente')
    
    
    
print("Fim")

