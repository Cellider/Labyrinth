import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Point(Sprite):
	"""Class to manage point"""

	def __init__(self, game, spawn_point):
		super().__init__()
		"""Get the screen and settings"""
		self.screen = game.screen
		self.settings = game.settings

		# Initiate the random value as its own
		self.spawn_point = spawn_point

		# Load the point image and set it's rect
		self.image = pygame.image.load('sprites/point.bmp')
		self.rect = self.image.get_rect()
		self.rect.center = self.spawn_point

	def draw(self):
		"""Draw the point into the screen"""
		self.screen.blit(self.image, self.rect)
