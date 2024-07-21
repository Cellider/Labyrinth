import pygame.font
from pygame.sprite import Group

from lifes import Lifes

class Scoreboard:
	"""Class to manage reporting score information"""

	def __init__(self, game):
		"""Initialize scorekeeping attributes."""
		self.game = game 
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()
		self.settings = game.settings
		self.stats = game.stats

		# Font settings for score information.
		self.text_color = (0, 0, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Prepare the initial score images.
		self.prep_score()
		self.prep_high_score()
		self.prep_lifes()

	def prep_score(self):
		"""Turn the score text into a rendered image."""
		score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True,
				self.text_color, None) 

		# Display the score at the top right of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = 1280
		self.score_rect.top = 20

	def show_score(self):
		"""Draw scores, lifes into the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.lifes.draw(self.screen)

	def prep_high_score(self):
		"""Turn the high score into a rendered image."""
		high_score_str = str(self.stats.high_score)
		self.high_score_image = self.font.render(high_score_str, True,
				self.text_color, None)

		# Center the high score at the top of the screen.
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def check_high_score(self):
		"""Check to see it there's a new high score."""
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			with open('high_score.txt', 'w') as points:
				points.write(str(self.stats.score))
			self.prep_high_score()

	def prep_lifes(self):
		"""Show how many lifes are left."""
		self.lifes = pygame.sprite.Group()
		for life_number in range(self.stats.lifes_left):
			life = Lifes(self.game)
			life.rect.x = 20 + life_number * life.rect.width
			life.rect.y = 20
			self.lifes.add(life)