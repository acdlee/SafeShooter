import pygame
from gamesettings import draw_stars

def draw_to_screen(screen, game_settings, hero, clock):
	#Drawing the screen
	screen.fill([90,14,118])
	draw_stars(screen, game_settings.stars)
	screen.blit(game_settings.bg.image, game_settings.bg.rect)
	# screen.blit(hero.image, hero.rect)
	#draw the hero in the actual hero class with update()
	#^allows for us to update movement
	hero.update()

	#Flip the display and tick the game clock
	pygame.display.flip()
	clock.tick(game_settings.clock_tick_rate)