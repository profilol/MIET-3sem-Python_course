class Author:
    def __init__(self, name, surname, age):
        if not type(age) is int:
            raise Exception("Can't assign non-integer value to author's age field")
        elif age < 0:
            raise Exception("Age can't be less than 0")
        else:
            self.name = name
            self.surname = surname
            self.age = age

    def __str__(self):
        result_string = f"[{self.name}, {self.surname}, {self.age}]"

        return result_string

    def __eq__(self, other):
        if self.name == other.name and self.surname == other.surname and self.age == other.age:
            return True
        else:
            return False
