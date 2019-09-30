import pygame
import sys
from gamesettings import GameSettings as settings
from Player import Player
from illustrate import draw_to_screen
from event_check import event_checker

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
while True:
	event_checker(hero)

	#Once finished check for events, let's update the screen
	draw_to_screen(screen, game_settings, hero, clock)


