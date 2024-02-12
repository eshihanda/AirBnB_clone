#!/usr/bin/python3
""" tests the state class"""

from models.state import State
from models.base_model import BaseModel
import unittest


class TestState(unittest.TestCase):
	"""tests for state class"""
	def setUp(self):
		self.state = State()

	def test_is_subclass(self):
		"""test if state is a subclass of BaseModel"""
		state = State()
		self.assertIsInstance(state, BaseModel)

	def test_state_attr(self):
		""" test of the class has attribute name and that
		it is an empty string"""
		state = State()
		self.assertTrue(hasattr(state, "name"))
		self.assertEqual(state.name, "")

	def test_name_attr(self):
		"""tests the attribute when set"""
		state = State(name='Michigan')
		self.assertEqual(state.name, 'Michigan')

