import pygame

class Player(pygame.sprite.Sprite):
	"""Spawn a player"""
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/better_hero_right.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = screen.get_width() // 2
		self.rect.y = screen.get_height() - 100

