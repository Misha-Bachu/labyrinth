class Game:
	def __init__(self,start=[0,0],finish=[0,0],card=[[0,0],[0,0]]):
		self.__start = start
		self.__finish = finish
		self.__card = card
		self.__way = {}

	def set_card(self,card):
		self.__card = card
	def set_start(self,start):
		self.__start = start
	def set_finish(self,finish):
		self.__finish = finish

	def run(self):
		try:
			print('runing...')
			card = self.__card
			tmp = self.__start
			finish = self.__finish
			way = []
			i = len(card)
			j = len(card[0])
			print(f'i = {i}, j = {j}')
			
		except IndexError:
			print('очень плохая музыка')

	def show(self):
		print(f'start = {self.__start} finish = {self.__finish} card = {self.__card} way = {self.__way}')
