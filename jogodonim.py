#rodada do computador
#
#
#
def computador_escolhe_jogada(n, m):
  i = m
  p = m
  while(p > 0 and p > n):
    p -= 1
  while(i > 0):
    if((n-i)%(m+1) == 0 and n-i > 0):
      p = i
      break
    i -= 1

  print('O computador tirou ', p, ' peças.')
  if(n-p == 1):
    print('Agora resta apenas uma peça no tabuleiro.')
  else:
    print('Agora restam apenas ', n-p,  'peças no tabuleiro.\n')
    
  return n-p
      
#rodada do jogador
#
#
  
def usuario_escolhe_jogada(n, m):
  while True:
    p = int(input('Quantas peças você vai tirar?'))
    if(p > 0 and p <= n and p <= m):
      break
    print('\nOops! Jogada inválida! Tente de novo.\n')
  print('Voce tirou ', p, ' peças.')
  if(n-p == 1):
    print('Agora resta apenas uma peça no tabuleiro.')
  else:
    print('Agora restam apenas ', n-p,  'peças no tabuleiro.\n')
  return n-p


#corpo do jogo
#
#
#
def Partida():
  n = int(input('Quantas peças?'))
  m = int(input('Limite de peças por jogada?'))
  vez = 0
  
  if(n%(m+1)==0):
    print('\nVocê começa!\n')
  else:
    vez = 1
    print('\nComputador começa!\n')
  
  while(n != 0):
    if(vez == 0):
      n = usuario_escolhe_jogada(n, m)
      vez = 1
    elif(vez == 1):
      n = computador_escolhe_jogada(n, m)
      vez = 0
  if (vez == 0):
    print('Fim do jogo! O computador ganhou!\n')
    return 1
  elif(vez == 1):
    print('Fim do jogo! Você ganhou!\n')
    return 0

print('Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato')

computador = 0
jogador = 0
modoDeJogo = int(input())
if(modoDeJogo == 1):
  print('Voce escolheu  uma partida isolada!')
  Partida()
  
elif(modoDeJogo == 2):
  print('Voce escolheu um campeonato!')
  for i in range (3):
    print('**** Rodada ', i+1 ,' ****')
    boolean = Partida()
    if(boolean):
      computador += 1
    else:
      jogador += 1
  print('**** Final do campeonato! ****\n\nPlacar: Você ', jogador, ' X ', computador, ' Computador')



