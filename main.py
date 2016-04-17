import random


def disp_board(board):
    print '\n'
    print ' ' + board[1] + '| '+ board[2] + '| ' + board[3]
    print ' ' + board[4] + '| '+ board[5] + '| ' + board[6]
    print ' ' + board[7] + '| '+ board[8] + '| ' + board[9]
def get_player_letter():
    letter = ''
    while not(letter=='X' or letter =='O'):
        letter = raw_input('Play X or O: ').upper()
        if not(letter=='X' or letter =='O'):
            print 'Invalid Char(X and O only)'
    if letter=='X':
        return ['X','O']

    elif letter == 'O':
        if random.randint(1,0)==0:
            return ['O','X']
        else:
            return ['X','O']

def first_to_mov():

        return  'Player 1'

def get_player_move(board):
    move = ' '
    move = raw_input('Choose your next position: (1-9) ')
    while not legal_moves(board, int(move)):
        print 'ahoo!'
    return int(move)

def check_winner(board,move):
    return ((board[7] == move and board[8] == move and board[9] == move) or  # across the top
            (board[4] == move and board[5] == move and board[6] == move) or  # across the middle
            (board[1] == move and board[2] == move and board[3] == move) or  # across the bottom
            (board[7] == move and board[4] == move and board[1] == move) or  # down themarkft side
            (board[8] == move and board[5] == move and board[2] == move) or  # down the middle
            (board[9] == move and board[6] == move and board[3] == move) or  # down the right side
            (board[7] == move and board[5] == move and board[3] == move) or  # diagonal
            (board[9] == move and board[5] == move and board[1] == move))  # diagonal
def get_computer_move():
    move=random.randint(1,10)
    return move

def legal_moves(board,move):
    return board[move]==' '
def mark_board(board,letter,move):
    board[move]=letter


print 'Tic-Tac-Toe\n by 6KB\n'
while True:
    b=[' ']*10
    player_letter,comp_letter = get_player_letter()
    turn=first_to_mov()
    print first_to_mov() + ' to move First'
    status = True

    while True:
            if turn =='Player 1':
                disp_board(b)
                move=get_player_move(b)
                print mark_board(b,player_letter,move)

                if check_winner(b,player_letter):
                    disp_board(b)
                    print  'Congratulations! You win!'
                    break
                else:
                    disp_board(b)
                    move = get_player_move(b)
                    print mark_board(b, comp_letter, move)
                    if check_winner(b, comp_letter):
                        print 'Player 2 has Won'



            else:
                 disp_board(b)
                 move=get_player_move()
                 print mark_board(b,comp_letter,move)
                 if check_winner(b,comp_letter):
                        print 'Player 2 has Won'





