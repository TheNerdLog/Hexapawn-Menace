import random as rnd
import time
# import pickle
# import hexapawn_core as core
# random.randrange (start, stop, step) will release numbers of the step between the start and stop inputs.

# all the menace boxes with hashes
# the board in match 2a1b1c:
#     |x x x|
#     |O    |
#     |  O O|


#Turn 2
xxxo___oo = ['2,4', '2,5', '3,6']
xxx_o_o_o = ['1,4', '1,5', '3,5', '3,6']

# turn 4
x_xo____o = ['3,6']
x_xxo___o = ['1,5', '4,7', '3,5', '3,6']
x_xx_o_o_ = ['4,7', '4,8']
x_xoo__o_ = ['1,5', '3,5']
xx_oox__o = ['1,5', '2,4']
xx_o_o__o = ['2,4', '2,6']
_xxox___o = ['2,4', '5,9', '5,8']
_xx_o___o = ['3,5', '3,6']
_xx_o_o__ = ['3,5', '3,6']
_xx_xoo__ = ['5,8', '5,7', '2,6'] #

#Turn 6
__xxo____ = ['4,7', '3,5', '3,6']
_x_oo____ = ['2,4']
_x_oxo___ = ['5,8', '2,4', '2,6']
x__xoo___ = ['1,5', '4,7']
__xxxo___ = ['4,7', '5,8']
_x_oox___ = ['2,4', '6,9']
_xxoxo___ = ['2,4', '2,6', '5,8']
_x__xo___ = ['2,6', '5,8']
__xoxx___ = ['5,8', '6,9']
__x_ox___ = ['3,5', '6,9']

all_moves = [xxxo___oo, xxx_o_o_o, x_xo____o, x_xxo___o, x_xx_o_o_, x_xoo__o_, xx_oox__o, xx_o_o__o, _xxox___o,
             _xx_o___o, _xx_o_o__, _xx_xoo__, __xxo____, _x_oo____, _x_oxo___, x__xoo___, __xxxo___, _x_oox___,
             _xxoxo___, _x__xo___, __xoxx___, __x_ox___]
all_moves_represented = ['xxxo___oo', 'xxx_o_o_o', 'x_xo____o', 'x_xxo___o', 'x_xx_o_o_', 'x_xoo__o_', 'xx_oox__o',
                         'xx_o_o__o', '_xxox___o', '_xx_o___o', '_xx_o_o__', '_xx_xoo__', '__xxo____', '_x_oo____',
                         '_x_oxo___', 'x__xoo___', '__xxxo___', '_x_oox___', '_xxoxo___', '_x__xo___', '__xoxx___',
                         '__x_ox___']
moves_made = []
wins = 0
game_board = ['x', 'x', 'x', '_', '_', '_', 'o', 'o', 'o']
left_column = ['0', '3', '6']
center_column = ['1', '4', '7']
right_column = ['2', '5', '8']
col = []
othercol1 = []
othercol2 = []
gameover = False

def rev_ind(li, x):
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i
    raise ValueError("{} is not in list".format(x))


class AI:
    def mirror_board(self, board):
        row1 = board[:3]
        row2 = board[3:6]
        row3 = board[6:]
        return row1[::-1] + row2[::-1] + row3[::-1]

    def is_mirrored(self, board):
        if board in all_moves_represented:
            return False
        elif self.mirror_board(board) in all_moves_represented:
            return True
        else:
            return False

    def flip_move(self, move):
        a = str(int(move[:1])-1)
        b = str(int(move[-1:])-1)
        if a in left_column:
            a = right_column[left_column.index(a)]
        elif a in right_column:
            a = left_column[right_column.index(a)]
        if b in left_column:
            b = right_column[left_column.index(b)]
        elif b in right_column:
            b = left_column[right_column.index(b)]
        return str(int(a)+1) + ',' + str(int(b)+1)

    def rand_move (self, board_layout):
        if self.is_mirrored(board_layout) is False:
            u = board_layout
            mirrored = False
            print('is mirrored')
        else:
            u = self.mirror_board(board_layout)
            mirrored = True
        b = all_moves_represented.index(u)
        s = rnd.choice(all_moves[all_moves_represented.index(u)])
        moves_made.append([b, s])
        if mirrored is True:
            s = self.flip_move(s)
        return s

    def did_i_win(self, win): # win is a Bool
        global gameover
        if win is False:
            losing_move = moves_made[len(moves_made)-1]  # an array of u and s
            all_moves[losing_move[0]].remove(losing_move[1])  # all_moves.index(losing_move[0])
        moves_made.clear()
        gameover = True


class Game:
    def to_string(self):
        s = ''
        for i in range(len(game_board)):
            s += game_board[i]
        return s

    def is_stalemate(self, player):
        p = player
        b = True
        if player is True:
            s = 'o'
        elif player is False:
            s = 'x'
        global col
        global othercol1
        global othercol2

        for i in range(len(game_board)):

            if game_board[i] == s:
                if str(i) in left_column:
                    col = left_column
                    othercol1 = center_column
                    othercol2 = othercol1
                elif str(i) in center_column:
                    col = center_column
                    othercol1 = right_column
                    othercol2 = left_column
                elif str(i) in right_column:
                    col = right_column
                    othercol1 = center_column
                    othercol2 = othercol1
                if p:
                    if game_board[i-3] == 'x' and game_board[int(othercol1[col.index(str(i))-1])] != 'x' \
                            and game_board[int(othercol2[col.index(str(i))-1])] != 'x':
                        b = True
                    else:
                        return False
                else:
                    if game_board[i+3] == 'o' and game_board[int(othercol1[col.index(str(i))+1])] != 'o' \
                            and game_board[int(othercol2[col.index(str(i))+1])] != 'o':
                        b = True
                    else:
                        return False
        return b

    def get_winner(self, player):
        try:
            game_board.index('x')
        except ValueError:
            print('Real person has won!! \n┬──┬ ノ( ゜-゜ノ)')
            if player is True:
                return True
            else:
                return False

        try:
            game_board.index('o')
        except ValueError:
            print('AI has won!! \n(ノಠ益ಠ)ノ彡┻━┻')
            if player is False:
                return True
            else:
                return False
        if rev_ind(game_board, 'x') >= 6:
            print('AI has won!! \n(ノಠ益ಠ)ノ彡┻━┻')
            if player is False:
                return True
            else:
                return False
        elif game_board.index('o') <= 2:
            print('Real person has won!! \n┬──┬ ノ( ゜-゜ノ)')
            if player is True:
                return True
            else:
                return False
        elif self.is_stalemate(player):  # Returns a Boolean
            if player is True:
                print('Real person has won!! \n┬──┬ ノ( ゜-゜ノ)')
            else:
                print('AI has won!! \n(ノಠ益ಠ)ノ彡┻━┻')
            return self.is_stalemate(player)
        return None

    def move(self, move): # move is in 'a,b' form
        a = int(move[:1])
        b = int(move[-1:])
        game_board[a-1] = '_'
        game_board[b - 1] = 'x'

    def show_board (self):
        print('|' + game_board[0] + game_board[1] + game_board[2] + '|')
        print('|' + game_board[3] + game_board[4] + game_board[5] + '|')
        print('|' + game_board[6] + game_board[7] + game_board[8] + '|')

    def reset_board(self):
        game_board.clear()
        game_board.extend(['x', 'x', 'x', '_', '_', '_', 'o', 'o', 'o'])
        self.show_board()


class Player:
    def is_move_valid (self, move):
        a = int(move[:1])-1
        b = int(move[-1:])-1  # a and b are the matching indexes of the columns
        attack = False
        output = False
        global col
        global othercol1
        global othercol2
        for i in range(len(game_board)):
            if a == i and game_board[i] == 'o':
                if str(i) in left_column:  # '7,4' goes in here
                    col = left_column
                    othercol1 = center_column
                    othercol2 = center_column
                elif str(i) in center_column:
                    col = center_column
                    othercol1 = right_column
                    othercol2 = left_column
                elif str(i) in right_column:
                    col = right_column
                    othercol1 = center_column
                    othercol2 = center_column
                else:
                    return output
                if str(b) == col[col.index(str(a))-1]:
                    attack = False
                elif str(b) == othercol1[col.index(str(a))-1] or str(b) == othercol2[col.index(str(a))-1]:
                    attack = True
                for y in range(len(game_board)):
                    if b == y and game_board[y] == '_' and attack is False:
                        return True
                    elif b == y and attack is True:
                        return True
                    else:
                        output = False
        return output

    def move(self, move):
        if self.is_move_valid(move):
            a = int(move[:1])
            b = int(move[-1:])
            game_board[a-1] = '_'
            game_board[b-1] = 'o'
        else:
            self.move(input("That wasn't valid; What is your move(it needs to be in format a,b) :"))


gb = Game()
p = Player()
a1= AI()

gb.reset_board()
print(gb.to_string())
print('Welcome to Hexapawn.')
time.sleep(.5)
print('You are playing against an AI.')
time.sleep(.5)
print('The goal of the game is to win.')
time.sleep(.5)
print('To win, you can do one of three things:')
time.sleep(.5)
print('1. Take the last move.')
print('2. Take the last piece.')
print('3. Get to the end of the board.')
time.sleep(.5)
print('This is the playing table:')
print('|X|X|X|')
print('| | | |')
print('|O|O|O|')
time.sleep(.5)
print('The grid is sorted as shown below.')
time.sleep(.5)
print('|1|2|3|')
print('|4|5|6|')
print('|7|8|9|')
time.sleep(.5)
print('For example, if you wanted to move the bottom rightmost piece')
print('you would type "9,6" and it would move forward')
time.sleep(.5)
print('remember that you can only eat diagonaly')
time.sleep(.5)

gb.reset_board()
while True:
    gameover = False
    if gameover is False:
        p.move(input("What is your move(it needs to be in format a,b) :"))
        gb.show_board()
        if gb.get_winner(True):
            gameover = True
            a1.did_i_win(False)
            gb.reset_board()
            gb.show_board()
    if gameover is False:
        gb.move(a1.rand_move(gb.to_string()))
        print('-----')
        gb.show_board()
        if gb.get_winner(False):
            gameover = True
            a1.did_i_win(True)
            gb.reset_board()

