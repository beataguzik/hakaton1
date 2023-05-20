

#najpierw zrobić plansze a,b,c i 1,2,3
def game_board():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

def display_board(board):
    print('  1 2 3')
    print('a {}|{}|{}'.format(board[0][0], board[0][1], board[0][2]))
    print('  -----')
    print('b {}|{}|{}'.format(board[1][0], board[1][1], board[1][2]))
    print('  -----')
    print('c {}|{}|{}'.format(board[2][0], board[2][1], board[2][2]))

#zrobić kombinacje ruchów + sprawdzenia i zabezpieczenia
def make_move(player, board):
    good_move = False
    while not good_move:
        move = input('Graczu {}, napisz swój ruch: '.format(player))
        if len(move) != 2:
            print('Zły ruch. Podaj wiersz (a, b lub c) + kolumnę (1, 2 lub 3) np.a1 : ')
            continue
        wiersz, kolumna = move[0], move[1]
        if wiersz not in ['a', 'b', 'c'] or kolumna not in ['1', '2', '3']:
            print('Wpisałeś źle wiersz lub/i kolumne. Podaj jeszcze raz (np. b3): ')
            continue
        wiersz_index = ord(wiersz) - ord('a')
        kolumna_index = int(kolumna) - 1
        if board[wiersz_index][kolumna_index] != ' ':
            print('Zajęte pole. Podaj wolne pole: ')
            continue
        board[wiersz_index][kolumna_index] = player
        good_move = True

#na koniec posprawdzać kto wygrywa
def check_winner(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False



#po skonczonej rozgr zapytać czy jeszcze gra
def if_next_move():
    answer = input('Czy chcesz zagrać jeszcze raz? (tak/nie): ')
    return answer.lower() == 'tak'


#zmiana nazwy graczy
def play():
    active_game = True
    while active_game:
        board = game_board()
        player1 = input("Wpisz nazwę pierwszego gracza: ")
        player2 = input("Wpisz nazwę drugiego gracza: ")
        player_turn = player1
        while True:
            display_board(board)
            make_move(player_turn, board)
            if check_winner(board, player_turn):
               display_board(board)
               print('Brawo, wygrał gracz {}!'.format(player_turn))
               break
            if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
               display_board(board)
               print('Remis!4857/*8')
               break
            player_turn = player2 if player_turn == player1 else player1
        if not if_next_move():
            break

play()