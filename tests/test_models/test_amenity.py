#!/usr/bin/python3
""" tests the amenity class"""

from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """tests for amenity class"""
    def setUp(self):
        self.amenity = Amenity()

    def test_is_subclass(self):
        """test if amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_name_attr(self):
        """ test if the class has attribute name and that
        it is an empty string"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def amenity_name_set(self):
        """test name set"""
        amenity = Amenity(name='Wi-Fi')
        self.assertEqual(amenity.name, 'Wi-Fi')
