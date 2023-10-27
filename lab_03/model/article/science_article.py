from model.article.article import Article
from model.author import Author


class ScienceArticle(Article):
    def __init__(self, title: str, author: Author, description: str):
        super().__init__(title, author, description)

    def base_method(self, author: Author = None):
        print("This is a child method")
