#!/usr/bin/python3
""" defines a command line interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
	""" cmd class"""
	prompt = "(hbnb) "

	def do_quit(self, arg):
		""" program exited"""
		return True

	def do_EOF(self, arg):
		"""signal end of file or program"""
		print()
		return True

	def empty_line(self):
		"""do nothing when using ENTER"""
		pass

if __name__ == '__main__':
	HBNBCommand().cmdloop()
