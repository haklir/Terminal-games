# ------------- #
#				#
#   BLACK-JACK	#
#				#
# ------------- #

from random import shuffle
from time import sleep
import os

card_values = 	{
	'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,'8': 8,
	'9': 9, '10':10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11
				}

class Player:

	def __init__(self, name, money):
		self.name = name
		self.money = money
		self.hand = []
		self.busted = False

	def stake(self):
		amount = 10**10
		while amount > self.money:
			amount = int(input("Place bet: "))
			if amount > self.money:
				print('Not enough cash.')
			else:
				self.money -= amount
				self.bet += amount
				break

	def draw(self):
		self.hand.append(game.deck.pop())
		
		handvalue = self.value()

		if handvalue > 21:
			self.busted = True
			print_game()
			return

		if self.name == 'Dealer':
			if handvalue < 17 or handvalue < player1.value():
				print_game()
				sleep(0.8)
				dealer.draw()
			else:
				print_game()
				sleep(0.8)

	def value(self):
		hand_value = sum([card_values[i] for i in self.hand])
		ace_count = self.hand.count('A')

		while hand_value > 21 and ace_count > 0 :
			hand_value -= 10
			ace_count -= 1

		return hand_value


class Game:

	def __init__(self):
		self.deck = [
		'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
					] * 4
		shuffle(self.deck)
		player1.busted = False
		player1.bet = 0
		player1.hand = []
		dealer.busted = False
		dealer.hand = []


def print_game():
	os.system('cls')

	# prints dealers hand etc.
	print('{:15}'.format('Dealer:'), end='')
	for card in dealer.hand:
		print('|' + card + '|', end='')
	if dealer.busted:
		print(' BUST!', '\n')
	else:
		print(' ', dealer.value(), '\n')

	# prints players hand etc.
	print('{:15}'.format(player1.name + ':'), end='')
	for card in player1.hand:
		print('|' + card + '|', end='')
	if player1.busted:
		print(' BUST!', '\n')
	else:
		print(' ', player1.value(), '\n')

	# prints money stuff
	print('BET:  {}'.format(player1.bet))  
	print('BANK: {}'.format(player1.money), '\n')
	print('-' * 30, '\n')

def define_winner():
	player1_value = player1.value()
	dealer_value = dealer.value()
	win = False

	if dealer.busted or player1_value > dealer_value:
		win = True
	elif player1_value == dealer_value and len(player1.hand) < len(dealer.hand):
		win = True

	if win:
		player1.money += player1.bet * 2
		print_game()
		print('You won {}€!'.format(player1.bet))
		
	else:
		print('You lost {}€.'.format(player1.bet))

os.system('cls')
dealer = Player('Dealer', 9999999)
player1 = Player(input('Name: '), int(input('Cash: ')))

while 1:

	if not input('Wanna play? ').lower().startswith('y'):
		print('C U!')
		break

	game = Game()
	dealer.hand.append(game.deck.pop())
	player1.draw()
	player1.draw()
	player1.stake()
	print_game()

	while player1.busted == False:
		if input('Draw? ').lower().startswith('y'):
			player1.draw()
			print_game()
		else:
			break

	if player1.busted:
		print('You lost {}€'.format(player1.bet))
	else:
		dealer.draw()
		define_winner()