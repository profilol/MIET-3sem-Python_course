from model.author import Author
from model.article.article import Article


class Commentary:
    def __init__(self, author: Author, article: Article, description: str):
        if not isinstance(author, Author):
            raise Exception("Can't assign non-author object to commentary's author field")
        elif not isinstance(article, Article):
            raise Exception("Can't assign non-article object to commentary's article field")
        else:
            self.author = author
            self.article = article
            self.description = description

    def __str__(self):
        result_string = f"{self.author}, {self.article}, {self.description}"

        return result_string
