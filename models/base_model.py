#!/usr/bin/python3
"""defines a class base model with all common attributes
and methods for other classes """

from datetime import datetime
import uuid


class BaseModel:
	"""the base model class from which other classes inherit from"""
	def __init__(self, *args, **kwargs):
		"""initializes the base model"""
		time_format = '%Y-%m-%dT%H:%M:%S.%f'
		if kwargs:
			for key, value in kwargs.items():
				if key == "__class__":
					continue
				elif key in ('created_at', 'updated_at'):
					setattr(self, key, datetime.strptime(value, time_format))
				else:
					setattr(self, key, value)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()

	def __str__(self):
		"""returns string representation of the of the class"""
		return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

	def save(self):
		"""updates the updated_attribute with current time"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""returns a dictionary with its keys and values"""
		new_dict = self.__dict__.copy()
		new_dict['__class__'] = type (self).__name__
		new_dict['created_at'] = self.created_at.isoformat()
		new_dict['updated_at'] = self.updated_at.isoformat()
		return new_dict
