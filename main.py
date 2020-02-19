#!/usr/bin/env python3

# IMPORTS

from herdlord import character, util
from herdlord import component as comp
import readchar
import os


# CODE

def main():
	os.system("setterm -cursor off")

	char = character.Character(comp.Inventory({"apple": 3, "toaster": 1}))

	map_display = comp.Map()
	map_display.add_object_to_grid(char)

	map_screen = comp.Screen([comp.Header([["Scholar Heather"]]), comp.JoinedComponent(
		[map_display, char.inventory])])

	while True:
		util.clear()
		print(map_screen)

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


main()
