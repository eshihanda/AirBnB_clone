#!/usr/bin/python3
""" tests the user class"""

from models.user import User
from models.base_model import BaseModel
import unittest


class TestUser(unittest.TestCase):
    """tests for User class"""
    def setUp(self):
        self.user = User()

    def test_user(self):
        """test if it is a subclass of the base model"""
        user = User()
        self.assertIsInstance(user, BaseModel)

    def test_email(self):
        """tests that user has email"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password(self):
        """test that user has password"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name_default(self):
        """test that user has first name"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name_default(self):
        """test that user has first name"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_user_attributes(self):
        user = User(email='monneshihanda@gmail.com', password='monn123',
                    first_name='monn', last_name='eshihanda')
        self.assertEqual(user.email, 'monneshihanda@gmail.com')
        self.assertEqual(user.password, 'monn123')
        self.assertEqual(user.first_name, 'monn')
        self.assertEqual(user.last_name, 'eshihanda')
