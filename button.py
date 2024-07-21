import pygame.font

class PlayButton:

	def __init__(self, game, text):
		"""Initialize button attributes."""
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = (255, 0, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# The button text needs to be prepped only once
		self._prep_text(text)

	def _prep_text(self, text):
		"""Turn text into a rendered image and center text on the button."""
		self.text_image = self.font.render(text, True, self.text_color,
			self.button_color)
		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.center = self.rect.center

	def draw_button(self):
		"""Draw blank button and then draw message."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.text_image, self.text_image_rect)


class ContinueButton:

	def __init__(self, game, text):
		"""Initialize button attributes."""
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = (255, 0, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# The button text needs to be prepped only once
		self._prep_text(text)

	def _prep_text(self, text):
		"""Turn text into a rendered image and center text on the button."""
		self.text_image = self.font.render(text, True, self.text_color,
			self.button_color)
		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.center = self.rect.center

	def draw_button(self):
		"""Draw blank button and then draw message."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.text_image, self.text_image_rect)


class RestartButton:

	def __init__(self, game, text):
		"""Initialize button attributes."""
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = (255, 0, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		# Increase value so the button is bellow the others
		self.rect.y += 70

		# The button text needs to be prepped only once
		self._prep_text(text)

	def _prep_text(self, text):
		"""Turn text into a rendered image and center text on the button."""
		self.text_image = self.font.render(text, True, self.text_color,
			self.button_color)
		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.center = self.rect.center

	def draw_button(self):
		"""Draw blank button and then draw message."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.text_image, self.text_image_rect)

class QuitButton:

	def __init__(self, game, text):
		"""Initialize button attributes."""
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()

		# Set the dimensions and properties of the button.
		self.width, self.height = 200, 50
		self.button_color = (255, 0, 0)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		# Build the button's rect object and center it.
		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = self.screen_rect.center
		# Increase value so the button is bellow the others
		self.rect.centery += 140

		# The button text needs to be prepped only once
		self._prep_text(text)

	def _prep_text(self, text):
		"""Turn text into a rendered image and center text on the button."""
		self.text_image = self.font.render(text, True, self.text_color,
			self.button_color)
		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.center = self.rect.center

	def draw_button(self):
		"""Draw blank button and then draw message."""
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.text_image, self.text_image_rect)
