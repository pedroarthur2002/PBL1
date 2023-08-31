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

contador_gasolina_1 = 0
contador_gasolina_2 = 0
contador_gasolina_3 = 0
contador_etanol_1 = 0
contador_etanol_2 = 0
contador_etanol_3 = 0
contador_diesel_1 = 0
contador_diesel_2 = 0
contador_diesel_3 = 0
soma_gasolina_1 = 0
soma_etanol_1 = 0
soma_diesel_1 = 0
soma_gasolina_2 = 0
soma_etanol_2 = 0
soma_diesel_2 = 0
soma_gasolina_3 = 0
soma_etanol_3 = 0
soma_diesel_3 = 0
menor_gasolina = 0
menor_etanol = 0
menor_diesel = 0
maior_gasolina = 0
maior_etanol = 0
maior_diesel = 0

#MENU
while True:
    print('1)INSERIR O COMBUSTÍVEL DE SUA PREFERÊNCIA E QUANTOS LITROS QUER ABASTECER')
    print('2)MOSTRAR OS DADOS DA PESQUISA E DO POSTO COM RESULTADO MENOR')
    print('3)MOSTAR A LISTA DE TODOS OS POSTOS E SUAS INFORMAÇÕES')
    print('4)SAIR DO PROGRAMA')
    print('-'*50)
    opçoes = int(input('BEM VINDO AO MENU! Qual das quatro opções você escolherá? '))
    if (opçoes != 3 and opçoes != 1 and opçoes != 2 and opçoes != 4):
        print('Digite uma das quatro opções válidas!')
        print('')        
    if opçoes == 1:
        contador += 1
        print('[1] GASOLINA')
        print('[2] ETANOL')
        print('[3] DIESEL')
        motorista_combustivel = int(input('Digite qual combustível você deseja: '))        
        motorista_litros = int(input('Digite quantos litros você pretende abastecer: '))        
        if (motorista_combustivel != 3 and motorista_combustivel != 1 and motorista_combustivel != 2):
            print('Digite uma das três opções válidas!')
        elif (motorista_combustivel != 3 and motorista_combustivel != 1 and motorista_combustivel != 2) and motorista_litros < 0:
            print('Digite uma das três opções válidas!')
            print('Digite uma litragem válida!')
        elif motorista_litros < 0:
            print('Digite uma litragem válida!')
        print('')
        preço_gasolina_1 = motorista_litros*gasolina_1
        preço_gasolina_2 = motorista_litros*gasolina_2
        preço_gasolina_3 = motorista_litros*gasolina_3
        preço_etanol_1 = motorista_litros*etanol_1
        preço_etanol_2 = motorista_litros*etanol_2
        preço_etanol_3 = motorista_litros*etanol_3
        preço_diesel_1 = motorista_litros*diesel_1
        preço_diesel_2 = motorista_litros*diesel_2
        preço_diesel_3 = motorista_litros*diesel_3
        if motorista_combustivel == 1:                        
            if gasolina_1 < gasolina_2 and gasolina_1 < gasolina_3:
                contador_gasolina_1 += 1
                soma_gasolina_1 += motorista_litros 
                print(f'O posto com a gasolina mais barata é o posto {posto_1} cujo preço é de R${(gasolina_1):.2f}/L')
                print(f'O valor pago foi de R${(preço_gasolina_1):.2f}')
                print(f'Ele economizará R${(preço_gasolina_2 - preço_gasolina_1):.2f} em relação ao posto {posto_2}')
                print(f'Ele economizará R${(preço_gasolina_3 - preço_gasolina_1):.2f} em relação ao posto {posto_3}')
                print('-'*50)                
            if gasolina_2 < gasolina_1 and gasolina_2 < gasolina_3:
                contador_gasolina_2 += 1
                soma_gasolina_2 += motorista_litros              
                print(f'O posto com a gasolina mais barata é o {posto_2} cujo preço é de R${(gasolina_2):.2f}/L')
                print(f'O valor pago foi de R${(preço_gasolina_2):.2f}')
                print(f'Ele economizará R${(preço_gasolina_1 - preço_gasolina_2):.2f} em relação ao posto {posto_1}')
                print(f'Ele economizará R${(preço_gasolina_3 - preço_gasolina_2):.2f} em relação ao posto {posto_3}')
                print('-'*50)                            
            if gasolina_3 < gasolina_1 and gasolina_3 < gasolina_2:
                contador_gasolina_3 += 1
                soma_gasolina_3 += motorista_litros
                print(f'O posto com a gasolina mais barata é o {posto_3} cujo preço é de R${(gasolina_3):.2f}/L')
                print(f'O valor pago foi de R${(preço_gasolina_3):.2f}')
                print(f'Ele economizará R${(preço_gasolina_1 - preço_gasolina_3):.2f} em relação ao posto {posto_1}')
                print(f'Ele economizará R${(preço_gasolina_2 - preço_gasolina_3):.2f} em relação ao posto {posto_2}')
                print('-'*50)               
        if motorista_combustivel == 2:            
            if etanol_1 < etanol_2 and etanol_1 < etanol_3:
                contador_etanol_1 += 1
                soma_etanol_1 += motorista_litros
                print(f'O posto com o etanol mais barato é o posto {posto_1} cujo preço é de R${(etanol_1):.2f}/L')
                print(f'O valor pago foi de R${(preço_etanol_1):.2f}')
                print(f'Você economizará R${(preço_etanol_2 - preço_etanol_1):.2f} em relação ao posto {posto_2}')
                print(f'Você economizará R${(preço_etanol_3 - preço_etanol_1):.2f} em relação ao posto {posto_3}')
                print('-'*50)                
            if  etanol_2 < etanol_1 and etanol_2 < etanol_3:
                contador_etanol_2 += 1
                soma_etanol_2 += motorista_litros
                print(f'O posto com o etanol mais barato é o {posto_2} cujo preço é de R${(etanol_2):.2f}/L')
                print(f'O valor pago foi de R${(preço_etanol_2):.2f}')
                print(f'Você economizará R${(preço_etanol_1 - preço_etanol_2):.2f} em relação ao posto {posto_1}')
                print(f'Você economizará R${(preço_etanol_3 - preço_etanol_2):.2f} em relação ao posto {posto_3}')
                print('-'*50)                
            if etanol_3 < etanol_1 and etanol_3 < etanol_2:
                contador_etanol_3 += 1
                soma_etanol_3 += motorista_litros
                print(f'O posto com o etanol mais barato é o {posto_3} cujo preço é de R${(etanol_3):.2f}/L')
                print(f'O valor pago foi de R${(preço_etanol_3):.2f}')
                print(f'Você economizará R${(preço_etanol_1 - preço_etanol_3):.2f} em relação ao posto {posto_1}')
                print(f'Você economizará R${(preço_etanol_2 - preço_etanol_3):.2f} em relação ao posto {posto_2}')
                print('-'*50)                      
        if motorista_combustivel == 3:            
            if diesel_1 < diesel_2 and diesel_1 < diesel_3:
                contador_diesel_1 +=  1
                soma_diesel_1 += motorista_litros
                print(f'O posto com o diesel mais barato é o posto {posto_1} cujo preço é de R${(diesel_1):.2f}/L')
                print(f'O valor pago foi de R${(preço_diesel_1):.2f}')
                print(f'Você economizará R${(preço_diesel_2 - preço_diesel_1):.2f} em relação ao posto {posto_2}')
                print(f'Você economizará R${(preço_diesel_3 - preço_diesel_1):.2f} em relação ao posto {posto_3}')
                print('-'*50)                
            if diesel_2 < diesel_1 and diesel_2 < diesel_3:
                contador_diesel_2 +=  1
                soma_diesel_2 += motorista_litros
                print(f'O posto com o diesel mais barato é o posto {posto_2} cujo preço é de R${(diesel_2):.2f}/L')
                print(f'O valor pago foi de R${(preço_diesel_2):.2f}')
                print(f'Você economizará R${(preço_diesel_1 - preço_diesel_2):.2f} em relação ao posto {posto_1}')
                print(f'Você economizará R${(preço_diesel_3 - preço_diesel_2):.2f} em relação ao posto {posto_3}')
                print('-'*50)               
            if diesel_3 < diesel_1 and diesel_3 < diesel_2:
                contador_diesel_3 += 1
                soma_diesel_3 += motorista_litros
                print(f'O posto com o diesel mais barato é o posto {posto_3} cujo preço é de R${(diesel_3):.2f}/L')
                print(f'O valor pago foi de R${(preço_diesel_3):.2f}') 
                print(f'Você economizará R${(preço_diesel_1 - preço_diesel_3):.2f} em relação ao posto {posto_1}')
                print(f'Você economizará R${(preço_diesel_2 - preço_diesel_3):.2f} em relação ao posto {posto_2}')
                print('-'*50)                                                    
    if opçoes == 2:
        if contador == 0:
            print('Para usar essa opção, você deve preencher a primeira opção!')
            print('-'*50)
        else:
            print('')
            if motorista_combustivel == 1:            
                if gasolina_1 < gasolina_2 and gasolina_1 < gasolina_3:             
                    print(f'O posto com a gasolina mais barata é o posto {posto_1} cujo preço é de R${(gasolina_1):.2f}/L')
                    print(f'O valor pago foi de R${(preço_gasolina_1):.2f}')                
                    print('-'*50)                    
                if gasolina_2 < gasolina_1 and gasolina_2 < gasolina_3:                            
                    print(f'O posto com a gasolina mais barata é o {posto_2} cujo preço é de R${(gasolina_2):.2f}/L')
                    print(f'O valor pago foi de R${(preço_gasolina_2):.2f}')                
                    print('-'*50)                    
                if gasolina_3 < gasolina_1 and gasolina_3 < gasolina_2:                
                    print(f'O posto com a gasolina mais barata é o {posto_3} cujo preço é de R${(gasolina_3):.2f}/L')
                    print(f'O valor pago foi de R${(preço_gasolina_3):.2f}')                
                    print('-'*50)                    
            if motorista_combustivel == 2:            
                if etanol_1 < etanol_2 and etanol_1 < etanol_3:                
                    print(f'O posto com o etanol mais barato é o posto {posto_1} cujo preço é de R${(etanol_1):.2f}/L')
                    print(f'O valor pago foi de R${(preço_etanol_1):.2f}')                
                    print('-'*50)
                if  etanol_2 < etanol_1 and etanol_2 < etanol_3:                
                    print(f'O posto com o etanol mais barato é o {posto_2} cujo preço é de R${(etanol_2):.2f}/L')
                    print(f'O valor pago foi de R${(preço_etanol_2):.2f}')                
                    print('-'*50)
                if etanol_3 < etanol_1 and etanol_3 < etanol_2:                
                    print(f'O posto com o etanol mais barato é o {posto_3} cujo preço é de R${(etanol_3):.2f}/L')
                    print(f'O valor pago foi de R${(preço_etanol_3):.2f}')                
                    print('-'*50)
            if motorista_combustivel == 3:            
                if diesel_1 < diesel_2 and diesel_1 < diesel_3:                
                    print(f'O posto com o diesel mais barato é o posto {posto_1} cujo preço é de R${(diesel_1):.2f}/L')
                    print(f'O valor pago foi de R${(preço_diesel_1):.2f}')                
                    print('-'*50)
                if diesel_2 < diesel_1 and diesel_2 < diesel_3:                
                    print(f'O posto com o diesel mais barato é o posto {posto_2} cujo preço é de R${(diesel_2):.2f}/L')
                    print(f'O valor pago foi de R${(preço_diesel_2):.2f}')                
                    print('-'*50)
                if diesel_3 < diesel_1 and diesel_3 < diesel_2:                
                    print(f'O posto com o diesel mais barato é o posto {posto_3} cujo preço é de R${(diesel_3):.2f}/L')
                    print(f'O valor pago foi de R${(preço_diesel_3):.2f}')                 
                    print('-'*50)    
#COMENTÁRIO                 
    if opçoes == 3:
        print(f'Posto {posto_1}')
        print(f'Gasolina: R${gasolina_1:.2f}')
        print(f'Etanol: R${etanol_1:.2f}')   
        print(f'Diesel: R${diesel_1:.2f}\n')

        print(f'Posto {posto_2}')
        print(f'Gasolina: R${gasolina_2:.2f}')   
        print(f'Etanol: R${etanol_2:.2f}')   
        print(f'Diesel: R${diesel_2:.2f}\n')

        print(f'Posto {posto_3}')
        print(f'Gasolina: R${gasolina_3:.2f}')   
        print(f'Etanol: R${etanol_3:.2f}')   
        print(f'Diesel: R${diesel_3:.2f}')
        print('-'*50)             
    if opçoes == 4:
        print('Você escolheu sair do menu!\n')
        break
    
#RELATÓRIO
while True:
    if contador == 0:
        print('Para ler o relatório, você deve digitar valores na primeira opção.')
        break
    else:
        print('[1] SIM')
        print('[2] NÃO')
        relatorio = int(input('Deseja ler o relatório? '))        
        if relatorio == 1:
            print('')
            print(f'Quantidade de consultas realizadas no sistema: {contador}')
            print(f'Quantidade de vezes que o posto {posto_1} teve o menor valor de combustível: {contador_gasolina_1 + contador_etanol_1 + contador_diesel_1}')
            print(f'Quantidade de vezes que o posto {posto_2} teve o menor valor de combustível: {contador_gasolina_2 + contador_etanol_2 + contador_diesel_2}')
            print(f'Quantidade de vezes que o posto {posto_3} teve o menor valor de combustível: {contador_gasolina_3 + contador_etanol_3 + contador_diesel_3}')
            if (contador_gasolina_1 + contador_etanol_1 + contador_diesel_1) != 0:
                print(f'A média de litros consultados do posto {posto_1} foi de {((soma_gasolina_1 + soma_etanol_1 + soma_diesel_1)/(contador_gasolina_1 + contador_etanol_1 + contador_diesel_1)):.2f}')
            else:
                print(f'O posto {posto_1} não teve o menor valor em nenhuma consulta!')
            if (contador_gasolina_2 + contador_etanol_2 + contador_diesel_2) != 0:
                print(f'A média de litros consultados do posto {posto_2} foi de {((soma_gasolina_2 + soma_etanol_2 + soma_diesel_2)/(contador_gasolina_2 + contador_etanol_2 + contador_diesel_2)):.2f}')
            else:
                print(f'O posto {posto_2} não teve o menor valor em nenhuma consulta!')
            if (contador_gasolina_3 + contador_etanol_3 + contador_diesel_3) != 0:
                print(f'A média de litros consultados do posto {posto_3} foi de {((soma_gasolina_3 + soma_etanol_3 + soma_diesel_3)/(contador_gasolina_3 + contador_etanol_3 + contador_diesel_3)):.2f}')
            else:            
                print(f'O posto {posto_3} não teve o menor valor em nenhuma consulta!')
            maior_gasolina = gasolina_1    
            if gasolina_2 > gasolina_1 and gasolina_2 > gasolina_3:
                maior_gasolina = gasolina_2
            if gasolina_3 > gasolina_1 and gasolina_3 > gasolina_2:
                maior_gasolina = gasolina_3
            if maior_gasolina == gasolina_1:
                print(f'Posto com maior preço de gasolina: Posto {posto_1}')
                print(f'Preço: R${(maior_gasolina):.2f}/L')
            if maior_gasolina == gasolina_2:
                print(f'Posto com maior preço de gasolina: Posto {posto_2}')
                print(f'Preço: R${(maior_gasolina):.2f}/L')
            if maior_gasolina == gasolina_3:
                print(f'Posto com maior preço de gasolina: Posto {posto_3}')
                print(f'Preço: R${(maior_gasolina):.2f}/L')
            maior_etanol = etanol_1
            if etanol_2 > etanol_1 and etanol_2 > etanol_3:
                maior_etanol = etanol_2
            if etanol_3 > etanol_1 and etanol_3 > etanol_2:
                maior_etanol = etanol_3
            if maior_etanol == etanol_1:
               print(f'Posto com maior preço de etanol: Posto {posto_1}')
               print(f'Preço: R${(maior_etanol):.2f}/L')
            if maior_etanol == etanol_2:
                print(f'Posto com maior preço de etanol: Posto {posto_2}')
                print(f'Preço: R${(maior_etanol):.2f}/L')
            if maior_etanol == etanol_3:
                print(f'Posto com maior preço de etanol: Posto {posto_3}')
                print(f'Preço: R${(maior_etanol):.2f}/L')
            maior_diesel = diesel_1
            if diesel_2 > diesel_1 and diesel_2 > diesel_3:               
                maior_diesel = diesel_2
            if diesel_3 > diesel_1 and diesel_3 > diesel_2:
                maior_diesel = diesel_3
            if maior_diesel == diesel_1:
                print(f'Posto com maior preço de diesel: Posto {posto_1}')
                print(f'Preço: R${(maior_diesel):.2f}/L')
            if maior_diesel == diesel_2:
                print(f'Posto com maior preço de diesel: Posto {posto_2}')
                print(f'Preço: R${(maior_diesel):.2f}/L')
            if maior_diesel == diesel_3:
                print(f'Posto com maior preço de diesel: Posto {posto_3}')
                print(f'Preço: R${(maior_diesel):.2f}/L')
            menor_gasolina = gasolina_1    
            if gasolina_2 < gasolina_1 and gasolina_2 < gasolina_3:
                menor_gasolina = gasolina_2
            if gasolina_3 < gasolina_1 and gasolina_3 < gasolina_2:
                menor_gasolina = gasolina_3
            if menor_gasolina == gasolina_1:
                print(f'Posto com menor preço de gasolina: Posto {posto_1}')
                print(f'Preço: R${(menor_gasolina):.2f}/L')
            if menor_gasolina == gasolina_2:
                print(f'Posto com menor preço de gasolina: Posto {posto_2}')
                print(f'Preço: R${(menor_gasolina):.2f}/L')
            if menor_gasolina == gasolina_3:
                print(f'Posto com menor preço de gasolina: Posto {posto_3}')
                print(f'Preço: R${(menor_gasolina):.2f}/L')
            menor_etanol = etanol_1
            if etanol_2 < etanol_1 and etanol_2 < etanol_3:
                menor_etanol = etanol_2
            if etanol_3 < etanol_1 and etanol_3 < etanol_2:
                menor_etanol = etanol_3
            if menor_etanol == etanol_1:
               print(f'Posto com menor preço de etanol: Posto {posto_1}')
               print(f'Preço: R${(menor_etanol):.2f}/L')
            if menor_etanol == etanol_2:
                print(f'Posto com menor preço de etanol: Posto {posto_2}')
                print(f'Preço: R${(menor_etanol):.2f}/L')
            if menor_etanol == etanol_3:
                print(f'Posto com menor preço de etanol: Posto {posto_3}')
                print(f'Preço: R${(menor_etanol):.2f}/L')
            menor_diesel = diesel_1
            if diesel_2 < diesel_1 and diesel_2 < diesel_3:               
                menor_diesel = diesel_2
            if diesel_3 < diesel_1 and diesel_3 < diesel_2:
                menor_diesel = diesel_3
            if menor_diesel == diesel_1:
                print(f'Posto com menor preço de diesel: Posto {posto_1}')
                print(f'Preço: R${(menor_diesel):.2f}/L')
            if menor_diesel == diesel_2:
                print(f'Posto com menor preço de diesel: Posto {posto_2}')
                print(f'Preço: R${(menor_diesel):.2f}/L')
            if menor_diesel == diesel_3:
                print(f'Posto com menor preço de diesel: Posto {posto_3}')
                print(f'Preço: R${(menor_diesel):.2f}/L')
            break  
        elif relatorio == 2:
            print('Fechando o programa...')
            break
        else:
            print('Você não digitou corretamente, digite novamente!')
    


