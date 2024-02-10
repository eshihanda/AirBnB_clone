#!/usr/bin/python3
"""defines a class User that inherists from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
	"""class that inherits from base model"""
	email = ""
	password = ""
    first_name = ""
    last_name = ""
	