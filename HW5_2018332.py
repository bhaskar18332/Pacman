# NAME:- BHASKAR SINGH
# Roll No.:- 2018332
# Section: B
# Group: 05

import pygame
from pygame.locals import *
from numpy import loadtxt
import time
import os 
import random

#Constants for the game
WIDTH, HEIGHT = (32, 32)
player_score=0
WALL_COLOR = pygame.Color(0, 0, 255, 255) # BLUE
PACMAN_COLOR = pygame.Color(255, 0, 0, 255) # RED
COIN_COLOR = pygame.Color(255, 255, 0, 255) # YELLOW
DOWN = (0,1)
UP = (0,-1)
RIGHT = (1,0)
LEFT = (-1,0)
moves=[(0,1),(0,-1),(1,0),(-1,0)]

#Draws a rectangle for the wall
def draw_wall(screen, pos):
	pixels = pixels_from_points(pos)
	#pygame.draw.rect(screen, WALL_COLOR, [pixels, (WIDTH, HEIGHT)])
	screen.blit(pygame.image.load('R10962_image1.jpg'),pixels)
#Draws a rectangle for the player
def draw_pacman(screen, pos): 
	pixels = pixels_from_points(pos)
	#pygame.draw.rect(screen, PACMAN_COLOR, [pixels, (WIDTH, HEIGHT)])
	screen.blit(pygame.image.load('imgonline-com-ua-resize-9vRDQdTDt0mfk9OI.jpg'),pixels)
#Draws a rectangle for the coin
def draw_coin(screen, pos):
	pixels = pixels_from_points(pos)
	#pygame.draw.rect(screen, COIN_COLOR, [pixels, (WIDTH, HEIGHT)])
	screen.blit(pygame.image.load('imgonline-com-ua-resize-n47xXYZVViCY8u4l.jpg'),pixels)
def draw_ghost1(screen, pos): 
	pixels = pixels_from_points(pos)
	#pygame.draw.rect(screen, PACMAN_COLOR, [pixels, (WIDTH, HEIGHT)])
	screen.blit(pygame.image.load('Blinky.gif'),pixels)
def draw_ghost2(screen, pos): 
	pixels = pixels_from_points(pos)
	#pygame.draw.rect(screen, PACMAN_COLOR, [pixels, (WIDTH, HEIGHT)])
	screen.blit(pygame.image.load('imgonline-com-ua-resize-RFQW8KEMyD35u.jpg'),pixels)
def draw_ghost3(screen, pos): 
	pixels = pixels_from_points(pos)
	#pygame.draw.rect(screen, PACMAN_COLOR, [pixels, (WIDTH, HEIGHT)])
	screen.blit(pygame.image.load('imgonline-com-ua-resize-nSEoEMVrEvbL3.jpg'),pixels)
def score(player_score,live):
	myfont=pygame.font.SysFont(None,25)
	Name=myfont.render("BHASKAR SINGH", True, (255,255,255))
	Score=myfont.render("score"+":"+str(player_score),True,(255,255,255))
	lives=myfont.render("Lives: "+str(live),True,(255,255,255))
	screen.blit(Name,(650,270))
	screen.blit(Score,(650,290))
	screen.blit(lives,(750,2))
	

#Uitlity functions
def add_to_pos(pos, pos2):
	return (pos[0]+pos2[0], pos[1]+pos2[1])
def pixels_from_points(pos):
	return (pos[0]*WIDTH, pos[1]*HEIGHT)


#Initializing pygame
pygame.init()
screen = pygame.display.set_mode((850,600), 0, 32)
background = pygame.surface.Surface((850,600)).convert()


#Initializing variables
layout = loadtxt('layout.txt', dtype=str)
rows, cols = layout.shape
pacman_position = (1,1)
ghost1_position=(17,17)
ghost2_position=(18,1)
ghost3_position=(3,17)
background.fill((0,0,0))
live=5

coins=[]
walls=[]

# Main game loop
for col in range(cols):
		for row in range(rows):
			value = layout[row][col]
			pos = (col, row)
			if value == 'w':
				walls.append(pos)
			elif value == 'c':
				coins.append(pos)
#print(coins)#check
#print(walls)#check
while (live>0) and len(coins)!=0:
	#print(live)#check
	coins=[]
	move_direction=(0,0)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type ==pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				move_direction=LEFT
			elif event.key == pygame.K_RIGHT:
				move_direction = RIGHT
			elif event.key == K_UP:
				move_direction=UP
			elif event.key == K_DOWN:
				move_direction = DOWN

	move_ghost1=random.choice(moves)
	move_ghost2=random.choice(moves)
	move_ghost3=random.choice(moves)
	screen.blit(background, (0,0))

	#Draw board from the 2d layout array.
  #In the board, '.' denote the empty space, 'w' are the walls, 'c' are the coins
	for col in range(cols):
		for row in range(rows):
			value = layout[row][col]
			pos = (col, row)
			if value == 'w':
				draw_wall(screen, pos)
			elif value == 'c':
				draw_coin(screen, pos)
	
	#print(g1)#check
	if pacman_position in walls:
	
		pacman_position=p1
	
	if ghost1_position in walls:

		ghost1_position=g1
	
	if ghost2_position in walls:
		
		ghost2_position=g2
	
	if ghost3_position in walls:
	
		ghost3_position=g3

	#Draw the player
	draw_pacman(screen, pacman_position)
	draw_ghost1(screen,ghost1_position)
	draw_ghost2(screen,ghost2_position)
	draw_ghost3(screen,ghost3_position)
	g1=ghost1_position
	g2=ghost2_position
	g3=ghost3_position
	p1=pacman_position
	

	if (pacman_position==ghost3_position or pacman_position==ghost2_position or pacman_position== ghost1_position):
		pacman_position=(1,1)
		live-=1
	#TODO: Take input from the user and update pacman moving direction, Currently hardcoded to always move down
	

	
	
	
	#Update player position based on movement.
	ghost1_position=add_to_pos(ghost1_position,move_ghost1)
	ghost2_position=add_to_pos(ghost2_position,move_ghost2)
	ghost3_position=add_to_pos(ghost3_position,move_ghost3)
	pacman_position = add_to_pos(pacman_position, move_direction)

	
	#TODO: Check if player ate any coin, or collided with the wall by using the layout array.
	# player should stop when colliding with a wall
	# coin should dissapear when eating, i.e update the layout array
	
	for col in range(cols):
		for row in range(rows):
			value = layout[row][col]
			pos = (col, row)
			if value == 'c':
				coins.append(pos)


	if pacman_position in coins:
		col=pacman_position[0]
		row=pacman_position[1]
		layout[row][col]='.'
		player_score+=1


	#Update the display
	score(player_score,live)
	pygame.display.update()
	
	#Wait for a while, computers are very fast.
	time.sleep(0.01)
	
