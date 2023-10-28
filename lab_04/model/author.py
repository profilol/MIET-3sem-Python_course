class Author:
    def __init__(self, name: str, surname: str, age: int):
        if not type(age) is int:
            raise Exception("Can't assign non-integer value to author's age field")
        elif age < 0:
            raise Exception("Age can't be less than 0")
        else:
            self.__name = name
            self.__surname = surname
            self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @property
    def surname(self) -> str:
        return self.__surname

    @property
    def age(self) -> int:
        return self.__age

    def __str__(self):
        result_string = f"[{self.__name}, {self.__surname}, {self.__age}]"

        return result_string

    def __eq__(self, other):
        if self.name == other.name and self.surname == other.surname and self.age == other.age:
            return True
        else:
            return False

    @classmethod
    def input_author(cls):
        try:
            name = input("Input author's name: ")
            surname = input("Input author's surname: ")
            age = int(input("Input author's age: "))
        except Exception as e:
            print("Wrong author's input")
        else:
            author = cls(name, surname, age)
            return author
