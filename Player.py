import pygame

class Player(pygame.sprite.Sprite):
	"""Spawn a player"""
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.image = pygame.image.load('images/better_hero_right.bmp')
		self.rect = self.image.get_rect()
		self.rect.x = screen.get_width() // 2
		self.rect.y = screen.get_height() - 100
		self.moving_left = False
		self.moving_right = False

	def update(self):
		"""Update the position and draw our player"""
		#Check for movement
		if self.moving_left and 0 < (self.rect.left):
			self.rect.x -= 5
		#!! THe problem is our character's "x" starts on its left
		#so until that left point actually exceeds get_width, itll move
		elif self.moving_right and (self.screen.get_width() > (self.rect.right)):
			self.rect.x += 5

		#Draw our player
		self.screen.blit(self.image, self.rect)


