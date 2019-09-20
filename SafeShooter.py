import pygame
import sys
from gamesettings import GameSettings as settings
from gamesettings import draw_stars
from Player import Player

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

	#Drawing the screen
	screen.fill([90,14,118])
	draw_stars(screen, game_settings.stars)
	screen.blit(game_settings.bg.image, game_settings.bg.rect)
	screen.blit(hero.image, hero.rect)

	#Flip the display and tick the game clock
	pygame.display.flip()
	clock.tick(game_settings.clock_tick_rate)


#Quit after exting the main game loop
sys.exit()