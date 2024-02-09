#!/usr/bin/python3
"""defines a class base model with all common attributes
and methods for other classes """

from datetime import datetime
import uuid
import models


class BaseModel:

    """Base model class from which other classes inherit.

    Attributes:
        id (str): The unique identifier of the model instance.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """Initializes the base model.

        Args:
            *args: Variable positional arguments (Not used).
            **kwargs: Variable keyword arguments.
        """
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
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)


    def __str__(self):
        """Returns string representation of the class instance."""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the class instance."""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
