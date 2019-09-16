import pygame

#http://www.petercollingridge.co.uk/tutorials/pygame-physics-simulation/creating-pygame-window/

#Game window settings
dimensions = (300,200)
screen = pygame.display.set_mode(dimensions)
pygame.display.flip()


#Game loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False