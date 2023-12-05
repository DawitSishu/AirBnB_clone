#!/usr/bin/python3
"""
a base model for classes to inherit
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """
    the base model in which other classd can inherit from
    """
    def __init__(self, *args, **kwargs):
        """ initialises the calss model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key == "__class__":
                    setattr(self, key, type(self))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        prints the string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """
        save method that updats the updated at of the model
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns all the key value pairs of the main attributes of the class
        """
        new_dict = dict(self.__dict__)
        new_dict["__class__"] = type(self).__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        return new_dict
