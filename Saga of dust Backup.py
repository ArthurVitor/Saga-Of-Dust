#Saga of dust v1
import random
mk = 0

nm = str(input('Qual seu nome? '))
print('Existem 3 aventureiros para você escolher.\n'
      'Aqui estam listados os 3 e suas estatisticas')
print('<>'*30)
print('''Arthur:
Fogo

Vida:247
Atk:12-56
Def:22  
Vel: 26''')
print('<>'*30)
print('''Diego:
Terra

Vida:227
Atk:10-58
Def:15
Vel:15''')
print('<>'*30)

print('''Bia:
Água

Vida:271
Atk:10-53
Def:21
Vel:13''')
print('<>'*30)
print(' ')
print('Vou lhe explicar como funciona o jogo')
print('O jogo funciona com um sistema de turnos que mudam de acordo com uma ação, seja ela atacar/correr/defende e etc')
print('Para você executar uma ação tera que escolher uma dessas opções')
print(' ')
print('Atacar [A]\n', end=''
      'A opção atacar ira causar dano ao inimigo\n'
      'Defender [D]\n'
      'Com a opção defender você ira tentar se defender do ataque de seu inimigo\n'
      'Correr [C]\n'
      'Se você escolher a opção correr você ira sair da partida\n')
print(' ')

esl = ' '
while esl not in 'ABD':
    esl = str(input('Escolha qual aventureiro você deseja usar: ')).strip().upper()[0]
    if esl == 'A':
        Vida = 247
        Atk1 = 12
        Atk2 = 56
        print('Você escolheu o aventureiro Arthur; Boa Sorte na sua aventura!')
    elif esl == 'B':
        Vida = 271
        Atk1 = 10
        Atk2 = 58
        print('Você escolheu o aventureiro Bia; Boa Sorte na sua aventura!')
    elif esl == 'D':
        Vida = 227
        Atk1 = 10
        Atk2 = 53
        print('Você escolheu o aventureiro Diego; Boa Sorte na sua aventura!')

while True:
    avt = ' '
    while avt not in 'SA':
        avt = str(input('Oque você deseja fazer? Suicidio ou Andar? ')).strip().upper()[0]
        if avt == 'S':
            print('Você escolheu se matar!')
            exit()
        elif avt == 'A':
            mnl = random.randint(1, 3)
            print(mnl)
            print(f'Você achou um monstro level {mnl}')
            if mnl == 1:
                atk1 = 15
                atk2 = 40
                msv = 200
            elif mnl == 2:
                atk1 = 20
                atk2 = 45
                msv = 250
            elif mnl == 3:
                atk1 = 25
                atk2 = 55
                msv = 300
            while msv >= 1:
                tt = str(input('Oque você deseja fazer? ')).strip().upper()[0]
                if tt == 'C':
                    break
                if tt == 'A' and msv >= 1 and Vida >= 1:
                    jgt = random.randint(Atk1, Atk2)
                    msv -= jgt
                    if msv <= 0:
                        mk += 1
                        print('O monstro está morto!')
                        print('Você ganhou!')
                        if mk >= 3:
                            print('Você ganhou mais 10 de dano por derrotar 3 monstros sem morrer!')
                            Atk1 += 10
                            Atk2 += 10
                            mk = 0
                        break

                    print(f'Você causou {jgt} de dano ao monstro')
                    print(f'O monstro está com {msv} de vida!\n')
                    print('Agora é a vez do monstro\n')
                    mst = random.randint(atk1, atk2)
                    Vida -= mst
                    if Vida <= 0:
                        print('Você está morto!')
                        break
                    print(f'O monstro causou {mst} de dano a você!')
                    print(f'Você está com {Vida} de vida!\n')