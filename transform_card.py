# Обработка строковой карты
def transform_card(s):
	start = [0,0]
	finish = [0,0]
	l = s.split('\n')
	l.pop()
	l.pop(0)
	new_list = []
	for i in l:
		tmp = []
		for j in i.split(' '):
			if j == '.':
				tmp.append(0)
			if j == 'x':
				tmp.append(1)
			if j == 's':
				start = [l.index(i),i.split(' ').index('s')]
				tmp.append(0)
			if j == 'f':
				finish = [l.index(i),i.split(' ').index('f')]
				tmp.append(0)
		new_list.append(tmp)
	return start,finish,new_list