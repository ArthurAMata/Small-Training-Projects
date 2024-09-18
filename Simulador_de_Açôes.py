import time
import random

class Acao:
    def __init__(self,name,current_price):
        self.name = name
        self.current_price = current_price

    
    def __str__(self):
        return f'{self.name}'
    
def alter_value(acao):
    randomnum = random.randint(10,50)
    randomchoice = random.randint(1,2)
    if randomchoice == 1:
        acao.current_price += acao.current_price * randomnum/100
    else:
        acao.current_price -= acao.current_price * randomnum/100

portifolio = []
portifolio_fake = []
saldo = 100

facebook = Acao('facebook',10)
tesla = Acao('tesla',15)
microsoft = Acao('microsoft',50)
spacex = Acao('spacex',6)
chevrolet = Acao('chevrolet',10)
intel = Acao('intel',12)
apple = Acao('apple',40)


acoes = [facebook,tesla,microsoft,spacex,chevrolet,intel,apple]


while True:
    print('--------------------Mercado de ações------------------')
    print('Oque você quer fazer')
    print('1 Comprar uma ação ')
    print('2 Vender uma ação')
    print('3 conferir saldo')
    print('4 conferir portifólio')
    print('5 Fechar o mercado')
    try:
        option_menu_market = int(input(' '))
    except ValueError:
        print('Digite apenas números inteiros')
    except Exception:
        print('Algo deu errado')

    if option_menu_market == 1:
        for acao in acoes:
             print(f'Acao: {acao.name}, Valor: {acao.current_price}')
        buy = input('Qual o nome da ação que você quer comprar? ').lower()
        for acao in acoes:
            if acao.name == buy:
                if acao.current_price < saldo:
                    portifolio.append(acao)
                    portifolio_fake.append(acao.name)
                    saldo -= acao.current_price
                    time.sleep(1)
                else:
                    print('Você é pobre ')
                    time.sleep(1)

    if option_menu_market == 2:
        buy = input('Qual o nome da ação que você quer vender? ').lower()
        for acao in portifolio:
            if acao.name == buy:
                portifolio.remove(acao)
                portifolio_fake.remove(acao.name)
                saldo += acao.current_price
                time.sleep(1)

    if option_menu_market == 3:
        print(f'O seu saldo é: {round(saldo,2)}')
        time.sleep(1)

    if option_menu_market == 4:
         print(portifolio_fake)
         time.sleep(1)
    
    for i in range(7):
        alter_value(acoes[i])

    if option_menu_market == 5:
        break
