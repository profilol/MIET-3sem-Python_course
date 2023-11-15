from model.author import Author
from model.article.joke_article import JokeArticle
from model.article.science_article import ScienceArticle
from model.article.article import Article
from model.article.article_enum import ArticleEnum


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

    @classmethod
    def input_commentary(cls, article_type: ArticleEnum):
        try:
            print("Input commentary's author")
            author = Author.input_author()

            print("Input commentary's article")
            if article_type is ArticleEnum.JokeArticle:
                article = JokeArticle.input_article()
            elif article_type is ArticleEnum.ScienceArticle:
                article = ScienceArticle.input_article()

            description = input("Input commentary's description: ")
        except Exception as e:
            print("Wrong commentary's input")
        else:
            comment = cls(author=author, article=article, description=description)
            return comment
