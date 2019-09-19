import pygame
from background import Background
import random as rand

class GameSettings():
	"""GameSettings for SafeShooter"""
	def __init__(self):
		#Window settings/tick rate/background image
		self.width = 1000
		self.height = 600
		self.dimensions = (self.width, self.height)
		self.clock_tick_rate = 30
		self.bg = Background('images/forest_background.bmp', [0,0])

		#initiliaze our stars
		self.stars = self.stargazing()

	#Create the list of star locations
	def stargazing(self):
		star_list = []
		for i in range(100):
			x = rand.randrange(0, self.width)
			y = rand.randrange(0, 500)
			star_list.append([x, y])

		return star_list

#This function draws our stars to the screen
def draw_stars(surface, stars):
	n = len(stars)
	star_size = 3
	colors = [(255,255,255), (255,215,0)]

	#Drawing the stars to the screen
	for i in range(n):
		starColor = rand.randrange(0,2)
		color = colors[starColor]
		shimmer = rand.randrange(0, star_size)
		pygame.draw.circle(surface, color, stars[i], shimmer)
		
