import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Player(Sprite):
	"""Class to manage player aspects."""

	def __init__(self, game):
		"""Initiate player, initial positions and game resources"""
		super().__init__()
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()
		self.settings = game.settings

		# Load the player image and get rect.
		self.image_location = 'sprites/player_up.bmp'
		self.image = pygame.image.load(self.image_location)
		self.rect = self.image.get_rect()

		# Store a decimal value for the player X, Y position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flag.
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		# Collision flags
		self.right_wall_collision = False
		self.up_wall_collision = False
		self.left_wall_collision = False
		self.down_wall_collision = False

	def change_sprite_direction(self):
		"""Change sprite according to direction"""
		if self.moving_up:
			self.image_location = 'sprites/player_up.bmp'
		if self.moving_down:
			self.image_location = 'sprites/player_down.bmp'
		if self.moving_left:
			self.image_location ='sprites/player_left.bmp'
		if self.moving_right:
			self.image_location = 'sprites/player_right.bmp'

	def update(self):
		self.change_sprite_direction()
		"""Update the player's position based on movement flag"""
		# We will first update the X and Y value and then turn into the rect value
		# No elif or also, so that no line take priority

		if self.moving_right and not self.right_wall_collision:
			# Will only run if the player is moving right and is not at the right edge of screen
			self.x += self.settings.player_speed

		if self.moving_left and not self.left_wall_collision:
			#Same thing as above but with left edge
			self.x -= self.settings.player_speed

		if self.moving_up and not self.up_wall_collision:
			# Same thing as above but with top of the screen
			self.y -= self.settings.player_speed

		if self.moving_down and not self.down_wall_collision:
			# Same thing as above but with bottom of the screen
			self.y += self.settings.player_speed

		# Update rect using values stored in self.x and self.y
		self.rect.x = self.x
		self.rect.y = self.y

		# Update the player sprite
		self.image = pygame.image.load(self.image_location)

	def draw(self):
		"""Draw the player into the screen at current position"""
		self.screen.blit(self.image, self.rect)

	def center_player(self):
		"""Put the player on center of the map"""
		self.rect.center = [760, 508]
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)