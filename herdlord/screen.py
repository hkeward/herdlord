# IMPORTS

from herdlord import constants, util


# CODE

class Screen:
	def __init__(self, content, header=constants.header_line, footer=""):
		self.header = header
		self.content = content
		self.footer = footer

	def print(self):
		for component in ["\t".join(self.header),
						  util.join_components([component for component in self.content if component.displayed]),
						  self.footer]:
			print(component)

