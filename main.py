# interface para leitura de produtos e vendas


from os import system

compra = []
valores = [1, 2, 3.5, 5, 5, 2]




def leitura():
  print('''
     # PRODUTOS #   | # CÓDIGOS #
                    |
   Churros R$1,00   | 00
   Churros R$2,00   | 01
   Churros Gourmet  | 02 
   Batata Frita     | 03
   Porção de Pastel | 04
   Bebida           | 05
   
   ''')
  
  while True:

    print('''Digite o Código do Produto e a Quantidade:
    ''')


    codigo = int(input('Código: >>> '))
    quantidade = int(input('Quantidade: >>> '))

    calculo_compra(codigo, quantidade)
    print('')
    print('Deseja Adicionar um item?')
    adicionar_item = input('Digite S ou N: ').lower()
    
    if adicionar_item == 'n' or adicionar_item == 'não':
      break
    else:
      print()
  
  total_compra()    




def calculo_compra(codigo, quantidade):


  if codigo == 00:
    total = 1*quantidade

  elif codigo == 1 or codigo == 5:
    total = 2*quantidade

  elif codigo == 2:
    total = 3.5*quantidade

  elif codigo == 3 or codigo == 4:
    total = 5*quantidade

  compra.append(total)

  
def total_compra():
  system('clear')

  total = sum(compra)

  print('''
     TOTAL DA COMPRA 
     R$%.2f
     '''%total)



  print('Qual o valor recebido?') 
  
  valor_recebido = int(input('>>> '))
  
  

  troco = valor_recebido - total

  print('O troco é R$%.2f'%troco)

leitura()     