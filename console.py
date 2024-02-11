#!/usr/bin/python3
""" defines a command line interpreter"""

import cmd
import shlex
from models.base_model import BaseModel
import models


classes = {"BaseModel"}


class HBNBCommand(cmd.Cmd):
	""" cmd class"""
	prompt = "(hbnb) "

	def do_create(self, arg):
		"""create a new instance of the BaseModel"""
		args = args.split()
		if len(args) == 0:
			print(** class name missing **)
			return
		if args[0] not in classes:
			print("** class doesn't exist **")
			return
		else:
			base = args[0]
			new_instance = classes[base]()
			new_instance.save()
			print(new_instance.id)
			return

	def do_show(self, arg):
		"""prints the string representation of an instance"""
		args = shlex.split(arg)
		if len(args) == 0:
            print("** class name missing **")
            return
		if args[0] not in classes:
			print("** class doesn't exist **")
			return
		if len(args) == 1:
            print("** instance id missing **")
            return
		else:
			key = args[0] + "." + args[1]
			if key in models.storage.all():
				print(models.storage.all()[key])
			else:
				print(** no instance found **)

	def do_destroy(self, arg):
		"""deletes an instance"""
		args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
		if args[0] not in classes:
			print("** class doesn't exist **")
			return
		if len(args) == 1:
            print("** instance id missing **")
            return
		else:
			key = args[0] + "." + args[1]
			if key in models.storage.all():
				del models.storage.all()[key]
                models.storage.save()
            else:
				("** no instance found **")

	def do_all(self, arg):
		"""print all string rep of all instances"""
        args = shlex.split(arg)
        instances = []
        if len(args) == 0:
            objects = models.storage.all()
        elif args[0] in classes:
            objects = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in objects:
            instances.append(str(objects[key]))
        print("[", end="")
        print(", ".join(instances), end="")
        print("]")

	def do_quit(self, arg):
		""" program exited"""
		return True

	def do_EOF(self, arg):
		"""signal end of file or program"""
		print()
		return True

	def empty_line(self):
		"""do nothing when using ENTER"""
		return False

if __name__ == '__main__':
	HBNBCommand().cmdloop()
