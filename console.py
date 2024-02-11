#!/usr/bin/python3
""" defines a command line interpreter"""

import cmd
from models.base_model import BaseModel
import shlex
from models import storage

class HBNBCommand(cmd.Cmd):
	""" cmd class"""
	prompt = "(hbnb) "
	classes = ("BaseModel")

	def do_quit(self, arg):
		""" program exited"""
		return True
	
	def help_quit(self):
		"""Display help information about the quit command."""
		print("Quit command to exit the program")
	
	def do_EOF(self):
		"""signal end of file or program"""
		print()
		return True

	def emptyline(self):
		"""Do nothing when an empty line is entered."""
		pass

	def do_create(self, arg):
		"""Creates a new instance of BaseModel,
		saves it (to the JSON file) and prints the id"""

		args = shlex.split(arg)

		if not len(args):
			print("** class name missing **")

		elif args[0] not in HBNBCommand.classes:
			print("** class doesn't exist **")
			
		else:
			instance = BaseModel()
			instance.save()
			print(instance.id)

	def do_show(self,arg):
		""" Prints the string representation of an instance based on the class
		name and id. Ex: $ show BaseModel 1234-1234-1234."""

		args = shlex.split(arg)
		if not len(args):
			print("** class name missing **")
		elif args[0] not in HBNBCommand.classes:
			print("** class doesn't exist **")
		elif len(args) < 2:
			print("** instance id missing **")
		else:
			obj = storage.all()
			key = f"{args[0]}.{args[1]}"
			if key in obj:
				print(obj[key])
			else:
				print("** no instance found **")
		
	def do_destroy(self, arg):
		"""
		Deletes an instance based on the class name and id (save the 
		change into	the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
		"""
		args = shlex.split(arg)
		if not len(args):
			print("** class name missing **")
		elif args[0] not in HBNBCommand.classes:
			print("** class doesn't exist **")
		elif len(args) < 2:
			print("** instance id missing **")
		else:
			obj = storage.all()
			key = f"{args[0]}.{args[1]}"
			if key not in obj:
				print("** no instance found **")
			else:
				del obj[key]
				storage.save()

	def do_all(self, arg):
		"""
		Prints all string representation of
		all instances based or not on the class name
		"""
		obj = storage.all()

		args = shlex.split(arg)

		if len(args) == 0:
			for key, value in obj.items():
				print(str(value))
		elif args[0] not in HBNBCommand.classes:
			print("** class doesn't exist **")
		else:
			for key, value in obj.items():
				clas, ids = key.split('.')
				if clas == args[0]:
					print(str(value))

	def do_update(self, arg):
		"""
		Updates an instance based on the class name and id by
		adding or updating attribute (save the change into the JSON file).
		Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
		"""
		args = shlex.split(arg)

		if len(args) == 0:
			print("** class name missing **")
		elif args[0] not in HBNBCommand.classes:
			print("** class doesn't exist **")
		elif len(args) < 2:
			print("** instance id missing ** ")

		else:
			objs = storage.all()
			key = f"{args[0]}.{args[1]}"
			if key not in objs:
				print("** no instance found **")
			elif len(args) < 3:
				print("** attribute name missing **")
			elif len(args) < 4:
				print("** value missing **")
			else:
				obj = objs[key]
				a_name = args[2]
				a_value = args[3]
				try:
					a_value = eval(a_value)
				except Exception:
					pass
				setattr(obj, a_name, a_value)
				obj.save()



if __name__ == '__main__':
	HBNBCommand().cmdloop()
