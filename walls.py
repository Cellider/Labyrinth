import pygame
from pygame.sprite import Sprite
from pygame.locals import *


# The values are based on how I designed the game map, they are the top left pixel x and y values
walls_dictionary = {
					'sprites/wall_1.bmp': [205, 105],
					'sprites/wall_2.bmp': [305, 15],
					'sprites/wall_3.bmp': [605, 15],
					'sprites/wall_4.bmp': [805, 15],
					'sprites/wall_5.bmp': [1005, 15],
					'sprites/wall_7.bmp': [415, 105],
					'sprites/wall_8.bmp': [405, 105],
					'sprites/wall_9.bmp': [1105, 105],
					'sprites/wall_10.bmp': [1205, 105],
					'sprites/wall_18.bmp': [905, 615],
					'sprites/wall_20.bmp': [605, 605],
					'sprites/wall_25.bmp': [205, 505],
					'sprites/wall_26.bmp': [605, 315],
					'sprites/wall_27.bmp': [705, 125],
					'sprites/wall_28.bmp': [805, 205],
					'sprites/wall_29.bmp': [1205, 305],
					'sprites/wall_30.bmp': [1005, 205],
					'sprites/wall_31.bmp': [505, 205],
					'sprites/wall_32.bmp': [405, 405],
					'sprites/wall_33.bmp': [205, 205],
					'sprites/wall_34.bmp': [105, 205],
					'sprites/wall_35.bmp': [305, 205],
					'sprites/wall_37.bmp': [705, 605],
					'sprites/wall_38.bmp': [905, 605],
					'sprites/wall_44.bmp': [815, 205],
					'sprites/wall_45.bmp': [15, 305],
					'sprites/wall_46.bmp': [905, 305],
					'sprites/wall_47.bmp': [905, 405],
					'sprites/wall_48.bmp': [1105, 405],
					'sprites/wall_49.bmp': [215, 505],
					'sprites/wall_50.bmp': [305, 605],
					'sprites/wall_51.bmp': [1105, 605],                   
					'sprites/wall_59.bmp': [515, 205],
					'sprites/wall_60.bmp': [1015, 205],
					'sprites/wall_61.bmp': [305, 305],
					'sprites/wall_62.bmp': [605, 305],
					'sprites/wall_63.bmp': [105, 405],
					'sprites/wall_64.bmp': [905, 505],
					'sprites/wall_66.bmp': [15, 605],
					'sprites/wall_70.bmp': [0, 0],
					'sprites/wall_71.bmp': [1305, 0],
					'sprites/wall_72.bmp': [15, 0],
					'sprites/wall_73.bmp': [15, 705]} 

class Wall(Sprite):
	"""Class to manage wall creation"""

	def __init__(self, game, wall_image, cords):
		"""Load game resources"""
		super().__init__()
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()
		self.settings = game.settings

		# Set the values passed as it's own
		self.wall_image = wall_image
		self.cords = cords

		# Load the wall image and get rect.
		self.image = pygame.image.load(self.wall_image)
		self.rect = self.image.get_rect()

		# Set the topleft value with the value passed
		self.rect.topleft = self.cords

	def draw(self):
		"""Draw the gun into the screen."""
		self.screen.blit(self.image, self.rect)

# Works the same way walls dictionary works, but with the center pixel
point_spawn_dictionary = {
					'sprites/spawn_1.bmp': [83, 89],
					'sprites/spawn_2.bmp': [707, 53],
					'sprites/spawn_3.bmp': [1159, 54],
					'sprites/spawn_4.bmp': [559, 260],
					'sprites/spawn_5.bmp': [1245, 257],
					'sprites/spawn_6.bmp': [449, 345],
					'sprites/spawn_7.bmp': [75, 531],
					'sprites/spawn_8.bmp': [78, 662],
					'sprites/spawn_9.bmp': [757, 667],
					'sprites/spawn_10.bmp': [1060, 662]}

class PointSpawn(Sprite):
	"""Class to manage point spawn creation"""

	def __init__(self, game, spawn_image, cords):
		"""Load game resources"""
		super().__init__()
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()
		self.settings = game.settings

		# Set values passed as it's own
		self.spawn_image = spawn_image
		self.cords = cords

		# Load the spawn image and get rect.
		self.image = pygame.image.load(self.spawn_image)
		self.rect = self.image.get_rect()

		# Set the center position with the value passed
		self.rect.center = self.cords

	def draw(self):
		"""Draw the spawn into the screen."""
		self.screen.blit(self.image, self.rect)