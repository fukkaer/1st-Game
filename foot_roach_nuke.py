# -*- coding: cp1252 -*-
#error list: error02= rpgg output is outside 1-3, error03=quit command malfunctioning
def rpgg():
	import random
	hand = random.randint(1,3)
	return hand
def p1opt():
	print('you chose:',userinput)
def cpuoption():
	if rpgg() == 1:
		return('computer chose: foot')
	elif rpgg() == 2:
		return('computer chose: nuke')
	elif rpgg() == 3:
		return('computer chose: cockroach')
def wordinstring(acceptedwordlist,wordliststring):
	return set(acceptedwordlist).intersection(wordliststring.split())
acceptedwordlist = ['Quit','quit','foot','Foot','cockroach','Cockroach','nuke','Nuke']
wordliststring = 'Quit quit foot Foot Cockroach cockroach nuke Nuke'
p1win = 0
p1loss = 0
p1tie = 0
totalrounds = 0
loop = True
while loop == True:
	userinput = input("foot, nuke or cockroach? (quit ends): ")
	rpgg()
	if userinput == 'Foot' or userinput == 'foot':
		p1opt()
		print(cpuoption())
		if rpgg() == 1:
			print('it is a tie!')
			p1tie += 1
		elif rpgg() == 3:
			print('you win!')
			p1win += 1
		elif rpgg() == 2:
			print('you lose!')
			p1loss += 1
		elif rpgg() != 1 or rpgg() != 2 or rpgg != 3:
			print('ERROR 02')
			print('rpgg_output',rpgg())
		totalrounds += 1
	elif userinput == 'Cockroach' or userinput == 'cockroach':
		p1opt()
		print(cpuoption())
		if rpgg() == 1:
			print('you lose!')
			p1loss += 1
		elif rpgg() == 3:
			print('it is a tie!')
			p1tie += 1
		elif rpgg() == 2:
			print('you win!')
			p1win += 1
		elif rpgg() != 1 or rpgg() != 2 or rpgg() != 3:
			print('ERROR 02')
			print('rpgg_output',rpgg())
		totalrounds += 1
	elif userinput == 'Nuke' or userinput == 'nuke':
		p1opt()
		print(cpuoption())
		if rpgg() == 1:
			print('you win!')
			p1win += 1
			print(rpgg())
		elif rpgg() == 3:
			print('you lose!')
			p1loss += 1
			print(rpgg())
		elif rpgg() == 2:
			print('both lose!')
			p1loss += 1
			print(rpgg())
		elif rpgg() != 1  or rpgg() != 2 or rpgg() != 3:
			print('ERROR 02')
			print('rpgg_output',rpgg())
		totalrounds += 1
	elif userinput == 'Quit' or userinput == 'quit':
		break
		loop == False
		print('ERROR03')
	elif userinput != wordinstring:
		print('incorrect selection.')
print('you played',totalrounds,'rounds, and won',p1win,'rounds, playing tie in',p1tie,'rounds.')
