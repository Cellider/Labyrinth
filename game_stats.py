class GameStats():
	"""Track statistics for Labyrinth."""

	def __init__(self, game):
		"""Initialize statistics."""
		self.settings = game.settings
		self.reset_stats()

		# Start the game on a inactive flag, so the game doesn't imediately begin 
		self.game_active = False

		self.score = 0

		# High score should never be reset, only increased
		with open('high_score.txt') as points:
			saved_high_score = points.read()
		self.high_score = int(saved_high_score)

	def reset_stats(self):
		"""Reset statistics that can change during the game."""
		self.lifes_left = self.settings.player_lifes
		self.score = 0