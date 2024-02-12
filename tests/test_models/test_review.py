#!/usr/bin/python3
""" tests the review class"""

from models.review import Review
from models.base_model import BaseModel
import unittest


class TestReview(unittest.TestCase):
    """tests for review class"""
    def setUp(self):
        self.review = Review()

    def test_is_subclass(self):
        """test if review is a subclass of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)

    def test_place_attr(self):
        """ test if the class has attribute place id and that
        it is an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")

    def test_user_attr(self):
        """ test if the class has attribute user id and that
        it is an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")

    def test_text_attr(self):
        """ test if the class has attribute place text and that
        it is an empty string"""
        review = Review()
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")
