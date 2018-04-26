# --------------- #
#				  #
#   TIC-TAC-TOE   #
#				  #
# --------------- #

import os
board = [' '] * 10

def print_board():
	# os.system('cls') ## clears the console. doesn't work with repl
	print('\n')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
	print('-' * 11)
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
	print('-' * 11)
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
	print('\n')

def move(box, plr):
	while 1:
		if board[box] == ' ':
			board[box] = plr
			break
		else:
			print('Invalid move.')
			box = int(input(plr + ', pick again: '))
	print_board()

def new_game():
	if input('Would you like to play again, y/n? ') == 'n':
		print('Bye bye!')
		return False
	return True

def victorious(plr):
	if ' ' not in board[1:]:
		print('The game is a draw!')
		return True

	def check(a,b,c):
		if board[a] == board[b] == board[c] == plr:
			print(plr + ', you won the game!')
			return True

	if check(1,2,3): return True
	if check(4,5,6): return True
	if check(7,8,9): return True
	if check(1,4,7): return True
	if check(2,5,8): return True
	if check(3,6,9): return True
	if check(1,5,9): return True
	if check(3,5,7): return True

	return False


while 1:	
	move(int(input('X, pick a box: ')), 'X')
	if not victorious('X'):
		move(int(input('O, pick a box: ')), 'O')
		if not victorious('O'):
			continue
	board = [' '] * 10
	if new_game() == False:
		break
