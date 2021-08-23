import sys, pygame
from random import randint

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)



win = pygame.display.set_mode((320,320))
pygame.display.set_caption("SNEK 1337:69")

#initialise vars
x = 160
y = 160
foodx = randint(0, 30) * 10
foody = randint(0, 30) * 10
foodeaten = False
modx = 0
mody = 0
direction = 0
width = 10
height = 10
vel = 10
stack = [[x, y],[x, y],[x, y],[x, y],[x, y],[x, y],[x, y],[x, y],[x, y],[x, y]]
snek = 10
counter = 0
cangoleft = True
cangoright = True
cangoup = True
cangodown = True
score = 'SCORE: '
speed = 100
points = 0
levelup = False

def snake():
	for coord in stack:
		oldx,oldy = coord
		pygame.draw.rect(win, (255, 0, 0), (oldx, oldy, width, height))

run = True
while run:
	
	if points >= 10:
		speed = 90
	if points >= 20:
		speed = 80
	if points >= 30:
		speed = 70
	if points >= 40:
		speed = 60
	if points >= 50:
		speed = 50
	
	pygame.time.delay(speed)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()
	
	#controls
	if keys[pygame.K_LEFT] and cangoleft == True:
		modx = vel * -1
		mody = 0
		direction = 3
		cangoright = False
		cangoleft = True
		cangoup = True
		cangodown = True
	if keys[pygame.K_RIGHT] and cangoright ==True:
		modx = vel
		mody = 0
		direction = 4
		cangoright = True
		cangoleft = False
		cangoup = True
		cangodown = True
	if keys[pygame.K_UP] and cangoup == True:
		modx = 0
		mody =  vel * -1
		direction = 1
		cangoright = True
		cangoleft = True
		cangoup = True
		cangodown = False
	if keys[pygame.K_DOWN] and cangodown == True:
		mody = vel
		modx = 0
		direction = 2
		cangoright = True
		cangoleft = True
		cangoup = False
		cangodown = True	
	"""
	#cheat
	if keys[pygame.K_SPACE]:
		foodx = randint(1, 31) * 10
		foody = randint(1, 31) * 10
		snek = snek + 1
		stack.append(stack[snek - 2])
	"""
	win.fill((0,0,0))
	points = snek - 10
	currentscore = myfont.render(score + str(points) + 'LEVEL: ' + str((100 - speed) / 10), False, (125, 125, 125))
	win.blit(currentscore,(0,0))
	
	#draw initial snake
	pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
	#draw food
	pygame.draw.rect(win, (255, 125, 0), (foodx, foody, width, height))
	
	stack[counter] = [x, y]
	counter = counter + 1
	if counter == snek:
		counter = 0
		
	x = x + modx
	y = y + mody
	
	#allow snake to reappear on opposite side when crossing the boundaries
	if x < 0 and direction == 3:
		x = 320
	if x > 310 and direction == 4:
		x = 0
	if y < 0 and direction == 1:
		y = 320
	if y > 310 and direction == 2:
		y = 0
	
	i = 0
	
	#food is eaten
	if x == foodx and y == foody:
		foodx = randint(1, 28) * 10
		foody = randint(1, 28) * 10
		snek = snek + 1
		stack.append(stack[snek - 2])
	#draw snake
	snake()
	
	#check if snake is kill and reset game
	for stuff in stack:
		if stuff == [x, y]:
			win.fill((0,0,0))
			x = 160
			y = 160
			modx = 0
			mody = 0
			direction = 0
			width = 10
			height = 10
			vel = 10
			stack = [[x, y],[x, y],[x, y],[x, y],[x, y],[x, y],[x, y],[x, y],[x, y],[x, y]]
			snek = 10
			counter = 0
			cangoleft = True
			cangoright = True
			cangoup = True
			cangodown = True
			speed = 100
			points = 0
			levelup = False
			pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
			
	pygame.display.update()

pygame.quit()