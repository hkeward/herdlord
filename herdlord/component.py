# IMPORTS

from herdlord import constants, util


# CODE

class Component:
	def __str__(self):
		rep = ""
		for line in self.grid:
			rep += "".join(line) + constants.newline
		return rep


class Header(Component):
	def __init__(self, grid=None):
		if grid is None:
			self.grid = [[]]
		else:
			self.grid = grid


class Map(Component):
	# map size = (size*4 x size)
	def __init__(self, size=20):
		self.x = size * 4
		self.y = size
		self.objects = []
		self.displayed = True

	@property
	def grid(self):
		line = [" "] * self.x
		lines = [list(line) for _ in range(self.y)]
		for obj in self.objects:
			lines[obj.y][obj.x] = obj.symbol
		return lines

	def add_object_to_grid(self, obj):
		self.objects.append(obj)


class Inventory(Component):
	x = 30
	count_width = 2

	def __init__(self, items):
		self.items = items
		self.y = 2 + len(items)
		self.displayed = True

	@property
	def grid(self):
		lines = list()
		lines.append(["INVENTORY"] + [" "] * (self.x - len("INVENTORY")))
		lines.append([constants.box_drawing["thick"]["top"]["middle"]] * self.x)
		for item, count in self.items.items():
			lines.append([item, "-" * (self.x - len(item) - self.count_width), str(f'{count:02}')])
		return lines

	def add_item(self, item):
		self.items[item] = self.items.get(item, 0) + 1

	def toggle(self):
		self.displayed = not self.displayed


# puts components side by side
class JoinedComponent(Component):
	def __init__(self, components):
		self.components = components

	@property
	def grid(self, borders=True):
		max_y = max(component.y for component in self.components) + (2 if borders else 0)
		joined_grid = []
		component_grids = []
		for component in [component for component in self.components if component.displayed]:
			if borders:
				component_grid = util.add_borders(component)
			else:
				component_grid = component.grid
			component_grid += [[]] * (max_y - component.y)
			component_grids.append(component_grid)
		for i in range(max_y):
			line = []
			for component_grid in component_grids:
				line += component_grid[i]
			joined_grid.append(line)
		return joined_grid


# stacks components vertically
# expects an array of grids (array of 2d arrays)
# generates a single 2d array made up of all components
class Screen(Component):
	def __init__(self, components):
		self.components = components

	@property
	def grid(self):
		lines = list()
		for component in self.components:
			for line in component.grid:
				lines.append(line)
		return lines


