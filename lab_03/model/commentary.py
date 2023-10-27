from model.author import Author
from model.article.article import Article


class Commentary:
    def __init__(self, author: Author, article: Article, description: str):
        if not isinstance(author, Author):
            raise Exception("Can't assign non-author object to commentary's author field")
        elif not isinstance(article, Article):
            raise Exception("Can't assign non-article object to commentary's article field")
        else:
            self.__author = author
            self.__article = article
            self.__description = description

    @property
    def author(self):
        return self.__author

    @property
    def article(self):
        return self.__article

    @property
    def description(self):
        return self.__description

    def __str__(self):
        result_string = f"{self.__author}, {self.__article}, {self.__description}"

        return result_string
