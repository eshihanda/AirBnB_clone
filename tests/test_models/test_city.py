#!/usr/bin/python3
""" tests the city class"""

from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """tests for city class"""
    def setUp(self):
        self.city = City()

    def test_is_subclass(self):
        """test if city is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)

    def test_name_attr(self):
        """ test if the class has attribute name and that
        it is an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_id_attr(self):
        """ test if the class has attribute id and that
        it is an empty string"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_name_attr(self)
        """tests the attribute when set"""
        city = City(state_id='123', name='Michigan')
        self.assertEqual(city.state_id, '123')
        self.assertEqual(city.name, 'Michigan')
