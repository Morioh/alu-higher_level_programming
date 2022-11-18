#!/usr/bin/python3
# class Student that defines a student by: (based on 10-student.py)
#   - Public instance attributes:
#       - first_name
#       - last_name
#       - age
#   - Instantiation with first_name, last_name and age:
#       def __init__(self, first_name, last_name, age)
#   - Public method def to_json(self):
#       that retrieves a dictionary representation,
#       of a Student instance (same as 8-class_to_json.py):
#           - If attrs is a list of strings, only attribute names,
#               contained in this list must be retrieved
#           - Otherwise, all attributes must be retrieved
#   - Public method def reload_from_json(self, json):
#       that replaces all attributes of the Student instance:
#           - You can assume json will always be a dictionary
#           - A dictionary key will be the public attribute name
#           - A dictionary value will be the value of the public attribute
"""
    class 'Student'
"""


class Student:
    """
        define class 'Student'
    """

    def __init__(self, first_name, last_name, age):
        """
            init a new Student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieve dictionary representation of a Student instance
        """

        if attrs is None or type(attrs) is not list:
            return self.__dict__
        for att in attrs:
            if type(att) is not str:
                return self.__dict__
        return {x: self.__dict__[x] for x in self.__dict__ if x in attrs}

    def reload_from_json(self, json):
        """
            replace all attributes of Student instance
        """

        for key, value in json.items():
            self.__dict__[key] = value
