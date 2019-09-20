import pygame
import sys
from gamesettings import GameSettings as settings
from Player import Player
from illustrate import draw_to_screen

#initialize game engine
pygame.init()

#initialize the game settings, screen, and clock
game_settings = settings()
screen = pygame.display.set_mode(game_settings.dimensions)
pygame.display.set_caption('SafeShooter')
clock = pygame.time.Clock()

#Our Hero
hero = Player(screen)

#Game loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	#Once finished check for events, let's update the screen
	draw_to_screen(screen, game_settings, hero, clock)


#Quit after exting the main game loop
sys.exit()