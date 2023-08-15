#VARIÁVEIS
contador = 0
posto_1= input('Digite o nome do primeiro posto: ')
gasolina_1= float(input('Digite o valor da gasolina no primeiro posto: '))
etanol_1= float(input('Digite o valor do etanol no primeiro posto: '))
diesel_1= float(input('Digite o preço no diesel no primeiro posto: '))

posto_2= input('Digite o nome do segundo posto: ')
gasolina_2= float(input('Digite o valor da gasolina no segundo posto: '))
etanol_2= float(input('Digite o valor do etanol no segundo posto: '))
diesel_2= float(input('Digite o preço no diesel no segundo posto: '))

posto_3= input('Digite o nome do terceiro posto: ')
gasolina_3= float(input('Digite o valor da gasolina no terceiro posto: '))
etanol_3= float(input('Digite o valor do etanol no terceiro posto: '))
diesel_3= float(input('Digite o preço no diesel no terceiro posto: '))

#MENU
while True:
    print('1)INSERIR O COMBUSTÍVEL DE SUA PREFERÊNCIA E QUANTOS LITROS QUER ABASTECER')
    print('2)MOSTRAR OS DADOS DA PESQUISA E DO POSTO COM RESULTADO MENOR')
    print('3)MOSTAR A LISTA DE TODOS OS POSTOS E SUAS INFORMAÇÕES')
    print('4)SAIR DO PROGRAMA')
    print('-'*30)
    opçoes = int(input('Bem vindo ao menu! Qual das quatro opções você escolherá? '))
    contador += 1    
    if opçoes == 1:
        motorista_combustivel = input('Digite qual combustível você deseja: ')
        motorista_litros = int(input('Digite quantos litros você pretende abastecer: '))
        if motorista_combustivel == 'gasolina':
            preço_gasolina_1 = motorista_litros*gasolina_1
            preço_gasolina_2 = motorista_litros*gasolina_2
            preço_gasolina_3 = motorista_litros*gasolina_3
            if gasolina_1 < gasolina_2 and gasolina_1 < gasolina_3:
                print(f'O posto com a gasolina mais barata é o posto {posto_1}')
                print(f'Ele economizará R${(preço_gasolina_2 - preço_gasolina_1):.2f} em relação ao posto {posto_2}')
                print(f'Ele economizará R${(preço_gasolina_3 - preço_gasolina_1):.2f} em relação ao posto {posto_3}')
            if gasolina_2 < gasolina_1 and gasolina_2 < gasolina_3:
                print(f'O posto com a gasolina mais barata é o {posto_2}')
                print(f'Ele economizará R${(preço_gasolina_1 - preço_gasolina_2):.2f} em relação ao posto {posto_1}')
                print(f'Ele economizará R${(preço_gasolina_3 - preço_gasolina_2):.2f} em relação ao posto {posto_3}')
            if gasolina_3 < gasolina_1 and gasolina_3 < gasolina_2:
                print(f'O posto com a gasolina mais barata é o {posto_3}')
                print(f'Ele economizará R${(preço_gasolina_1 - preço_gasolina_3):.2f} em relação ao posto {posto_1}')
                print(f'Ele economizará R${(preço_gasolina_2 - preço_gasolina_3):.2f} em relação ao posto {posto_2}')
        if motorista_combustivel == 'etanol':
            preço_etanol_1 = motorista_litros*etanol_1
            preço_etanol_2 = motorista_litros*etanol_2
            preço_etanol_3 = motorista_litros*etanol_3
            if etanol_1 < etanol_2 and etanol_1 < etanol_3:
                print(f'O posto com o etanol mais barato é o posto {posto_1}')
                print(f'Você economizará R${(preço_etanol_2 - preço_etanol_1):.2f} em relação ao posto {posto_2}')
                print(f'Você economizará R${(preço_etanol_3 - preço_etanol_1):.2f} em relação ao posto {posto_3}')
            if  etanol_2 < etanol_1 and etanol_2 < etanol_3:
                print(f'O posto com o etanol mais barato é o {posto_2}')
                print(f'Você economizará R${(preço_etanol_1 - preço_etanol_2):.2f} em relação ao posto {posto_1}')
                print(f'Você economizará R${(preço_etanol_3 - preço_etanol_2):.2f} em relação ao posto {posto_3}')
            if etanol_3 < etanol_1 and etanol_3 < etanol_2:
                print(f'O posto com o etanol mais barato é o {posto_3}')
                print(f'Você economizará R${(preço_etanol_1 - preço_etanol_3):.2f} em relação ao posto {posto_1}')
                print(f'Você economizará R${(preço_etanol_2 - preço_etanol_3):.2f} em relação ao posto {posto_2}') 
        if motorista_combustivel == 'diesel':
            preço_diesel_1 = motorista_litros*diesel_1
            preço_diesel_2 = motorista_litros*diesel_2
            preço_diesel_3 = motorista_litros*diesel_3
            if diesel_1 < diesel_2 and diesel_1 < diesel_3:
                print(f'O posto com o diesel mais barato é o posto {posto_1}')
                print(f'Você economizará R${(preço_diesel_2 - preço_diesel_1):.2f} em relação ao posto {posto_2}')
                print(f'Você economizará R${(preço_diesel_3 - preço_diesel_1):.2f} em relação ao posto {posto_3}')
            if diesel_2 < diesel_1 and diesel_2 < diesel_3:
                print(f'O posto com o diesel mais barato é o posto {posto_2}')
                print(f'Você economizará R${(preço_diesel_1 - preço_diesel_2):.2f} em relação ao posto {posto_1}')
                print(f'Você economizará R${(preço_diesel_3 - preço_diesel_2):.2f} em relação ao posto {posto_3}')
            if diesel_3 < diesel_1 and diesel_3 < diesel_2:
                print(f'O posto com o diesel mais barato é o posto {posto_3}')  
                print(f'Você economizará R${(preço_diesel_1 - preço_diesel_3):.2f} em relação ao posto {posto_1}')
                print(f'Você economizará R${(preço_diesel_2 - preço_diesel_3):.2f} em relação ao posto {posto_2}')                                      
    if opçoes == 3:
        print(f'Posto {posto_1}')
        print(f'Gasolina: R${gasolina_1:.2f}')
        print(f'Etanol: R${etanol_1:.2f}')   
        print(f'Diesel: R${diesel_1:.2f}')  

        print(f'Posto {posto_2}')
        print(f'Gasolina: R${gasolina_2:.2f}')   
        print(f'Etanol: R${etanol_2:.2f}')   
        print(f'Diesel: R${diesel_2:.2f}')

        print(f'Posto {posto_3}')
        print(f'Gasolina: R${gasolina_3:.2f}')   
        print(f'Etanol: R${etanol_3:.2f}')   
        print(f'Diesel: R${diesel_3:.2f}')             
    if opçoes == 4:
        print('Você escolheu sair do programa!')
        break

