from objects import Mand, Coin, Laser1, Laser2, Laser3, Beam, Dragon, Ball, Background, Speed, Magnet
from board import Board, pos
from getch import KBHit
from time import time,sleep
from random import randint
import sys
import os

bgh = 50
bgb = 200

usrh = 20
usrb = 7

bg = Board(bgb, bgh)
enemy = 0
usr = Mand(usrb, usrh, bg)
bg1 = Background(0, 0, bg)
bg2 = Background(100, 0, bg)

gch = KBHit()

st = time()
sleep(1)

st1 = time()
sleep(1)

st2 = time()
sleep(1)

st3 = time()

start = time()
sptime = time() + 13074197

stf = 0

score = 0
lives = 5
dlives = 5

co = 0
numc = 0

l1 = 0
numl1 = 0

l2 = 0
numl2 = 0

l3 = 0
numl3 = 0

blt = 0
ice = 0

spd = 0
speed = 0
done = 0
done1 = 0

sh = 0
shend = 0

mag = 0;
mgtime = time() + 13408494

obs = ['|', '\\', '-', ' ', 'O']

while 1:
	usr.down()
	bg.make()

	print('%s%s%s' % (pos(50,5),"Score : ",score))
	print('%s%s%s' % (pos(51,5), "Lives : ",lives))
	print('%s%s%s' % (pos(52,5),"Shield : ",sh))
	print('%s%s%s' % (pos(53,5),"Dragon : ",dlives))

	if sh and time() - shst > 10:
		sh = 0
		shend = time()

	if speed == 0:
		timelast = 5
	else:
		timelast = 3
	
	if time() - st > timelast and numc < 10:
		co = Coin(190, randint(25, 45), bg)
		numc = numc + 1
		st = time()
	if co and co.x > 1:
		co.left(speed)
		if bg.grid[co.y][co.x-1] not in obs:
			score = score + 1
			bg.grid[co.y][co.x] = ' '
			co = 0
	else:
		if co:
			bg.grid[co.y][co.x] = ' '
		co = 0

	if time() - st1 > timelast and numl1 < 10:
		l1 = Laser1(190, randint(25, 45), bg)
		numl1 = numl1 + 1
		st1 = time()
	if l1 and l1.x > 1:
		l1.left(speed)
		if bg.grid[l1.y][l1.x-3] not in obs or bg.grid[l1.y+3][l1.x-3] not in obs or bg.grid[l1.y+1][l1.x-3] not in obs or bg.grid[l1.y+2][l1.x-3] not in obs:
			if sh == 0:
				if bg.grid[l1.y][l1.x-3] != '>' or bg.grid[l1.y+1][l1.x-3] != '>' or bg.grid[l1.y+2][l1.x-3] != '>' or bg.grid[l1.y+3][l1.x-3] != '>':
					lives = lives - 1
			bg.grid[l1.y][l1.x] = ' '
			bg.grid[l1.y+1][l1.x] = ' '
			bg.grid[l1.y+2][l1.x] = ' '
			bg.grid[l1.y+3][l1.x] = ' '
			l1 = 0
		elif bg.grid[l1.y][l1.x-2] not in obs or bg.grid[l1.y+3][l1.x-2] not in obs or bg.grid[l1.y+1][l1.x-3] not in obs or bg.grid[l1.y+2][l1.x-3] not in obs:
			if sh == 0:
				if bg.grid[l1.y][l1.x-2] != '>' or bg.grid[l1.y+1][l1.x-2] != '>' or bg.grid[l1.y+2][l1.x-2] != '>' or bg.grid[l1.y+3][l1.x-2] != '>':
					lives = lives - 1
			bg.grid[l1.y][l1.x] = ' '
			bg.grid[l1.y+1][l1.x] = ' '
			bg.grid[l1.y+2][l1.x] = ' '
			bg.grid[l1.y+3][l1.x] = ' '
			l1 = 0
		elif bg.grid[l1.y][l1.x-2] not in obs or bg.grid[l1.y+3][l1.x-2] not in obs or bg.grid[l1.y+1][l1.x-3] not in obs or bg.grid[l1.y+2][l1.x-3] not in obs:
			if sh == 0:
				if bg.grid[l1.y][l1.x-1] != '>' or bg.grid[l1.y+1][l1.x-1] != '>' or bg.grid[l1.y+2][l1.x-1] != '>' or bg.grid[l1.y+3][l1.x-1] != '>':
					lives = lives - 1
			bg.grid[l1.y][l1.x] = ' '
			bg.grid[l1.y+1][l1.x] = ' '
			bg.grid[l1.y+2][l1.x] = ' '
			bg.grid[l1.y+3][l1.x] = ' '
			l1 = 0
	else:
		if l1:
			bg.grid[l1.y][l1.x] = ' '
			bg.grid[l1.y+1][l1.x] = ' '
			bg.grid[l1.y+2][l1.x] = ' '
			bg.grid[l1.y+3][l1.x] = ' '
		l1 = 0

	if time() - st2 > timelast and numl2 < 10:
		l2 = Laser2(190, randint(25, 45), bg)
		numl2 = numl2 + 1
		st2 = time()	
	if l2 and l2.x > 1:
		l2.left(speed)
		if bg.grid[l2.y][l2.x-3] not in obs or bg.grid[l2.y+1][l2.x-3] not in obs:
			if sh == 0:
				if bg.grid[l2.y][l2.x-3] != '>' or bg.grid[l2.y+1][l2.x-3] != '>':
					lives = lives - 1
			bg.grid[l2.y][l2.x] = ' '
			bg.grid[l2.y][l2.x+1] = ' '
			bg.grid[l2.y][l2.x+2] = ' '
			bg.grid[l2.y][l2.x+3] = ' '	
			bg.grid[l2.y+1][l2.x] = ' '
			bg.grid[l2.y+1][l2.x+1] = ' '
			bg.grid[l2.y+1][l2.x+2] = ' '
			bg.grid[l2.y+1][l2.x+3] = ' '		
			l2 = 0
		elif bg.grid[l2.y][l2.x-2] not in obs or bg.grid[l2.y+1][l2.x-2] not in obs:
			if sh == 0:
				if bg.grid[l2.y][l2.x-2] != '>' or bg.grid[l2.y+1][l2.x-2] != '>':
					lives = lives - 1
			bg.grid[l2.y][l2.x] = ' '
			bg.grid[l2.y][l2.x+1] = ' '
			bg.grid[l2.y][l2.x+2] = ' '
			bg.grid[l2.y][l2.x+3] = ' '
			bg.grid[l2.y+1][l2.x] = ' '
			bg.grid[l2.y+1][l2.x+1] = ' '
			bg.grid[l2.y+1][l2.x+2] = ' '
			bg.grid[l2.y+1][l2.x+3] = ' '	
			l2 = 0
		elif bg.grid[l2.y][l2.x-1] not in obs or bg.grid[l2.y+1][l2.x-2] not in obs:
			if sh == 0:
				if bg.grid[l2.y][l2.x-1] != '>' or bg.grid[l2.y+1][l2.x-1] != '>':
					lives = lives - 1
			bg.grid[l2.y][l2.x] = ' '
			bg.grid[l2.y][l2.x+1] = ' '
			bg.grid[l2.y][l2.x+2] = ' '
			bg.grid[l2.y][l2.x+3] = ' '
			bg.grid[l2.y+1][l2.x] = ' '
			bg.grid[l2.y+1][l2.x+1] = ' '
			bg.grid[l2.y+1][l2.x+2] = ' '
			bg.grid[l2.y+1][l2.x+3] = ' '	
			l2 = 0
	else:
		if l2:
			bg.grid[l2.y][l2.x] = ' '
			bg.grid[l2.y][l2.x+1] = ' '
			bg.grid[l2.y][l2.x+2] = ' '
			bg.grid[l2.y][l2.x+3] = ' '
			bg.grid[l2.y+1][l2.x] = ' '
			bg.grid[l2.y+1][l2.x+1] = ' '
			bg.grid[l2.y+1][l2.x+2] = ' '
			bg.grid[l2.y+1][l2.x+3] = ' '	
		l2 = 0

	if time() - st3 > timelast and numl3 < 10:
		l3 = Laser3(190, randint(25, 45), bg)
		numl3 = numl3 + 1
		st3 = time()
	if l3 and l3.x > 1:
		l3.left(speed)
		if bg.grid[l3.y][l3.x-3] not in obs or bg.grid[l3.y+1][l3.x-3] not in obs or bg.grid[l3.y+2][l3.x-3] not in obs or bg.grid[l3.y+3][l3.x-3] not in obs:
			if sh == 0: 
				if bg.grid[l3.y][l3.x-3] != '>' or bg.grid[l3.y+1][l3.x-3] != '>' or bg.grid[l3.y+2][l3.x-3] != '>' or bg.grid[l3.y+3][l3.x-3] != '>':
					lives = lives - 1
			bg.grid[l3.y][l3.x] = ' '
			bg.grid[l3.y+1][l3.x+1] = ' '
			bg.grid[l3.y+2][l3.x+2] = ' '
			bg.grid[l3.y+3][l3.x+3] = ' '			
			l3 = 0		

		elif bg.grid[l3.y][l3.x-2] not in obs or bg.grid[l3.y+1][l3.x-2] not in obs or bg.grid[l3.y+2][l3.x-2] not in obs or bg.grid[l3.y+3][l3.x-2] not in obs:
			if sh == 0:
				if bg.grid[l3.y][l3.x-2] != '>' or bg.grid[l3.y+1][l3.x-2] != '>' or bg.grid[l3.y+2][l3.x-2] != '>' or bg.grid[l3.y+3][l3.x-2] != '>':
					lives = lives - 1
			bg.grid[l3.y][l3.x] = ' '
			bg.grid[l3.y+1][l3.x+1] = ' '
			bg.grid[l3.y+2][l3.x+2] = ' '
			bg.grid[l3.y+3][l3.x+3] = ' '			
			l3 = 0
		elif bg.grid[l3.y][l3.x-1] not in obs or bg.grid[l3.y+1][l3.x-1] not in obs or bg.grid[l3.y+2][l3.x-1] not in obs or bg.grid[l3.y+3][l3.x-1] not in obs:
			if sh == 0:
				if bg.grid[l3.y][l3.x-1] != '>' or bg.grid[l3.y+1][l3.x-1] != '>' or bg.grid[l3.y+2][l3.x-1] != '>' or bg.grid[l3.y+3][l3.x-1] != '>':
					lives = lives - 1
			bg.grid[l3.y][l3.x] = ' '
			bg.grid[l3.y+1][l3.x+1] = ' '
			bg.grid[l3.y+1][l3.x+2] = ' '
			bg.grid[l3.y+1][l3.x+3] = ' '		
			l3 = 0
	else:
		if l3:
			bg.grid[l3.y][l3.x] = ' '
			bg.grid[l3.y+1][l3.x+1] = ' '
			bg.grid[l3.y+1][l3.x+2] = ' '
			bg.grid[l3.y+1][l3.x+3] = ' '		
		l3 = 0
	if blt and blt.x < 193:
		blt.right(speed)
		if bg.grid[blt.y][blt.x+4] != ' ' and enemy != 0 and blt.x < 189:
			if bg.grid[blt.y][blt.x+4] != '*':
				dlives = dlives - 1
			bg.grid[blt.y][blt.x] = ' '
			bg.grid[blt.y][blt.x+1] = ' '
			bg.grid[blt.y][blt.x+2] = ' '
			bg.grid[blt.y][blt.x+3] = ' '
			blt = 0
	else:
		if blt:
			bg.grid[blt.y][blt.x] = ' '
			bg.grid[blt.y][blt.x+1] = ' '
			bg.grid[blt.y][blt.x+2] = ' '
			bg.grid[blt.y][blt.x+3] = ' '		
		blt = 0

	if ice and ice.x > 5:
		ice.left()
		if bg.grid[ice.y][ice.x-1] != ' ' and ice.x > 7:
			if bg.grid[ice.y][ice.x-1] != '>' and sh == 0:
				lives = lives - 2
			bg.grid[ice.y][ice.x] = ' '
			ice = 0
	else:
		if ice:
			bg.grid[ice.y][ice.x] = ' '
		ice = 0

	if lives <= 0:
		print(f"{pos(20, 100)}YOU LOSE") 
		sleep(2)
		break;
	if dlives <= 0:
		print(f"{pos(20, 100)}YOU WIN")
		sleep(2) 
		break
	
	if numl1 >= 10 and numl2 >=10 and numl3 >=10:
		enemy = Dragon(150, usr.y - 5, bg)	
		if time() - stf > 5:
			ice = Ball(enemy.x, enemy.y + 5, bg)
			stf = time()
	
	if time() - start > 5 and done == 0:
		mag = Magnet(randint(65, 135), randint(15, 35), bg)
		done = 1
		mgtime = time()

	if mag:
		bg.grid[mag.y][mag.x] = ' '
		bg.grid[mag.y][mag.x+1] = ' '
		bg.grid[mag.y][mag.x+2] = ' '
		mag = Magnet(mag.x, mag.y, bg)
		if mag.x > usr.x:
			usr.right(1)
		elif mag.x < usr.x:
			usr.left(1)
		if mag.y > usr.y:
			usr.down(1)
		elif mag.y < usr.y:
			usr.up(1)

	if mag and time() - mgtime > 10:
		bg.grid[mag.y][mag.x] = ' '
		bg.grid[mag.y][mag.x+1] = ' '
		bg.grid[mag.y][mag.x+2] = ' '
		mag = 0

	if time() - start > 20 and done1 == 0:
		spd = Speed(190, 25, bg)
		done1 = 1

	if spd and spd.x > 5:
		spd.left()
		if bg.grid[spd.y][spd.x-1] not in obs and spd.x > 7:
			bg.grid[spd.y][spd.x] = ' '
			bg.grid[spd.y][spd.x+1] = ' '
			bg.grid[spd.y][spd.x+2] = ' '
			spd = 0
			speed = 1
			sptime = time()
	else:
		if spd:
			bg.grid[spd.y][spd.x] = ' '
			bg.grid[spd.y][spd.x+1] = ' '
			bg.grid[spd.y][spd.x+2] = ' '
		spd = 0	

	if spd and time() - sptime > 10:
		speed = 0
		spd = 0

	inp = gch.getinput()
	if inp == 'w':
		usr.up()
		if enemy:
			enemy.rem()
	elif inp == 'a':
		usr.left()
	elif inp == 'd':
		usr.right()
	elif inp == ' ' and time() - shend > 60:
		sh = 1
		shst = time()
	elif inp == 'p':
		blt = Beam(usr.x+1, usr.y, bg)
	elif inp == 'q':
		break
