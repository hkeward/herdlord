# IMPORTS

from herdlord import constants


# CODE

class Component:
	def __init__(self, grid):
		self.grid = grid

	def __str__(self):
		rep = ""
		for line in self.grid:
			rep += "".join(line) + constants.newline
		return rep
