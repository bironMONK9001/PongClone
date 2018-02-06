#This is a pong clone written by Max Ferguson


import sys, pygame, random
from pygame.locals import *
mainClock = pygame.time.Clock()

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('PONG')

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Game objects
playerPaddle = pygame.Rect(0, 200, 30, 150)
enemyPaddle = pygame.Rect(610, 200, 30,150)
ball = pygame.Rect(270, 190, 25, 25)

#Paddle Movement
moveUp = False
moveDown = False

#Ball Movement
UPLEFT = True
UPRIGHT = False
DOWNLEFT = False
DOWNRIGHT = False

MOVESPEED = 6
BALLSPEED = 1

#Game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

		if event.type == KEYDOWN:
			if event.key == K_UP or event.key == K_w:
				moveUp = True
				moveDown = False
			if event.key == K_DOWN or event.key == K_s:
				moveUp = False 
				moveDown = True 

		if event.type == KEYUP:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			
			if event.key == K_UP or event.key == K_w:
				moveUp = False
			if event.key == K_DOWN or event.key == K_s:
				moveDown= False

	#Background
	windowSurface.fill(BLACK)

	#Move Player
	if moveUp and playerPaddle.top > 0:
		playerPaddle.top -= MOVESPEED
	if moveDown and playerPaddle.top < WINDOWHEIGHT - 150:
		playerPaddle.top += MOVESPEED
	
	#Collision detection
	if ball.top < 0:
		if UPLEFT == True:
			UPLEFT = False
			DOWNLEFT = True
			BALLSPEED += 1
		if UPRIGHT == True:
			UPRIGHT = False
			DOWNRIGHT = True
			BALLSPEED += 1
	if ball.top > WINDOWHEIGHT:
		if DOWNLEFT == True:
			DOWNLEFT = False 
			UPLEFT = True
			BALLSPEED += 1
		if DOWNRIGHT == True:
			DOWNRIGHT = False
			UPRIGHT = True
			BALLSPEED += 1
	
	if ball.left < 0 or ball.left > WINDOWWIDTH:
		BALLSPEED = 0

	#Ball Movement
	if UPLEFT:
		ball.top -= BALLSPEED
		ball.left -= BALLSPEED
	if UPRIGHT:
		ball.top += BALLSPEED
		ball.left -= BALLSPEED
	if DOWNLEFT:
		ball.top += BALLSPEED 
		ball.left-= BALLSPEED
	if DOWNRIGHT:
		ball.top += BALLSPEED
		ball.left += BALLSPEED
	
	#Draw game objects
	pygame.draw.rect(windowSurface, WHITE, playerPaddle)
	pygame.draw.rect(windowSurface, WHITE, enemyPaddle)
	pygame.draw.rect(windowSurface, WHITE, ball)

	pygame.display.update()
	mainClock.tick(60)
