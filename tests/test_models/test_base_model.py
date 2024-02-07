#!/usr/bin/python3
""" tests the base model"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.Testcase):
	"""tests the base model class"""
	def setUp(self):
		self.base_model = BaseModel()

	def test_init_method(self):
		my_model = BaseModel()

		self.assertIsNotNone(my_model.id)
		self.assertIsNotNone(my_model.created_at)
		self.assertIsNotNone(my_model.updated_at)

	def test_save_method(self):
		"""tests the save method"""
		my_model = BaseModel()

		old_updated_at = my_model.updated_at
		my_model.save()
		new_updated_at = my_model.updated_at
		self.assertNotEqual(old_updated_at, new_updated_at)

	def test_to_dict(self):
		""" tests to_dict method"""
		my_model = BaseModel()

		new_dict = my_model.to_dict()
		self.assertIsInstance(new_dict, dict)
		self.assertEqual(new_dict["__class__"], "BaseModel")
		self.assertEqual(type(new_dict["created_at"]), str)
		self.assertEqual(type(new_dict["updated_at"]), str)
		self.assertEqual(new_dict["created_at"], my_model.created_at.isoformat())
		self.assertEqual(new_dict["updated_at"], my_model.updated_at.isoformat())

	def test_str_method(self):
		"""test the string method"""
		my_model = BaseModel()

		string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
		self.assertEqual(string, str(my_model))
