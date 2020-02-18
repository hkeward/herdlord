class Character:
	def __init__(self, inventory):
		self.inventory = inventory
		self.x = 0
		self.y = 0
		self.symbol = "@"

	def move(self, direction):
		if direction == "up":
			self.y -= 1
		elif direction == "down":
			self.y += 1
		elif direction == "left":
			self.x -= 2
		elif direction == "right":
			self.x += 2
