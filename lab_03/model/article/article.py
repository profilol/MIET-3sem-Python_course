from model.author import Author
from abc import ABCMeta, abstractmethod


class Article(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, title: str, author: Author, description: str):
        if not isinstance(author, Author):
            raise Exception("Can't assign non-author object to article's author field")
        else:
            self.__title = title
            self.__author = author
            self.__description = description

    @property
    def title(self) -> str:
        return self.__title

    @property
    def author(self) -> Author:
        return self.__author

    @property
    def description(self) -> str:
        return self.__description

    def __str__(self):
        result_string = f"[{self.__title}, {self.__author}, {self.__description}]"

        return result_string

    def __eq__(self, other):
        if self.author == other.author and self.title == other.title and self.description == other.description:
            return True
        else:
            return False

    def show_additional_info(self, author: Author = None):
        print("This is a parent method")
