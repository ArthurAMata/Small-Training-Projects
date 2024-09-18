# -*- coding: utf-8 -*-

import time

import random

from collections import Counter

hu1 = 0
hu2 = 0
p1 = 0
p2 = 0
wq = 0
hq = 0
mq = 0

def verify_book_True(inventory_books_keys,book_verify):
    for i in inventory_books_keys:
                if i == book_verify:
                    return True
                else:
                    return False

potion_recipes = {
    'Felix Felices': {     #Aumenta a sorte
        'herb_use1': 'Aether', 
        'herb_use2': 'Madroerme',
        'p1': 'ap',  
        'p2': 'ap', 
        'water_q': 'pa', 
        'heat_q': 'fe',  
        'mix_q': 'mm'  
    },
    'Andorinha': {   #recupera a vida levemente
        'herb_use1': 'Dandelion', 
        'herb_use2': 'Madroerme',
        'p1': 'mp',  
        'p2': 'tp', 
        'water_q': 'ma', 
        'heat_q': 'el',  
        'mix_q': 'muim'  
    },
    'Aerondith': {  #permite mergulhar pela água sem precisar respirar durante o tempo do seu efeito e nadar é mais rápido
        'herb_use1': 'Lobo Branco',
        'herb_use2': 'Basilisco',
        'p1': 'tp',
        'p2': 'mp',
        'water_q': 'ta',
        'heat_q': 'fe',
        'mix_q': 'muim'
    },
    'Papa Figo': {  #aumente a imudade e resistencia a venenos alimentos e etc
        'herb_use1': 'Albedo',
        'herb_use2': 'Nevasca',
        'p1': 'ap',
        'p2': 'tp',
        'water_q': 'ma',
        'heat_q': 'cb',                                                     
        'mix_q': 'mm'
    },
    'Rouba-Ovelha': {   #deixa mais rápido só que em troca de energia
        'herb_use1': 'Dandelion',
        'herb_use2': 'Fungus',
        'p1': 'mp',
        'p2': 'ap',
        'water_q': 'pa',
        'heat_q': 'el',
        'mix_q': 'mp'
    },
    'Dreamfyre': {      #calor n afeta mais o usuário durante o efeito 
        'herb_use1': 'Basilisco',
        'herb_use2': 'Fungus',
        'p1': 'ap',
        'p2': 'mp',
        'water_q': 'ta',
        'heat_q': 'cb',
        'mix_q': 'mm'
    },
    'Gato Branco': {    #permite enxergar no escuro só que em preto e branco
        'herb_use1': 'Cactacida',
        'herb_use2': 'Cáscara',
        'p1': 'tp',
        'p2': 'mp',
        'water_q': 'ma',
        'heat_q': 'el',
        'mix_q': 'mp'
    },
    'Trovoada': {   #aumenta a força e resistência
        'herb_use1': 'Fungus',
        'herb_use2': 'Albedo',
        'p1': 'ap',
        'p2': 'mp',
        'water_q': 'pa',
        'heat_q': 'cb',
        'mix_q': 'mm'
    },
    'Djistka_seca': {   #o usuário enxerga fontes de energia mágicas
        'herb_use1': 'Nevasca',
        'herb_use2': 'Fungus',
        'p1': 'ap',
        'p2': 'mp',
        'water_q': 'pa',
        'heat_q': 'el',
        'mix_q': 'mp'
    },
    'Nekker': { #o usuario é imune a oufato ee animais
        'herb_use1': 'Cactacida',
        'herb_use2': 'Nevasca',
        'p1': 'tp',
        'p2': 'mp',
        'water_q': 'ma',
        'heat_q': 'cb',
        'mix_q': 'mm'
    },
    'Raffard': { # surto de energia em rtoca de um canssaço pós uso
        'herb_use1': 'Madroerme',
        'herb_use2': 'Dandelion',
        'p1': 'ap',
        'p2': 'tp',
        'water_q': 'pa',
        'heat_q': 'fe',
        'mix_q': 'muim'
    },
    'Bosque_de_Maribor': { #permite o usuário identificar  pegada e manchas muito mais fácilmente
        'herb_use1': 'Aether',
        'herb_use2': 'Albedo',
        'p1': 'mp',
        'p2': 'ap',
        'water_q': 'ma',
        'heat_q': 'cb',
        'mix_q': 'mm'
    },
    'Coruja': { #também permite uma visão no escuro porém apenas ao escuro da noite
        'herb_use1': 'Nevasca',
        'herb_use2': 'Dandelion',
        'p1': 'ap',
        'p2': 'tp',
        'water_q': 'pa',
        'heat_q': 'el',
        'mix_q': 'mp'
    },
    'Colmeia': {  #o usuário escuta melhor
        'herb_use1': 'Fungus',
        'herb_use2': 'Aether',
        'p1': 'tp',
        'p2': 'ap',
        'water_q': 'ma',
        'heat_q': 'cb',
        'mix_q': 'muim'
    },
    'Samun': {  #resitencia alta a explosões
        'herb_use1': 'Albedo',
        'herb_use2': 'Basilisco',
        'p1': 'ap',
        'p2': 'mp',
        'water_q': 'pa',
        'heat_q': 'el',
        'mix_q': 'mm'
    },
    'Nevasca': {  #deixa a percepção de tempo mais devagar
        'herb_use1': 'Nevasca',
        'herb_use2': 'Cáscara',
        'p1': 'tp',
        'p2': 'mp',
        'water_q': 'ma',
        'heat_q': 'fe',
        'mix_q': 'mp'
    },
    'Tir_na_Lia': {      #cura machucados e dores leves 
        'herb_use1': 'Dandelion',
        'herb_use2': 'Cactacida',
        'p1': 'ap',
        'p2': 'mp',
        'water_q': 'pa',
        'heat_q': 'cb',
        'mix_q': 'mm'
    },
    'Lua_Cheia': {  #o usuário n precisa dormir durante o efeito
        'herb_use1': 'Basilisco',
        'herb_use2': 'Fungus',
        'p1': 'tp',
        'p2': 'ap',
        'water_q': 'ma',
        'heat_q': 'el',
        'mix_q': 'muim'
    },
    'Sonho_do_Dragao': {    #imune a queimadura e fogo por um curto período de tempo
        'herb_use1': 'Aether',
        'herb_use2': 'Dandelion',
        'p1': 'ap',
        'p2': 'mp',
        'water_q': 'ta',
        'heat_q': 'fe',
        'mix_q': 'mm'
    },
    'Alcohest': {   #só tem um cheiro muito ruim
        'herb_use1': 'Madroerme',
        'herb_use2': 'Nevasca',
        'p1': 'mp',
        'p2': 'tp',
        'water_q': 'pa',
        'heat_q': 'cb',
        'mix_q': 'muim'
    },
    'Felina': {         #vc n emite mais sons
        'herb_use1': 'Gato',
        'herb_use2': 'Fungus',
        'p1': 'ap',
        'p2': 'mp',
        'water_q': 'pa',
        'heat_q': 'el',
        'mix_q': 'mp'
    },
    'Arquigrifo': {         #o usuário é resistente a veneno 
        'herb_use1': 'Mandrágora',
        'herb_use2': 'Nevasca',
        'p1': 'tp',
        'p2': 'ap',
        'water_q': 'ma',
        'heat_q': 'cb',
        'mix_q': 'mm'
    },
    'Lupina': {     #surto de energia temporários
        'herb_use1': 'Melancolia',
        'herb_use2': 'Cactacida',
        'p1': 'mp',
        'p2': 'ap',
        'water_q': 'pa',
        'heat_q': 'fe',
        'mix_q': 'muim'
    },
    'Ursídea': {    #aumenta a resitencia a poções completamente
        'herb_use1': 'Fogo de Dragão',
        'herb_use2': 'Fungus',
        'p1': 'ap',
        'p2': 'mp',
        'water_q': 'ma',
        'heat_q': 'cb',
        'mix_q': 'mm'
    },
    'Liche_Ancião': {      #semi invisibilidade
        'herb_use1': 'Draconis',
        'herb_use2': 'Nevasca',
        'p1': 'tp',
        'p2': 'ap',
        'water_q': 'pa',
        'heat_q': 'el',
        'mix_q': 'mp'
    },
    'Pó de Lua': {          #revela a localização de 1 pessoa naquele momento
        'herb_use1': 'Múmia',
        'herb_use2': 'Aether',
        'p1': 'ap',
        'p2': 'tp',
        'water_q': 'ma',
        'heat_q': 'fe',
        'mix_q': 'mm'
    },
    'Vento do Norte': {     #frio n será mais um problema
        'herb_use1': 'Cactacida',
        'herb_use2': 'Gato',
        'p1': 'tp',
        'p2': 'mp',
        'water_q': 'pa',
        'heat_q': 'cb',
        'mix_q': 'muim'
    },
    'Unicórnio Negro': {        #venenos agora curam
        'herb_use1': 'Dandelion',
        'herb_use2': 'Mandrágora',
        'p1': 'ap',
        'p2': 'mp',
        'water_q': 'pa',
        'heat_q': 'el',
        'mix_q': 'mm'
    },
    'Dor na Consciência': {         #o tempo retrocede em 1 minuto
        'herb_use1': 'Fungus',
        'herb_use2': 'Melancolia',
        'p1': 'tp',
        'p2': 'ap',
        'water_q': 'ma',
        'heat_q': 'cb',
        'mix_q': 'mp'
    },
    'Rosa de Shaerawed': {      #permite que qualquer planta cresça mais rápido(n é pra beber)
        'herb_use1': 'Nevasca',
        'herb_use2': 'Gato',
        'p1': 'mp',
        'p2': 'ap',
        'water_q': 'pa',
        'heat_q': 'el',
        'mix_q': 'mm'
    },
    'Víbora': {         #venenos n são mais um problema
        'herb_use1': 'Aether',
        'herb_use2': 'Fungus',
        'p1': 'ap',
        'p2': 'mp',
        'water_q': 'ma',
        'heat_q': 'fe',
        'mix_q': 'muim'
    },
    'Zirael': {     #mostra o caminho para onde quer ir ou oque vc quer achar
        'herb_use1': 'Lobo Branco',
        'herb_use2': 'Basilisco',
        'p1': 'tp',
        'p2': 'tp',
        'water_q': 'pa',
        'heat_q': 'fe',
        'mix_q': 'mm'
    },
    'Rívia':{   # todos os sentidos aumentados extremamente
        'herb_use1': 'Lobo Branco',
        'herb_use2': 'Lobo Branco',
        'p1': 'tp',
        'p2': 'ap',
        'water_q': 'pa',
        'heat_q': 'cb',
        'mix_q': 'mm'
    }

}

pot_upgrade = 0

appearences =  [
    "Um homem alto e encurvado, com longos cabelos brancos e uma capa de pele de lobo, suas mãos estão cheias de cicatrizes e seus olhos refletem uma experiência amarga.",
    "Uma mulher de meia-idade com vestes negras e olhos azuis brilhantes, exalando uma aura misteriosa. Seu cabelo curto e grisalho está preso por uma tiara de prata simples.",
    "Um cavaleiro corpulento de armadura desgastada, com uma grande cicatriz atravessando seu rosto. Ele carrega uma espada gigante nas costas e sua expressão é sempre severa.",
    "Um jovem mago de aspecto esquelético, envolto em mantos verdes com símbolos arcanos bordados. Sua pele é pálida como a neve e seus olhos irradiam uma energia sobrenatural.",
    "Uma camponesa robusta com mãos calejadas e cabelo embaraçado, seu rosto está sujo de terra e ela veste um avental rasgado, mas seus olhos brilham com determinação.",
    "Um caçador de aparência selvagem, com barba espessa e desgrenhada. Sua armadura de couro está coberta de sangue seco e ele carrega várias peles de animais em seu ombro.",
    "Uma guerreira nórdica alta e musculosa, com uma grande tatuagem de dragão em seu braço. Seu cabelo loiro está preso em tranças e ela carrega um machado gigante à sua cintura.",
    "Um alquimista velho e manco, com uma longa barba grisalha e olhos que parecem enxergar além do presente. Ele carrega um pequeno saco de couro cheio de frascos e ingredientes.",
    "Um nobre de cabelos curtos e castanhos, com roupas luxuosas adornadas com peles de arminho e joias douradas. Ele anda com um ar de superioridade e fala de forma altiva.",
    "Um mercenário de pele morena, com várias cicatrizes pelo corpo. Ele veste uma armadura leve de couro e tem um olhar desconfiado, sempre segurando o cabo de sua espada.",
    "Uma sacerdotisa de olhos verdes penetrantes, vestida com um manto dourado decorado com símbolos antigos. Ela segura um cajado entalhado com runas brilhantes.",
    "Um bardo de cabelo castanho desgrenhado, vestindo roupas coloridas e um chapéu adornado com penas. Ele carrega um alaúde e seus olhos dançam com um brilho de travessura.",
    "Um homem robusto, com a barba por fazer e uma cicatriz que atravessa seu olho direito. Ele veste uma armadura de ferro pesada e carrega um martelo de guerra gigante.",
    "Uma elfa de traços delicados e pele clara, com longos cabelos dourados. Ela veste uma armadura leve de couro e carrega um arco de madeira ancestral nas costas.",
    "Um mercador gordo e suado, com um sorriso suspeito. Ele veste roupas extravagantes e carrega um saco de moedas preso ao cinto, sempre atento a possíveis oportunidades.",
    "Uma feiticeira de pele pálida, com longos cabelos pretos e olhos vermelhos como fogo. Suas vestes são negras e cheias de símbolos misteriosos, e ela sempre parece sussurrar palavras arcanas.",
    "Um soldado veterano de rosto endurecido, com um elmo amassado de metal e uma armadura surrada. Seu olhar é sombrio, refletindo anos de batalhas sangrentas.",
    "Uma ladina de estatura baixa e ágil, com um capuz que cobre seu rosto. Ela veste roupas escuras e carrega várias lâminas escondidas em seu cinto."
]

thks_aswers = [
    "Muito obrigado, você salvou o meu dia!",
    "Agradeço imensamente, estava realmente precisando.",
    "Essa poção é exatamente o que eu procurava, muito grato!",
    "Não sei o que faria sem sua ajuda. Obrigado!",
    "Você é um verdadeiro mestre alquimista, obrigado!",
    "Minhas preces foram atendidas, sou eternamente grato!",
    "Com isso, posso seguir em frente. Obrigado de coração.",
    "Finalmente, uma solução! Meus agradecimentos.",
    "Você tem um talento raro, muito obrigado!",
    "Nunca pensei que encontraria uma poção dessas, muito obrigado!",
    "Agora posso continuar minha jornada, agradeço muito!",
    "Você é uma verdadeira bênção, agradeço profundamente!",
    "Isso foi mais do que esperava, obrigado mesmo!",
    "Sua poção veio na hora certa, meus sinceros agradecimentos!",
    "Agora sim, posso enfrentar qualquer coisa! Obrigado!",
    "Você me surpreendeu! Grato pela poção.",
    "Essa é uma poção poderosa, grato pela sua habilidade.",
    "Inacreditável! Obrigado por me ajudar com essa."
]


problems = {
    'Estou com dor de cabeça a 3 dias me ajude' : 'Andorinha',
    'Me machuquei depois de um batalha' : 'Andorinha',
    'Um monstro me atacou' : 'Andorinha',
    'Me machuquei depois de um batalha' : 'Andorinha',
    'Me machuquei depois de um batalha' : 'Andorinha',
    'Me machuquei depois de um batalha' : 'Andorinha',
    'Me machuquei depois de um batalha' : 'Andorinha',
    'Estou com dor de cabeça a 3 dias me ajude' : 'Andorinha',
    'Estou com dor de cabeça a 3 dias me ajude' : 'Andorinha',
    'Estou com dor no corpo inteiro a 3 dias me ajude' : 'Andorinha',
    'Meu estômago está revirando depois de comer cogumelos estranhos.': 'Papa Figo',
    'Preciso aumentar minha força para carregar uma espada gigante.': 'Trovoada',
    'vou entrar numa caverna para encontrar algo que eu perdi.': 'Gato Branco',
    'Estou congelando de frio , preciso de algo rápido': 'Vento do Norte',
    'vou para o deserto para encontrar um amigo': 'Dreamfyre',
    'preciso de um dente de um tubarão que vive no fundo da água para minha coleção.': 'Aerondith',
    'preciso abrir um buraco em uma parede mas tenho medo de me machucar com a explosão': 'Samun',
    'Preciso subir uma montanha e algo para caso eu me machuque': 'Andorinha',
    'Estou prestes a lutar contra um urso que está aterrorizando os arredores, preciso de resistência extra.': 'Trovoada',
    'Fui envenenado por um espião, preciso de um antídoto': 'Víbora',
    'Acabei de sair de uma luta, preciso me curar rapidamente.': 'Tir_na_Lia',
    'Preciso entregar uma mensagem,muito rápido': 'Rouba-Ovelha',
    'Sinto que estou sendo seguido, preciso ver nas sombras.': 'Gato Branco',
    'Estou investigando um assassinato, preciso ver as coisas com mais detalhes.': 'Bosque_de_Maribor',
    'Preciso passar despercebido pelos guardas,Não me pergunte o porque.': 'Felina',
    'Preciso escutar as conversas do conselho, mas estão longe.': 'Colmeia',
    'Renho que lutar em uma batalha por horas sem me cansar': 'Raffard',
    'Preciso testar algo que pode ser perigoso caso algo errado aconteça como reverto oque eu fiz caso de errado': 'Dor na Consciência',
    'Minha casa pegou fogo e quase morri, quero estar previnido caso aconteça de novo': 'Sonho_do_Dragao',
    'Preciso que meu jardim cresca rápido é com ele que ganho dinheiro': 'Rosa de Shaerawed',
}

inventory_books_keys = [
    'Nota do velho alquimista'
]

inventory_books_values = [
    'A maioria das pessoas me pagam para eu curar uma leve dor de cabeça ou \nter algo para se curar caso um animal da floresta ataque elas e na maioria\n das vezes eu vendo uma poção que deve ser a que eu mais faço, \neu não lembro o nome dela mas é so pegar um dandelion de\n jardim massacrar ele depois triturar um daquele cogumelos de esgoto\n Madroerme ,adicionar metade do vidro de água e deixar esquentar rápidamente\n não mais que Isso depois misture até a mão cansar e pronto\n OBS:Já deixei algumas ervas no saco de ervas de reserva'
]

inventory_books_it = ['x']

def get_potion(herb_use1, herb_use2, pilao_q1, pilao_q2, water_q, heat_q, mix_q, inventory_potions):
    for potion_name, recipe in potion_recipes.items():
        if (herb_use1 == recipe['herb_use1'] and
            herb_use2 == recipe['herb_use2'] and
            pilao_q1 == recipe['p1'] and
            pilao_q2 == recipe['p2'] and
            water_q == recipe['water_q'] and
            heat_q == recipe['heat_q'] and
            mix_q == recipe['mix_q']):
            print(f'Parabéns, você criou a poção {potion_name}!')
            if  potion_name in inventory_learned_potions:
                pass
            else:
                inventory_learned_potions.append(potion_name)
            inventory_potions.append(potion_name)
            return
    print("A combinação de ingredientes e quantidades não resultou em uma poção conhecida.")

def herbs_spawn():

    collected_herbs = []

    
    num_herbs = 3


    for _ in range(num_herbs):

        probabilities = [1 / (i + 1) for i in range(len(ordem_raridade))]
        total_prob = sum(probabilities)
        probabilities = [p / total_prob for p in probabilities]  
        selected_herb = random.choices(ordem_raridade, probabilities)[0]
        collected_herbs.append(selected_herb)
    
    return collected_herbs

def verify_learned_herb(inventory, potion_name):
    if potion_name not in potion_recipes:
        return False
    recipe = potion_recipes[potion_name]
    required_herbs = {
        recipe['herb_use1']: 1,
        recipe['herb_use2']: 1
    }
    for herb, count in required_herbs.items():
        if inventory.count(herb) < count:
            return False
    for herb, count in required_herbs.items():
        for _ in range(count):
            inventory.remove(herb)
    return True

stamina = 150

money = 0
learned_potions_herb1 = []
learned_potions_herb2 = []

life = 100
luck = 10

inventory_learned_potions = []

inventory = ['Madroerme','Madroerme','Madroerme','Dandelion','Dandelion','Dandelion']

inventory_potions = []

ordem_raridade = [
    'Fungus',
    'Dandelion',
    'Madroerme',
    'Cáscara',
    'Albedo',
    'Cactacida',
    'Nevasca',
    'Múmia',
    'Draconis',
    'Fogo de Dragão',
    'Melancolia',
    'Grão de Areia',
    'Mandrágora',
    'Gato',
    'Espinho',
    'Luz da Aurora',
    'Arenária',
    'Aether',
    'Basilisco',
    'Lobo Branco'
]
pot = []

dick_ervas = {
    'Arenária' : 'Flor branca com miolo amarelo e forte cheiro de grama normalmente misturada com alcool para reduzir a dor',
    'Luz da Aurora': 'Erva com flores que emitem uma luz suave. Usada para poções de esclarecimento e percepção.',
    'Espinho': 'Planta com folhas espinhosas e aroma intenso. Usada para poções de defesa.',
    'Gato': 'Erva com folhas largas e macias, de um verde intenso. Usada para preparar poções de agilidade.',
    'Mandrágora': 'Planta rara com raízes que emitem um som agudo quando arrancadas. Conhecida por suas propriedades mágicas.',
    'Grão de Areia': 'Erva com sementes finas que ajudam a fortalecer as defesas do usuário.',
    'Melancolia': 'Planta com flores pálidas que normalmente usada em óleos de espada.',
    'Fogo de Dragão': 'Planta com folhas vermelhas e flamejantes, usada para poções de resistência ao fogo.',
    'Draconis': 'Raiz com cor avermelhada e propriedades que aumentam a força física temporariamente.',
    'Múmia': 'Erva com aparência desidratada, com propriedades que ajudam na recuperação de vitalidade.',
    'Aether': 'Erva mágica de cor azul brilhante, com folhas etéreas e translúcidas.',
    'Albedo': 'Planta com flores brancas e pétalas delicadas, cresce em áreas úmidas.',
    'Basilisco': 'Erva de folhas largas e verdes escuras, com um aroma intenso e apimentado.',
    'Cactacida': 'Cogumelo com uma base espinhosa e cor de cacto, encontrado em ambientes secos.',
    'Dandelion': 'Planta com flores amarelas brilhantes, conhecida por suas sementes voadoras.',
    'Fungus': 'Cogumelo marrom escuro e carnudo, cresce em locais sombreados e úmidos.',
    'Madroerme': 'Raiz de aparência retorcida e folhas largas, com um cheiro forte e penetrante.',
    'Cáscara': 'Cogumelo pequeno e vermelho, frequentemente encontrado em áreas sombrias.',
    'Nevasca': 'Planta com flores brancas e frágeis, resistente ao frio e encontrada em locais nevados.',
    'Lobo Branco': 'Planta com folhas largas e prateadas, conhecida por seu uso em poções de combate.',
}
print('Bem-vindo à cabana do alquimista! Você chega e vê uma cabana velha e mofada. Andando e explorando mais, você apenas encontra um caldeirão, um fole, uma garrafa de água, um pilão e uma colher de madeira. Junto, você encontra um livro empoeirado. O que você faz?')
time.sleep(1)
print('1 - Abrir o livro (entrar no tutorial)')
print('2 - Jogar o livro fora (pular tutorial)')
time.sleep(1)
try:
    option_tuto = int(input(' '))
except ValueError:
    print('Algo deu errado')
    exit()
if option_tuto == 1:
    print('ᛏᚺ ᚨᚾᚲᛁᛖ ᛗᚨᚾᚲ ᛟᚱᛋᛏ ᚨᚾᚲ ᚠᚨᚾᛏᚺ ᚨᚾᚲᛁᛖ ᛗᚨᚾᚲ ᛟᚱᛋᛏ ᚨᚾᚲ ᚠᚨᚨᚾᚲ ᚠᚨᚾᛏᚺ ᚨᚾᚲᚨᚾᚲ ᚠᚨᚾᛏᚺ ᚨᚾᚲᚨᚾᚲᛁᛖ ᛗᚨᚾᚲ ᛟᚱᛋᛏ ᚨᚾᚲ ᚠᚨᚾᛏᚺᚾᚲ ᚠᚨᚾ ᚠᛏᚺ ᚨᚾᚲᚾᚲ ᚷᚨᚾᚲᛁᛖ ᛗᚨᚾᚲ ᛟᚱᛋᛏ ᚨᚾᚲ ᚠᚨᚾᛏᚺᚾᚲᛁᛖ ᛗᚨᚾᚲ ᛟᚱᛋᛏ ᚨᚾᚲ ᚠᚨᚾᛏᚺᚾᚲᛁᛖ ᛗᚨᚾᚲ ᛟᚱᛋᛏ ᚨᚾᚲ ᚠ ᚠ ᚷᚨᚾᛟ')
    time.sleep(1)
    print('Livro errado. Você abre o livro ao lado e lê: "O caldeirão será a base onde você jogará as ervas e água para criar alguma poção. O fole será o quanto você esquentará a sua mistura e a colher o quanto você vai misturar, e o pilão a força da sua poção. Misture e seja criativo para ver o que você vai fazer. (BOA SORTE)"')
    time.sleep(1)
    print('Tente entrar na cabena primeiro tem algo pra vc na biblioteca empoeirada')
    time.sleep(1)
while True:
    print('======== MENU =======')
    print('1 - Entrar na cabana')
    print('2 - Sair para explorar e pegar ervas')
    print('3 - Sair para vender suas poções')
    print('4 - conferir saca de poções')
    print('5 - Loja do tobias')
    print('6 - Conferir saco de moedas')

    try:
        option_menu = int(input(' '))
    except ValueError:
        print('Algo deu errado')
        exit()

    if option_menu == 1:
        if len(inventory) == 0:
            print('Você não tem ervas. Vá buscar algumas.')
        else:
            while True:
                print('------------MENU CABANA----------')
                print('1 Dormir')
                print('2 cozinhar')
                print('3 conferir saco de poções')
                print('4 Conferir saco de ervas')
                print('5 Ver biblioteca empoeirada')
                print('6 Sair da cabana')
                if pot_upgrade == True:
                    print('7 Preparar automáticamente')
                else:
                    pass
                try:
                    option_hut = int(input(' '))
                except Exception:
                    print('Algo deu errado')
                if option_hut == 1:
                    print('VC deita e descansa')
                    time.sleep(1)
                    print('01:00')
                    time.sleep(1)
                    print('02:00')
                    time.sleep(1)
                    print('03:00')
                    time.sleep(1)
                    print('04:00')
                    time.sleep(1)
                    print('05:00')
                    time.sleep(1)
                    print('06:00')
                    stamina += 100

                elif option_hut == 2:
                    print('Vc entra na cozinha e encontra seus instrumentos de trabalho')
                    time.sleep(1)
                    index_it_hut = 0
                    for i in inventory:
                        print(f'{index_it_hut} {i}')
                        index_it_hut += 1
                    herb_use1_index = int(input('Primeiro escolha uma erva para colocar'))
                    herb_use1 = inventory[herb_use1_index]
                    inventory.remove(herb_use1)
                    time.sleep(1.5)
                    print('agora vc pega o seu pilão e decide?')
                    print('1 amassar a erva')
                    print('2 massacrar a erva')
                    print('3 triturar a erva')
                    option_pilao_herb = int(input(' '))
                    pilao_q1 = 0
                    if option_pilao_herb == 1:
                        pilao_q1 = 'ap'
                    elif option_pilao_herb == 2:
                        pilao_q1 = 'mp'
                    else:
                        pilao_q1 = 'tp'
                    time.sleep(1)
                    index_it_hut = 0
                    for i in inventory:
                        print(f'{index_it_hut} {i}')
                        index_it_hut += 1
                    herb_use2_index =int(input('agora escolha uma outra erva para colocar'))
                    herb_use2 = inventory[herb_use2_index]
                    inventory.remove(herb_use2)
                    time.sleep(1.5)
                    print('agora vc pega o seu pilão e decide?')
                    print('1 amassar a erva')
                    print('2 massacrar a erva')
                    print('3 triturar a erva')
                    option_pilao_herb = int(input(' '))
                    pilao_q2 = 0
                    if option_pilao_herb == 1:
                        pilao_q2 = 'ap'
                    elif option_pilao_herb == 2:
                        pilao_q2 = 'mp'
                    else:
                        pilao_q2 = 'tp'
                    time.sleep(1)
                    print('ótimo agora vc pega a água e pensa o qunato vai adicionar')
                    print('1 adicionar pouca água')
                    print('2 adicionar metade da água')
                    print('3 virar o vidro de água')
                    option_add_water = int(input(' '))
                    water_q = 0
                    if option_add_water == 1:
                        water_q = 'pa'
                    elif option_add_water == 2:
                        water_q = 'ma'
                    else:
                        water_q = 'ta'
                    time.sleep(1)
                    print('Quase no final hora de aquecer a mistura,vc joga lenha no forno e se prepara para atiçar o fogo')
                    print('1 apenas esquentar levemente')
                    print('2 criar leves bolhas na mistura')
                    print('3 ferver')
                    option_heat = int(input(' '))
                    heat_q = 0
                    if  option_heat == 1:
                        heat_q = 'el'
                    elif option_heat == 2:
                        heat_q = 'cb'
                    else:
                        heat_q = 'fe'
                    time.sleep(1)
                    print('Por último misture com a colher')
                    print('1 misturar pouco')
                    print('2 misturar medio')
                    print('3 misturar muito')
                    option_mix = int(input(' '))
                    mix_q = 0
                    if  option_mix == 1:
                        mix_q = 'mp'
                    elif option_mix == 2:
                        mix_q = 'mm'
                    else:
                        mix_q = 'muim'
                    time.sleep(1)
                    get_potion(herb_use1, herb_use2, pilao_q1, pilao_q2, water_q, heat_q, mix_q, inventory_potions)
                
                elif option_hut == 3:
                    print(inventory_potions)
                    
                elif option_hut == 4:
                    print(inventory)
                
                elif option_hut == 5:
                    print('Você olha a velha estante de livos e escolhe')
                    index_it_book = 0
                    for i in inventory_books_keys:
                        print(f'{index_it_book} -- {inventory_books_keys[index_it_book]}')
                        index_it_book += 1
                    book_use_index =int(input('Qual livro você vai ler'))

                    it_it = len(inventory_books_keys) - 1
                    print((inventory_books_values[it_it])) 
                
                elif option_hut == 6:
                    print('Você sai par o ar livre')
                    break

                elif option_hut == 7:
                    if pot_upgrade == True:
                        index_it_auto = 0
                        for i in inventory_learned_potions:
                            print(f'{index_it_auto} {i}')
                            index_it_auto += 1
                        auto_use_index = int(input('Escolha uma poção para produzir(apenas as que vc já produziu)'))
                        auto_use = inventory_learned_potions[auto_use_index]
                        if  verify_learned_herb(inventory, auto_use):
                            print("Iniciando o processo de criação da poção...")
                            time.sleep(1)
                            print("Reunindo os ingredientes ...")
                            time.sleep(1.5)
                            print("Triturando as ervas raras e os componentes secretos...")
                            time.sleep(1)
                            print("Adicionando água à mistura...")
                            time.sleep(1)
                            print("Aquecendo lentamente o caldeirão...")
                            time.sleep(1)
                            print("Misturando cuidadosamente os ingredientes...")
                            time.sleep(1)
                            print("A chama começa a intensificar, a poção está ganhando forma...")
                            time.sleep(1.5)
                            print("Um brilho suave começa a surgir do caldeirão...")
                            time.sleep(2)
                            print("O aroma da poção toma conta do ambiente, o poder está quase completo...")
                            time.sleep(1.5)
                            print("A poção está pronta!.")
                            time.sleep(1)
                            print(f'Parabéns, você criou a poção {auto_use}!')
                            inventory_potions.append(auto_use)
                        else:
                            print('Vc  n tem as ervas necessárias')

                    else:
                        print('Algo deu errado')

    elif option_menu == 2:
        if stamina >= 50:
            novas_ervas = herbs_spawn()
            inventory.extend(novas_ervas)
            contagem_ervas = Counter(inventory)
            stamina -= 50
            print('Você encontrou as seguintes ervas:')
            for erva, quantidade in contagem_ervas.items():
                descricao = dick_ervas.get(erva, 'Descrição não encontrada.')
                print(f'{quantidade}x {erva}: {descricao}')
        else:
            print('Você está com pouca stamina para explorar. Descanse um pouco.')

    elif option_menu == 3:
        if len(inventory_potions) == 0:
            print('Você não tem poções para vender.')
        else:
            problem_statement, required_potion = random.choice(list(problems.items()))
            person_appearence = random.choice(list(appearences))
            print(f'{person_appearence}: "{problem_statement}"')
            print('Você possui as seguintes poções para vender:')
            for idx, potion in enumerate(inventory_potions):
                print(f'{idx} - {potion}')
            try:
                selected_potion_index = int(input('Escolha o índice da poção para oferecer: '))
                if 0 <= selected_potion_index < len(inventory_potions):
                    selected_potion = inventory_potions[selected_potion_index]
                    if selected_potion == required_potion:
                        num_reward = random.randint(30,60)
                        reward = 3 * num_reward  
                        thks_aswer = random.choice(list(thks_aswers))
                        print(f'A pessa diz : {thks_aswer} "{required_potion}".')
                        print(f'Você ganhou {reward} moedas!')
                        money += reward
                    else:
                        num_reward = random.randint(30,60)
                        reward = num_reward/3 
                        print(f'Infelizmente, a pessoa estava procurando por outra poção.')
                        print(f'Você ganhou {reward} moedas.')
                        money += reward
                    inventory_potions.pop(selected_potion_index)
                else:
                    print('Índice de poção inválido.')
            except ValueError:
                print('Entrada inválida. Por favor, insira um número válido.')

    elif option_menu == 4:
            if len(inventory_potions) == 0:
                print('Você n tem poções')
            else:
                print(inventory_potions)


    elif option_menu == 5:
        print('Você chegou na loja do tobias, ele conhecia o velho alquimista \n e roubou todos os livros de receitas dele e agora ele te vende em um velho balcão\n de madeira por preços exorbitantes')
        print('+++++++++++Balcão do tobias++++++++++')
        print('1 livro do andarilho solitário  $200')
        print('2 livro do explorador de cavernas $800')
        print('3 tomo do caçador de monstros $1500')
        print('4 livro do imperador dos 7 reinos $2500')
        print('5 caldeirão modificado do velho alquimista $5000') #fazer isso aí e fazer ,as coisas da loja
        
        print('X - Sair da loja')
        if len(inventory_books_it) == 5:
            print('6 tomo do velho alquimista')
        else:
            pass
        option_book_buy = input(' ')
        if option_book_buy == '1':
            book_verify = 'livro do andarilho solitário'
            verify_book_True(inventory_books_keys,book_verify)
            if verify_book_True == True:
                break
            else:    
                if money >= 200:
                    inventory_books_keys.append('livro do andarilho solitário')
                    inventory_books_values.append("""
Felix Felices: A maioria das pessoas busca um pouco de sorte \n nas apostas ou nas caçadas, e eu tenho a solução perfeita. \n Para preparar essa poção, comece pegando um Aether fresco. \n Amassá-lo bem com o pilão é o primeiro passo. \n Em seguida, pegue um Madroerme, e amasse-o também até formar \n uma pasta homogênea. Agora, adicione metade de um vidro \n de água pura à mistura. O segredo está no aquecimento: \n aqueça rapidamente, sem deixar ferver. Misture vigorosamente \n até seus braços cansarem, e pronto. Um gole dessa poção \n e a sorte estará ao seu lado.
                                                  
Papa Figo: Se você quer resistir a venenos ou alimentos suspeitos, \n essa poção é a ideal. Primeiro, pegue um Albedo e amasse-o \n com cuidado até extrair todo seu potencial. Depois, \n adicione uma Nevasca e triture-a bem até virar pó. Agora, \n adicione metade de um frasco de água pura. Aqueça lentamente, \n só até começar a formar pequenas bolhas. Misture até obter \n uma textura uniforme. Essa poção vai aumentar sua imunidade \n contra todo tipo de toxina.

Rouba-Ovelha: Se a pressa é o que você precisa, mas não se importa \n em sacrificar energia, essa é a poção certa. Pegue um Dandelion \n e massacra-o bem com o pilão. Depois, adicione um Fungus \n e amasse-o suavemente. Adicione pouca água, apenas o suficiente \n para diluir os ingredientes. Aqueça levemente, só para que a mistura \n comece a reagir, sem fervura. Misture com cuidado, de leve, \n e a poção estará pronta para te dar velocidade, embora com \n um custo de energia.

Dreamfyre: Para suportar o calor escaldante, essa poção é essencial. \n Comece com um Basilisco e amasse-o bem no pilão. Em seguida, \n triture um Fungus até ficar bem fino. Adicione um terço de água \n e aqueça a mistura até criar pequenas bolhas, mas sem deixar ferver. \n Mexa vigorosamente até a mistura engrossar. Essa poção vai proteger \n você dos efeitos mais intensos do calor por um bom tempo.

Gato Branco: Para aqueles que precisam enxergar no escuro, mesmo que apenas \n em preto e branco, essa poção faz milagres. Pegue um Cactacida \n e triture-o finamente no pilão. Depois, adicione uma Cáscara \n e massacre-a até virar pó. Coloque metade de um vidro de água pura. \n Aqueça suavemente, sem deixar ferver, até a mistura ganhar consistência. \n Mexa com moderação, e a poção estará pronta para proporcionar \n visão noturna temporária.

Trovoada: Se o que você busca é força e resistência, essa poção \n não vai te decepcionar. Comece com um Fungus, amasse-o bem \n com o pilão. Adicione um Albedo, triturado até o pó. Agora, \n coloque pouca água para concentrar os ingredientes. Aqueça a mistura \n até ferver e mexa vigorosamente até obter uma textura densa. \n Após consumir essa poção, sua força e resistência serão \n ampliadas consideravelmente.

Djistka Seca: Para os magos que desejam ver fontes de energia mágica invisíveis, \n esta poção é indispensável. Pegue uma Nevasca e amasse-a com firmeza. \n Depois, adicione um Fungus, triturado até ficar bem fino. Adicione \n pouca água, o suficiente para diluir os ingredientes. Aqueça a mistura \n levemente, só para liberar seu potencial, sem fervura. Mexa levemente, \n e estará pronta. Com essa poção, você verá as energias mágicas \n escondidas ao seu redor.
""")
                    print('[!AGORA VC TEM O LIVRO DO ANDARILHO SOLITÁRIO!]')
                else:
                    print('Tobias fala: ''isso não é o suficiente eu quero mais'' ')

        elif option_book_buy == '2':
            book_verify = 'livro do explorador de cavernas'
            verify_book_True(inventory_books_keys,book_verify)
            if verify_book_True == True:
                break
            else:  
                if money >= 800:
                    inventory_books_keys.append('livro do explorador de cavernas')
                    inventory_books_values.append("""
Nekker: Se você deseja se tornar invisível ao olfato de animais \n e criaturas, essa poção é o que você precisa. Comece triturando \n um Cactacida até que fique em pó. Em seguida, pegue uma Nevasca \n e amasse-a bem no pilão. Adicione metade de um frasco de água \n à mistura. Aqueça a mistura até começar a borbulhar levemente, \n sem ferver completamente. Misture de forma moderada, \n com movimentos constantes, e sua imunidade ao olfato \n estará garantida por um tempo.

Raffard: Essa poção vai te dar uma explosão de energia, mas \n com um preço: o cansaço posterior é inevitável. Comece amassando \n um Madroerme até ele liberar seus óleos naturais. Depois, \n triture um Dandelion. Adicione uma pequena quantidade de água, \n o suficiente para formar uma pasta. Aqueça a mistura até ferver \n vigorosamente. Agora, misture com toda a sua força, até seus braços \n não aguentarem mais. Beba e sinta a energia fluir, sabendo \n que o cansaço virá em breve.

Bosque de Maribor: Se você quer enxergar até os mínimos detalhes \n em pegadas ou manchas, essa poção é perfeita. Pegue um Aether \n e triture-o bem no pilão. Em seguida, amasse um Albedo com força. \n Adicione metade de um vidro de água e aqueça até borbulhar \n suavemente. Misture até obter uma consistência uniforme. Com essa poção, \n sua visão para rastros e marcas se tornará muito mais aguçada.

Coruja: Essa poção te permitirá ver no escuro, mas apenas durante \n a noite profunda. Comece amassando uma Nevasca com cuidado. \n Depois, triture um Dandelion. Adicione uma pequena quantidade de água \n e aqueça levemente, só o suficiente para ativar a mistura. \n Misture suavemente até que a poção ganhe corpo. Com essa poção, \n a noite será sua aliada, revelando o que os olhos normais \n não conseguem ver.

Colmeia: Se você deseja aguçar sua audição, essa poção é indispensável. \n Pegue um Fungus e triture-o até virar pó. Em seguida, amasse um Aether \n até liberar seus óleos. Adicione metade de um vidro de água \n e aqueça até que bolhas suaves comecem a se formar. Misture vigorosamente \n até obter uma textura espessa. Depois de beber, você será capaz \n de ouvir até os sons mais sutis.

Lua Cheia: Para aqueles que precisam ficar acordados por longos períodos \n sem dormir, essa poção é essencial. Comece triturando um Basilisco. \n Depois, amasse um Fungus até que ele libere sua essência. Adicione \n metade de um frasco de água e aqueça levemente, sem deixar ferver. \n Misture vigorosamente até que a poção ganhe consistência. Com essa poção, \n você ficará desperto durante o efeito, sem sentir cansaço.

Sonho do Dragão: Para quem busca proteção contra fogo e queimaduras, \n essa poção oferece resistência temporária. Comece amassando \n um Aether com o pilão. Em seguida, triture um Dandelion. Adicione \n toda a água do frasco e aqueça até a mistura ferver. Mexa com vigor \n até obter uma consistência firme. Com essa poção, as chamas \n e queimaduras não te afetarão por um curto período.
""")
                    print('[!AGORA VC TEM O LIVRO DO EXPLORADOR DE CAVERNAS!]')
                else:
                    print('Tobias fala: ''isso não é o suficiente eu quero mais'' ')

        elif option_book_buy == '3':
            book_verify = 'tomo do caçador de monstros'
            verify_book_True(inventory_books_keys,book_verify)
            if verify_book_True == True:
                break
            else:  
                if money >= 1500:
                    inventory_books_keys.append('tomo do caçador de monstros')
                    inventory_books_values.append("""
Nevasca: Com essa poção, a percepção do tempo parece desacelerar, \n permitindo que você reaja com mais precisão. Para prepará-la, \n comece triturando uma Nevasca, até que suas folhas estejam \n bem quebradas. Em seguida, amasse uma Cáscara no pilão. Adicione \n metade de um frasco de água e aqueça até que a mistura ferva \n vigorosamente. Misture suavemente e pronto, sua percepção do tempo \n estará alterada, permitindo reações mais rápidas.

Tir na Lia: Se você busca cura para ferimentos leves e dores, \n esta poção será sua aliada. Comece amassando um Dandelion \n para extrair seu sumo. Em seguida, triture um Cactacida até que \n se desfaça em pedaços pequenos. Adicione uma pequena quantidade \n de água e aqueça até que bolhas suaves comecem a aparecer. Misture \n moderadamente até que a poção esteja completamente uniforme. Agora \n você tem em mãos uma cura para ferimentos e dores leves.

Alcohest: Embora essa poção não traga benefícios diretos, ela \n é famosa por seu cheiro terrível, capaz de afastar qualquer um \n que a sinta. Para fazê-la, comece triturando um Madroerme no pilão. \n Depois, amasse uma Nevasca com cuidado. Adicione um pouco de água \n à mistura e aqueça até que a mistura borbulhe. Mexa vigorosamente \n até ficar homogênea. Cuidado: o cheiro será insuportável!

Felina: Se você deseja passar despercebido e não emitir nenhum som, \n essa é a poção certa. Comece amassando um Gato com movimentos \n suaves. Em seguida, triture um Fungus até obter uma consistência fina. \n Adicione uma pequena quantidade de água e aqueça levemente. Misture \n suavemente e logo você se verá silencioso como um felino.

Arquigrifo: Para quem precisa de resistência a venenos, essa poção \n oferece proteção. Comece triturando uma Mandrágora, liberando seus \n poderosos efeitos. Em seguida, amasse uma Nevasca. Adicione metade \n de um frasco de água e aqueça até que bolhas apareçam suavemente. \n Misture bem até a poção ficar espessa. Agora você está preparado \n para enfrentar venenos com mais resistência.

Lupina: Se você precisa de uma explosão temporária de energia, \n Lupina é a escolha certa. Comece triturando uma Melancolia, seguida \n de amassar um Cactacida. Adicione uma pequena quantidade de água \n e aqueça até ferver intensamente. Misture com força, até que \n a poção atinja sua consistência. Prepare-se para um surto de energia, \n mas não se esqueça de que ele é passageiro.

Ursídea: Para aqueles que desejam aumentar a resistência a outras \n poções, Ursídea é ideal. Comece amassando um Fogo de Dragão, \n com cuidado para extrair seu poder. Depois, triture um Fungus. \n Adicione metade de um frasco de água e aqueça até que a mistura \n comece a borbulhar suavemente. Misture até obter uma consistência firme. \n Ao consumir, suas resistências a poções serão amplificadas.

Samun: Se o objetivo é resistir a explosões, Samun fornecerá \n a proteção necessária. Comece amassando um Albedo com o pilão, \n depois triture um Basilisco até que ele se esfarele. Adicione \n uma pequena quantidade de água e aqueça levemente. Misture \n moderadamente até obter uma poção robusta e homogênea. Com ela, \n você será resistente a impactos explosivos por um curto período.
""")
                    print('[!AGORA VC TEM O TOMO DO CAÇADOR DE MONSTROS!]')
                else:
                    print('Tobias fala: ''isso não é o suficiente eu quero mais'' ')

        elif option_book_buy == '4':
            book_verify = 'livro do imperador dos 7 reinos'
            verify_book_True(inventory_books_keys,book_verify)
            if verify_book_True == True:
                break
            else:  
                if money >= 2500:
                    inventory_books_keys.append('livro do imperador dos 7 reinos')
                    inventory_books_values.append("""
Liche Ancião: Essa poção confere ao usuário uma semi-invisibilidade, permitindo passar \n despercebido em diversas situações. Para prepará-la, comece triturando a erva \n Draconis até transformá-la em pó fino. Em seguida, amasse uma Nevasca no pilão, \n até liberar seus óleos. Adicione uma pequena quantidade de água à mistura \n e aqueça levemente. Mexa suavemente, e logo você será envolto em uma névoa \n que distorce sua presença, tornando-o parcialmente invisível.

Pó de Lua: Com esta poção, você poderá localizar uma pessoa específica no \n exato momento de seu consumo. Para fazê-la, comece amassando uma Múmia no pilão, \n extraindo seus componentes secretos. Depois, triture um Aether até obter \n uma consistência uniforme. Adicione metade de um frasco de água e aqueça \n até que a mistura ferva intensamente. Misture moderadamente, e a localização \n de qualquer pessoa que você desejar será revelada.

Vento do Norte: Ao beber essa poção, você se tornará resistente ao frio, enfrentando \n as temperaturas mais baixas com tranquilidade. Para prepará-la, triture uma Cactacida \n até ela se desmanchar. Em seguida, amasse uma Erva de Gato. Adicione uma pequena \n quantidade de água e aqueça até que bolhas leves comecem a surgir. Misture vigorosamente \n e, ao finalizar, estará protegido contra o frio.

Unicórnio Negro: Esta poção tem a incrível habilidade de transformar venenos em cura. \n Comece amassando um Dandelion no pilão. Em seguida, triture uma Mandrágora até \n ela liberar seu poder. Adicione uma pequena quantidade de água e aqueça suavemente. \n Misture moderadamente, e os venenos que antes eram mortais agora poderão \n restaurar sua vitalidade.

Dor na Consciência: Com esta poção, o tempo recuará um minuto, permitindo que você \n corrija um erro recente. Para prepará-la, comece triturando um Fungus. Depois, \n amasse uma Melancolia até obter uma mistura homogênea. Adicione metade de um \n frasco de água e aqueça até que a mistura ferva suavemente. Mexa delicadamente, \n e o tempo retrocederá, dando-lhe uma segunda chance.

Rosa de Shaerawed: Embora esta poção não seja destinada para o consumo, ela permite \n que qualquer planta cresça com uma velocidade impressionante. Comece triturando \n uma Nevasca. Em seguida, amasse uma erva de Gato no pilão. Adicione uma pequena \n quantidade de água e aqueça levemente. Misture moderadamente, e aplique-a \n em qualquer planta para acelerar seu crescimento.

Víbora: Com essa poção, você se tornará imune a qualquer tipo de veneno. \n Comece amassando um Aether para liberar seus componentes mágicos. Depois, \n triture um Fungus até transformá-lo em pó. Adicione metade de um frasco de água \n e aqueça até que a mistura ferva intensamente. Misture vigorosamente, e \n sua imunidade contra venenos estará garantida.
""")
                    print('[!AGORA VC TEM O LIVRO DO IMPERADOR DOS 7 REINOS!]')
                else:
                    print('Tobias fala: ''isso não é o suficiente eu quero mais'' ')
        
        elif option_book_buy == '6':
                book_verify = 'livro do velho alquimista'
                verify_book_True(inventory_books_keys,book_verify)
                if verify_book_True == True:
                    break
                else:
                    if len(inventory_books_it) == 5:
                        print('Tobias fala:"Acho que vc já dominou a sabedoria de fazer poções \n aqui vai um presente use com cuidado')
                        inventory_books_keys.append('livro do velho alquimista')
                        inventory_books_values.append("""
Zirael: Essa poção permite ao usuário achar oque quiser e chegar aonde quiser \n muito requisitada Para prepará-la, comece triturando a \n erva Lobo Branco, que simboliza resistência e determinação. Em seguida, amasse o \n Basilisco, uma criatura com poder de transformação. Aqueça a mistura até que \n comece a borbulhar e mexa moderadamente. A poção resultante é prateada e, ao \n consumi-la, ocvê terá a capacidade de chegar aonde quiser.

Rívia: Com esta poção, todos os seus sentidos serão aguçados a níveis \n sobre-humanos. Para prepará-la, triture o Lobo Branco duas vezes, representando tanto \n o poder bruto quanto a precisão necessária. Aqueça até que a mistura fique \n translúcida, mexendo com cuidado. Consumir esta poção concede visão no escuro e \n a capacidade de detectar até o menor sinal, tornando você um caçador sem igual.

Aerondith: Esta poção é ideal para enfrentar as profundezas, permitindo que o \n usuário mergulhe por longos períodos sem precisar de ar e nade com grande \n velocidade. Para prepará-la, amasse o Lobo Branco e o Basilisco, depois adicione \n água e aqueça até ferver. Mexa vigorosamente até que a mistura tome uma \n tonalidade aquosa. Após beber, você se tornará tão ágil quanto qualquer criatura \n aquática.
""")
                        print('[!AGORA VC TEM O LIVRO DO VELHO ALQUIMISTA!]')   
                    else:
                        print('Ainda não ,vc n está pronto')
        elif option_book_buy == '5':
            if  pot_upgrade == False:
                if money >= 5000:
                    pot_upgrade = True
                    print('[!AGORA VC TEM O CALDEIRÂO MODIFICADO DO VELHO ALQUIMISTA!]')
                else:
                    print('Vc n tem dinheiro o suficiente')

            else: 
                print('Vc já tem esse item') 
        elif option_book_buy == 'X':
            break 

    elif option_menu == 6:
        print(f'Vc tem {money} moedas')

    else:
        print('Opção inválida.')
