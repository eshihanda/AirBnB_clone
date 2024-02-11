#!/usr/bin/python3
"""defines a city class that inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """city class"""
    state_id = ""
    name = ""
