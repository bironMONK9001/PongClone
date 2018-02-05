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

	#Ball Movement
	if UPLEFT:
		ball.top -= MOVESPEED
		ball.left -= MOVESPEED
	if UPRIGHT:
		ball.top += MOVESPEED
		ball.left -= MOVESPEED
	if DOWNLEFT:
		ball.top += MOVESPEED 
		ball.left-= MOVESPEED
	if DOWNRIGHT:
		ball.top += MOVESPEED
		ball.left += MOVESPEED
	
	#Draw game objects
	pygame.draw.rect(windowSurface, WHITE, playerPaddle)
	pygame.draw.rect(windowSurface, WHITE, enemyPaddle)
	pygame.draw.rect(windowSurface, WHITE, ball)

	pygame.display.update()
	mainClock.tick(60)
