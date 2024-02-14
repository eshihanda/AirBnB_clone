#!/usr/bin/python3
""" tests the Place class"""

from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlace(unittest.TestCase):
    """tests for place class"""
    def setUp(self):
        self.place = Place()

    def test_is_subclass(self):
        """test if place is a subclass of BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)

    def test_name_attr(self):
        """ test if the class has attribute name and that
        it is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(Place.name, "")

    def test_city_id_attr(self):
        """ test if the class has attribute id and that
        it is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")

    def test_user_id_attr(self):
        """ test if the class has attribute id and that
        it is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")

    def test_description_attr(self):
        """ test if the class has attribute description and that
        it is an empty string"""
        place = Place()
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")

    def test_number_of_rooms_attr(self):
        """ test if the class has attribute number of rooms and that
         it is an integer"""
        place = Place()
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)

    def test_bathrooms_attr(self):
        """tests if the class has attributes number of bathrooms"""
        place = Place()
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """tests if the class has attribute max guest"""
        place = Place()
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)

    def test_price_by_night_attr(self):
        """tests if the class has attributes price by night"""
        place = Place()
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)

    def test_latitude_attr(self):
        """tests if the class has attribute latitude"""
        place = Place()
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)

    def test_longitude_attr(self):
        """tests if the class has attribute longitude"""
        place = Place()
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
