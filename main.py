#!/usr/bin/env python3

# IMPORTS

from herdlord import character, screen, map, inventory, util
import readchar
import os


# CODE

def main():
	os.system("setterm -cursor off")

	char = character.Character(inventory.Inventory({"apple": 3, "toaster": 1}))

	map_display = map.Map()
	print(map_display.grid)
	map_display.add_object_to_grid(char)
	print(map_display.grid)

	map_screen = screen.Screen(content=[map_display, char.inventory])

	while True:
		util.clear()
		map_screen.print()

		inp = readchar.readchar()
		if inp == "]":
			break
		elif inp == "w":
			char.move("up")
		elif inp == "a":
			char.move("left")
		elif inp == "s":
			char.move("down")
		elif inp == "d":
			char.move("right")
		elif inp == "i":
			char.inventory.toggle()
		elif inp == "o":
			char.inventory.add_item("rock")

		map_display.update_map()


main()
