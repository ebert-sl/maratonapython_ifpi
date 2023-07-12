from random import randrange # Exibirá um número aleatório para o computador jogar

board = [[0 for i in range(3)] for j in range(3)] # Cria o tabuleiro

def display_board(board): # Cria a visão do tabuleiro
    counter = 1
    for i in range(3):
        print(('+' + '-' * 7) * 3 + '+')
        print(('|       ') * 3 + '|')
        print('|', end='')
        for j in range(3):
            if board[i][j] == 'O' or board[i][j] == 'X':
                if j == 2:
                    print('  ', board[i][j], '  |')
                else:
                    print('  ', board[i][j], '  |', end='')
                counter += 1
                continue
            board[i][j] = counter
            if j == 2:
                print('  ', board[i][j], '  |')
            else:
                print('  ', board[i][j], '  |', end='')
            counter += 1
        print(('|       ') * 3 + '|')
    print(('+' + '-' * 7) * 3 + '+')

def enter_move(board): # Movimento do usuário
    display_board(board) # Mostra o resultado parcial
    try:
        number = int(input('Digite um número: '))
    except:
        print('Você digitou um valor inválido! Tente novamente.')
        return enter_move(board)
    for i in range(3):
        for j in range(3):
            if board[i][j] == number: # Verifica se o número está entre 1 e 9
                check = (i, j,)
                if check in make_list_of_free_fields(board): # Verifica se o número está livre
                    board[i][j] = 'O'
                    make_list_of_free_fields(board) # Atualiza a lista de espaços livres
                    if victory_for(board, 'O'):
                        display_board(board) # Mostra o resultado final
                        print('VITÓRIA DO JOGADOR!')
                        quit()
                    draw_move(board) # Passa pro jogador
    print('\nVocê digitou um número errado ou já ocupado! Tente novamente.')
    enter_move(board)
                
def make_list_of_free_fields(board): # Espaços livres
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'O' and board[i][j] != 'X':
                free_fields.append((i, j,))
    return free_fields

def victory_for(board, sign): # Verifica vitória
    if (board[0][0], board[1][1], board[2][2]) == (sign, sign, sign): # Diagonal
        return True
    elif (board[0][2], board[1][1], board[2][0]) == (sign, sign, sign): # Diagonal
        return True
    elif (board[0][0], board[0][1], board[0][2]) == (sign, sign, sign): # Linha
        return True
    elif (board[1][0], board[1][1], board[1][2]) == (sign, sign, sign): # Linha
        return True
    elif (board[2][0], board[2][1], board[2][2]) == (sign, sign, sign): # Linha
        return True
    elif (board[0][0], board[1][0], board[2][0]) == (sign, sign, sign): # Coluna
        return True
    elif (board[0][1], board[1][1], board[2][1]) == (sign, sign, sign): # Coluna
        return True
    elif (board[0][2], board[1][2], board[2][2]) == (sign, sign, sign): # Coluna
        return True

def draw_move(board): # Movimento do computador
    for count in range(10):
        random_number = randrange(10) # Seleciona um número aleatório entre 1 e 9
        for i in range(3):
            for j in range(3):
                if board[i][j] == random_number:
                    check = (i, j,)
                    if check in make_list_of_free_fields(board): # Verifica se o número está livre
                        board[i][j] = 'X'
                        make_list_of_free_fields(board) # Atualiza a lista de espaços livres
                        if victory_for(board, 'X'):
                            display_board(board) # Mostra o resultado final
                            print('VITÓRIA DO COMPUTADOR!')
                            quit()
                        enter_move(board) # Passa pro jogador
                    
enter_move(board)