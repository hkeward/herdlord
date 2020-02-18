# IMPORTS

from herdlord import constants, component


# CODE

class Inventory(component.Component):
	x = 30
	count_width = 2

	def __init__(self, items):
		component.Component.__init__(self, [])
		self.items = items
		self.grid = []
		self._generate_grid()
		self.y = 2 + len(items)
		self.displayed = True

	def _generate_grid(self):
		lines = list()
		lines.append(["INVENTORY"] + [" "] * (self.x - len("INVENTORY")))
		lines.append([constants.box_drawing["thick"]["top"]["middle"]] * self.x)
		for item, count in self.items.items():
			lines.append([item, "-" * (self.x - len(item) - self.count_width), str(f'{count:02}')])
		self.grid = lines

	def add_item(self, item):
		self.items[item] = self.items.get(item, 0) + 1
		self._generate_grid()

	def toggle(self):
		self.displayed = not self.displayed
