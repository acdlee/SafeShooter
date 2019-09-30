import pygame
import sys

def event_checker(hero):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				hero.moving_left = True
			elif event.key == pygame.K_RIGHT or event.key == ord('d'):
				hero.moving_right = True
			elif event.key == pygame.K_UP or event.key == ord('w'):
				print('jump')
			elif event.key == ord('q'):
				sys.exit()
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == ord('a'):
				hero.moving_left = False
			elif event.key == pygame.K_RIGHT or event.key == ord('d'):
				hero.moving_right = False
			elif event.key == pygame.K_UP or event.key == ord('w'):
				print('stop jump')