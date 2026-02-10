class Student:
    """Represent a student with basic identifying information."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the student."""
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            result = {}
            for a in attrs:
                if a in self.__dict__:
                    result[a] = self.__dict__[a]
            return result
        return self.__dict__
