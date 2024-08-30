import random

pont = 0 # variavel para ativar condicao, assim mostrando pontuação do jogador
pont2 = [] # lista para pegar pontuação do jogador e somar no final da partida
parada = False # variavel para parar loop
parada2 = False # variavel para parar loop
parada3 = False # variavel para parar loop
while True: # loop do jogo
    pont = 0 # para reiniciar a pontuação do jogador a cada jogo
    a = random.randint(0, 10) # número a ser sorteados
    for c in range(5): # 5 tentativas para o jogador
        while True: # loop de tratamento de erro
            try:
                tent = int(input('\033[1mChute o número gerado pelo computador: \033[m'))
                break
            except (NameError, ValueError):
                print('\033[1;31mResposta inválida\033[m')
        if tent > 10: # se o jogador fazer uma jogada acima de 10 que foi pedida, aparecerar um loop pedindo a resposta correta
            while True:
                print('\033[1;31mValor acima do pedido. Tente Novamente\033[m')
                tent = int(input('Chute o número gerado pelo computador: '))
                if tent <= 10:
                    break   
        parada2 = False # para reiniciar o valor de True para False
        parada3 = False # para reiciniar o valor de True para False
        pont += 1 # contador para gerenciar a pontuação do jogador
        if tent == a: # se o chute do jogador for igual número sorteado    
            if pont == 1: # condicoes para para pontuação do jogador baseado na variavel pont
                print('\033[1;32mPARABENS VOCE CONSEGUIU. VOCE GANHOU 100 PONTOS!!\033[m')
                pont2.append(100)
                parada3 = True # variavel para parar o loop
            elif pont == 2:
                print('\033[1;33mPARABENS VOCE CONSEGUIU. VOCE GANHOU 80 PONTOS!!\033[m')
                pont2.append(80)
                parada3 = True 
            elif pont == 3:
                print('\033[1;34mPARABENS VOCE CONSEGUIU. VOCE GANHOU 60 PONTOS!!\033[m')
                pont2.append(60)
                parada3 = True 
            elif pont == 4:
                print('\033[1;35mPARABENS VOCE CONSEGUIU. VOCE GANHOU 40 PONTOS!!\033[m')
                pont2.append(40)
                parada3 = True 
            elif pont == 5:
                print('\033[1;31mPARABENS VOCE CONSEGUIU. VOCE GANHOU 20 PONTOS!!\033[m')
                pont2.append(20) 
                parada3 = True 
        if parada3 == True: # condicao para parar o loop
            break
        elif c == 4: # se o for chegar no valor de 4 o jogador perde
            print('\033[1mQue pena, Voce perdeu :C\033[m')
    while True: # loop para tratamento de erro
        try:
            cont = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
            if cont == 'N':
                parada2 = True
                break
            elif 'S' in cont:
                break
            else:
                print('\033[1;31mResposta inválida\033[m')
        except IndexError:
            print('\033[1;31mResposta inválida\033[m')
    if parada2 == True: 
        break
print(f'Obrigado por jogar!! Sua pontuação final foi de \033[1;32m{sum(pont2)}\033[m pontos') # loop finalizado mostrando o resultado do jogador
