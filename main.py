import sys
import pygame
from random import choice

from settings import Settings
from player import Player
from point import Point
from game_stats import GameStats
from button import PlayButton, ContinueButton, RestartButton, QuitButton
from scoreboard import Scoreboard
from walls import walls_dictionary, Wall, point_spawn_dictionary, PointSpawn

class Labyrinth:
	"""Class to manage the main part of the game code."""

	def __init__(self):
		"""Initialize the game, create and store game resources."""

		# Set the game windom size, the value is the size I made the game map
		# I then set it on fullscreen if you game a small monitor like mine
		self.screen = pygame.display.set_mode((1320, 720), pygame.FULLSCREEN)
		# Set a text on game window
		pygame.display.set_caption('Labyrinth')
		self.screen_image = pygame.image.load('sprites/background.bmp')


		# Create instance to store settings, game stats and scoreboard
		self.settings = Settings()
		self.stats = GameStats(self)
		self.sb = Scoreboard(self)

		# Create and stores the object of the game
		self.player = Player(self)
		self.enemies_list = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()
		self.walls_list =  pygame.sprite.Group()
		self.spawn_list = pygame.sprite.Group()
		self.point_list = pygame.sprite.Group()

		# Make the menu buttons.
		self.play_button = PlayButton(self, 'PLAY')
		self.continue_button =  ContinueButton(self, 'CONTINUE')
		self.restart_button = RestartButton(self, 'RESTART')
		self.quit_button =  QuitButton(self, 'QUIT')

		# Call functions that only need to be called once
		self.create_walls()
		self.create_point_spawn()
		# Call the first point to spawn
		self.create_point()

		# Sets the flag for pausing the game
		self.game_paused = False
	
	def run_game(self):
		"""Start the main loop events and respond to them"""

		while True:
			# Check for event first so we can know when the player click the start button
			self._check_events()

			self._update_screen()
			# We update the screen before anything else so the player can see the game before clicking the start button
			if self.stats.game_active == True and not self.game_paused:
				self.player.update()
				self._check_player_wall_collision()
				self._check_player_point_collision()

	def _check_events(self):
		"""Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)
				self._check_continue_button(mouse_pos)
				self._check_quit_button(mouse_pos)
				self._check_restart_button(mouse_pos)

	def create_walls(self):
		"""Create the walls on the game by getting each x and y value assigned with the image on a dictionary"""
		walls_temp_list = list(walls_dictionary.keys())
		for wall in walls_temp_list:
			cords = walls_dictionary.get(wall)
			# Create a wall and pass the values
			new_wall = Wall(self, wall, cords)
			# Add the walls created to a list
			self.walls_list.add(new_wall)

	def create_point_spawn(self):
		"""Create the spots that the points using the same method as the walls"""
		spawn_temp_list = list(point_spawn_dictionary.keys())
		for spawn in spawn_temp_list:
			cords = point_spawn_dictionary.get(spawn)
			# Create a spawn and pass the values
			new_spawn = PointSpawn(self, spawn, cords)
			# Add the spawns created to a list
			self.spawn_list.add(new_spawn)


	def _check_play_button(self, mouse_pos):
		"""Start a new game when the player clicks PLAY."""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)

		if button_clicked and not self.stats.game_active:
			# Reset the game settings
			self.stats.reset_stats()
			self.stats.game_active = True
			self.sb.prep_score()
			self.sb.prep_lifes()

			# Put the player on a designated spot
			self.player.center_player()

			# Hide the mouse cursor
			pygame.mouse.set_visible(False)

		else:
			# If the player doesn't click the button the game won't start
			pygame.mouse.set_visible(True)

	def _check_continue_button(self, mouse_pos):
		"""Resume the game if clicked"""
		button_clicked = self.continue_button.rect.collidepoint(mouse_pos)

		if button_clicked:
			self.game_paused = False

	def _check_quit_button(self, mouse_pos):
		"""Exit the game if clicked."""
		button_clicked = self.quit_button.rect.collidepoint(mouse_pos)

		if button_clicked:
			sys.exit()

	def _check_restart_button(self, mouse_pos):
		"""Restart the game if clicked"""
		button_clicked = self.restart_button.rect.collidepoint(mouse_pos)

		if button_clicked:
			self.stats.game_active = False
			self.game_paused = False

	def _check_keydown_events(self, event):
		"""Listen for keypress inputs."""
		if event.key == pygame.K_RIGHT:
			self.player.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.player.moving_left = True
		elif event.key == pygame.K_UP:
			self.player.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.player.moving_down = True
		elif event.key == pygame.K_ESCAPE:
			self.pause_game()
				

	def _check_keyup_events(self, event):
		"""Listen for key releases."""
		if event.key == pygame.K_RIGHT:
			self.player.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.player.moving_left = False
		elif event.key == pygame.K_UP:
			self.player.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.player.moving_down = False

	def pause_game(self):
		"""Pause the game"""
		self.game_paused = True
		pygame.mouse.set_visible(True)
 

	def create_point(self):
		"""Create a point on a random spawn"""
		# No more than 1 point at any given time
		if len(self.point_list) == 0:
			# Get the spawn cordinates values from the dictionary and choose a random one
			spawn_point = list(point_spawn_dictionary.values())
			random_spawn = choice(spawn_point)
			# Create a point object and pass the random value
			point = Point(self, random_spawn)
			self.point_list.add(point)

	def _check_player_point_collision(self):
		"""Checks if the player collided with a point"""
		collision =  pygame.sprite.spritecollideany(self.player, self.point_list)
		if collision:
			# Increase score 
			self.stats.score += self.settings.point_value
			# Empty the score list
			self.point_list.empty()
			# Create a new one
			self.create_point()
			# Increase current score and check if its higher that high score
			self.sb.prep_score()
			self.sb.check_high_score()

	def _check_player_wall_collision(self):
		"""Respond appropriately if the player has hit an wall"""
		wall_collision = pygame.sprite.spritecollideany(self.player, self.walls_list)
		if wall_collision:
			self._player_hit()


	def _player_hit(self):
		"""Respond if the player hit a wall"""
		# If the player has lifes remaining
		if self.stats.lifes_left > 0:
			# Decrement life and reposition the player
			self.stats.lifes_left-= 1
			self.sb.prep_lifes()
			self.player.center_player()

		else:
			# Stop the game if lifes run out 
			self.stats.game_active = False

	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.blit(self.screen_image, (0, 0))
		for wall in self.walls_list:
			wall.draw()
		for spawn in self.spawn_list:
			spawn.draw()
		self.player.draw()
		for point in self.point_list.sprites():
			point.draw()

		# Draw the score information.
		self.sb.show_score()
		
		# Draw the play button if the game inactive.
		if not self.stats.game_active:
			self.play_button.draw_button()
		#Draw buttons when game is paused
		if self.game_paused == True:
			self.continue_button.draw_button()
			self.restart_button.draw_button()
			self.quit_button.draw_button()
 
		pygame.display.flip()


if __name__ == '__main__':
	# Make an instance and run the game
	game = Labyrinth()
	game.run_game()