# Exercício - sistema de perguntas e resposta 

perguntas = [
    {
        'Pergunta': 'Quanto é 49-7?',
        'Opções': [43, 41, 42, 39],
        'Resposta': 42,
    },
    {
        'Pergunta': 'Quanto é 7*7?',
        'Opções': [49, 41, 42, 39],
        'Resposta': 49,
    },
    {
        'Pergunta': 'Quanto é 25/5?',
        'Opções': [3, 4, 2, 5],
        'Resposta': 5,
    },
]


qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()
    print('Opções:')

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i}) {opcao}')
    print()
    
    resposta = input('Escolha uma opção: ')
    acertou = False
    resposta_int = None
    qtd_opcoes = len(opcoes)


    if resposta.isdigit():
        resposta_int = int(resposta)
    
    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcoes:
            if opcoes[resposta_int] == pergunta['Resposta']:
                acertou = True
    
    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou :)')
    else:
        print('Errou :(')
    
    
    print()
    
print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas')
    