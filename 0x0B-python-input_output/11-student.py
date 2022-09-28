#!/usr/bin/python3
"""
Module 11-student
Defines a student by public instance attributes:
first_name, last_name and age
"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, args=None):
        """retrieves a dictionary representation of a Student instance"""
        data = self.__dict__
        if args is not None and type(args) is list:
            new = {}
            for i in args:
                if i in data:
                    val = data[i]
                    new[i] = val
            return new
        return data

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance:"""
        for key, value in json.items():
            if key in self.__dict__:
                self.__dict__[key] = value

