#!/usr/bin/env python3

# IMPORTS

import os
from herdlord import constants
from herdlord import component as comp


# FUNCTIONS

def clear():
	os.system("clear")


# component should be an object that has the attributes grid (the thing to wrap in borders) and x (width of component)
def add_borders(component, box_type="thick"):
	bordered = list()
	bordered.append([constants.box_drawing[box_type]["top"]["left"],
					 constants.box_drawing[box_type]["top"]["middle"] * component.x,
					 constants.box_drawing[box_type]["top"]["right"]])
	for row in component.grid:
		bordered.append([constants.box_drawing[box_type]["vertical"]] +
						row + [constants.box_drawing[box_type]["vertical"]])
	bordered.append([constants.box_drawing[box_type]["bottom"]["left"],
					 constants.box_drawing[box_type]["bottom"]["middle"] * component.x,
					 constants.box_drawing[box_type]["bottom"]["right"]])
	return bordered


# joins components that should be side by side
def join_components(components, borders=True):
	max_y = max(component.y for component in components) + (2 if borders else 0)
	joined_grid = []
	component_grids = []
	for component in components:
		if borders:
			component_grid = add_borders(component)
		else:
			component_grid = component.grid
		component_grid += [[]] * (max_y - component.y)
		component_grids.append(component_grid)
	for i in range(max_y):
		line = []
		for component_grid in component_grids:
			line += component_grid[i]
		joined_grid.append(line)
	return comp.Component(joined_grid)
