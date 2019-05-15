import copy

# Класс лабиринта
class Game:
	def __init__(self,start=[0,0],finish=[0,0],card=[[0,0],[0,0]]):
		self.__start = start
		self.__finish = finish
		self.__card = card
		self.__way = []

	def set_card(self,card):
		self.__card = card
	def set_start(self,start):
		self.__start = start
	def set_finish(self,finish):
		self.__finish = finish
	def show_way(self):
		print(f'Way : {self.__way }')
		

	def run(self):
		try:
			card = copy.deepcopy(self.__card)
			finish = self.__finish
			way = [self.__start]
			n = len(card)
			m = len(card[0])
			self.__show_card_string(copy.deepcopy(self.__card),m)
			if card[ way[0][0] ][ way[0][1] ] == 0:
				card[ way[0][0] ][ way[0][1] ] = 2

			while True:
				if finish in way:
					self.__way = self.__get_way(card,n,m)[::-1] 
					return
				if way == []:
					print('Путь не найден.')
					return
				tmp = way.pop(0)
				i = tmp[0]
				j = tmp[1]
				cell = card[i][j]
				if i+1 < n:
					if card[i+1][j] == 0:
						card[i+1][j] = cell+1
						way.append([i+1,j])
				
				if i-1 >= 0:
					if card[i-1][j] == 0:
						card[i-1][j] = cell+1
						way.append([i-1,j])
				
				if j+1 < m:
					if card[i][j+1] == 0:
						card[i][j+1] = cell+1
						way.append([i,j+1])
				
				if j-1 >= 0:
					if card[i][j-1] == 0:
						card[i][j-1] = cell+1
						way.append([i,j-1])
		except IndexError:
			print('Вы явно где то ошиблись.')
		except TypeError:
			print('Вы явно где то ошиблись.')

	def __get_way(self,card,n,m):
		way = [self.__finish]
		i = self.__finish[0]
		j = self.__finish[1]
		card2 = copy.deepcopy(self.__card)
		card2[i][j] = 2
		while True:
			if self.__start == [i,j]:
				break
			cell = card[i][j]-1
			if i+1 < n:
				if card[i+1][j] == cell:
					i += 1
					card2[i][j] = 2
					way.append([i,j])
					continue
			if i-1 >= 0:
				if card[i-1][j] == cell:
					i-=1
					card2[i][j] = 2
					way.append([i,j])
					continue
			if j+1 < m:
				if card[i][j+1] == cell:
					j+=1
					card2[i][j] = 2
					way.append([i,j])
					continue
			if j-1 >= 0:
				if card[i][j-1] == cell:
					j-=1
					card2[i][j] = 2
					way.append([i,j])
					continue
		self.__show_card_string(card2,m)
		return way

	def __show_card(self,card):
		for i in card:
			print(i)

	def __show_card_string(self,card,m):
		s = '_'*(m+1)*2
		s+='\n'
		card[self.__start[0]][self.__start[1]] = 3
		card[self.__finish[0]][self.__finish[1]] = 4
		for i in card:
			s+='|'
			for j in i:
				if j == 0: s+='  '
				if j == 1: s+=' x'
				if j == 2: s+=' .'
				if j == 3: s+=' s'
				if j == 4: s+=' f'
			s+='|\n'
		s+= u'\u203e'*(m+1)*2
		print(s)