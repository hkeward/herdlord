# IMPORTS

from herdlord import component


# CODE

class Map(component.Component):
	# size: map size (size*4 x size)
	def __init__(self, size=20):
		component.Component.__init__(self, [])
		self.x = size * 4
		self.y = size
		self.objects = []
		self.displayed = True
		self.grid = []
		self._generate_grid()

	def _generate_grid(self):
		line = [" "] * self.x
		lines = [list(line) for _ in range(self.y)]
		for obj in self.objects:
			lines[obj.y][obj.x] = obj.symbol
		self.grid = lines

	def add_object_to_grid(self, obj):
		self.objects.append(obj)
		self._generate_grid()

	def update_map(self):
		self._generate_grid()
