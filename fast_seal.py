#!usr/bin/env python
#!-*- config: utf-8 -*-

# This script is to be used to train the rapid set of text
# Этот сценарий должен использоваться для обучения быстрого набора текста

import os
os.system('cls||clear') # Clear terminal

menu = '''
1 - Start
2 - Choos system text
3 - Exit\n\n'''

sys_text = ''' 
1 - Text for 30 words 
2 - Text for 50 words
3 - Text for 150 words
'''
sys_text_rus_30 = '''Обычная клавиатура не позволяет комфортно набирать большие тексты. Пальцы и руки быстро устают, что приводит к постепенному снижению скорости печати и, как следствие, к ухудшению качества  и увеличению числа опечаток.'''
sys_text_rus_50 = '''Во время печати на клавиатуре задействованы различные мышцы кистей рук. Любым мышцам свойственна усталость и пальцы рук не исключение. Мозг дает рукам сигнал нажать ту или иную клавишу, а пальцы не слушаются. Пальцы устали и хотят отдохнуть! Отсюда снижение скорости и ошибки - из-за усталости. По этому отдых важная часть!'''
sys_text_rus_150 = '''Основы ФЫВА и ОЛДЖ – два магических слова, которые помогут любому желающему быстро научиться печатать текст на компьютере. Клавиши с этими буквами находятся в среднем (основном) ряду клавиатуры.
На пути к быстрой печати 50% успеха зависит от правильной постановки рук на клавиатуре, от того, насколько точно Вы умеете ставить пальцы на исходную позицию, от умения, не глядя на клавиатуру, находить основную позицию, чувствовать и ощущать клавиатуру.
Поставьте пальцы левой руки на четыре крайние буквы основного ряда клавиатуры – ФЫВА, пальцы правой руки – ОЛДЖ. Большие пальцы рук автоматически встают над пробельной клавишей. Это исходное положение рук на клавиатуре.
Быстрая скорость печати вырабатывается путем ежедневной практики, но гораздо эффективнее проводить тренировку набора на специальном клавиатурном тренажёре. Такие тренажёры рассчитаны на людей, умеющих набирать слепым десятипальцевым методом.
В основе клавиатурного тренажёра для развития скоростной печати заложен принцип, когда при наборе текста фиксируются опечатки пользователя, на основе которых генерируется последующии порции текста с проблемными словами или буквосочетаниями.'''

print(menu)
while menu:
	write = input('Choose nomber: ')

# 1 menu
	if write == '1':
		Input_text_repeat = input('Please write new text!\n\n')
		Input_text_user = input('Please, repeat this text:\n\n' + Input_text_repeat + '\n\n')
		if Input_text_repeat == Input_text_user:
			print('WELL DONE!!!!!')
			while True:
				write2 = input(' Do your want again? Y/N\n')
				if write2 == 'Y':
					Input_text_user = input('Please, repeat this text:\n\n' + Input_text_repeat + '\n\n')
				elif write2 == 'N':
					print('Ok, Bye!)))')
					break
				else:
					print('Sorry, your loose, repeat now!')
		else:
			print('Sorry, your loose, repeat now!')

# 2 menu
	elif write == '2':
		print(sys_text)
		Choos_systext = input('Choose number: ')
		while Choos_systext:

# Chooce 30 words

			if Choos_systext == '1': 
				Input_text_user = input('Please, repeat this text:\n\n' + sys_text_rus_30 + '\n\n')
				if sys_text_rus_30 == Input_text_user:
					print('WELL DONE!!!!!\n')
					while True:
						write2 = input(' Do your want again? Y/N\n')
						if write2 == 'Y':
							Input_text_user = input('Please, repeat this text:\n\n' + sys_text_rus_30 + '\n\n')
						elif write2 == 'N':
							os.system('cls||clear')
							print(menu)
							break
						else:
							print('Sorry, your loose, repeat now!')
							while True:
								write2 = input('Do your want again? Y/N\n')
								if write2 == 'Y':
									Input_text_user = input('Please, repeat this text:\n\n' + sys_text_rus_30 + '\n\n')
								elif write2 == 'N':
									os.system('cls||clear')
									print(menu)
									break
							break
					break
				else:
					print('Sorry, your loose, repeat now!\n')
					while True:
						write2 = input('Do your want again? Y/N\n')
						if write2 == 'Y':
							Input_text_user = input('Please, repeat this text:\n\n' + sys_text_rus_30 + '\n\n')
						elif write2 == 'N':
							os.system('cls||clear')
							print(menu)
							break
					break

# Chooce 50 words

			elif Choos_systext == '2': 
				Input_text_user = input('Please, repeat this text:\n\n' + sys_text_rus_50 + '\n\n')
				if sys_text_rus_50 == Input_text_user:
					print('WELL DONE!!!!!\n')
					while True:
						write2 = input(' Do your want again? Y/N\n')
						if write2 == 'Y':
							Input_text_user = input('Please, repeat this text:\n\n' + sys_text_rus_50 + '\n\n')
						elif write2 == 'N':
							os.system('cls||clear')
							print(menu)
							break
						else:
							print('Sorry, your loose, repeat now!')
							while True:
								write2 = input('Do your want again? Y/N\n')
								if write2 == 'Y':
									Input_text_user = input('Please, repeat this text:\n\n' + sys_text_rus_50 + '\n\n')
								elif write2 == 'N':
									os.system('cls||clear')
									print(menu)
									break
							break
					break
				else:
					print('Sorry, your loose, repeat now!\n')
					while True:
						write2 = input('Do your want again? Y/N\n')
						if write2 == 'Y':
							Input_text_user = input('Please, repeat this text:\n\n' + sys_text_rus_50 + '\n\n')
						elif write2 == 'N':
							os.system('cls||clear')
							print(menu)
							break
					break

# Chooce 150 words

			elif Choos_systext == '3': 
				Input_text_user = input('Please, repeat this text:\n\n' + sys_text_rus_150 + '\n\n')
				if sys_text_rus_150 == Input_text_user:
					print('WELL DONE!!!!!\n')
					while True:
						write2 = input(' Do your want again? Y/N\n')
						if write2 == 'Y':
							Input_text_user = input('Please, repeat this text:\n\n' + sys_text_rus_150 + '\n\n')
						elif write2 == 'N':
							os.system('cls||clear')
							print(menu)
							break
						else:
							print('Sorry, your loose, repeat now!')
							while True:
								write2 = input('Do your want again? Y/N\n')
								if write2 == 'Y':
									Input_text_user = input('Please, repeat this text:\n\n' + sys_text_rus_150 + '\n\n')
								elif write2 == 'N':
									os.system('cls||clear')
									print(menu)
									break
							break
					break
				else:
					print('Sorry, your loose, repeat now!\n')
					while True:
						write2 = input('Do your want again? Y/N\n')
						if write2 == 'Y':
							Input_text_user = input('Please, repeat this text:\n\n' + sys_text_rus_150 + '\n\n')
						elif write2 == 'N':
							os.system('cls||clear')
							print(menu)
							break
					break


			else:
				print('Sorry, try nomber again!\n')
				break

# 3 Menu
	elif write == '3':
		os.system('cls||clear')
		exit()
	else:
		print('Sorry, try nomber again!')
