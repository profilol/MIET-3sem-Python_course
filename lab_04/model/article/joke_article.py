from model.article.article import Article
from model.author import Author


class JokeArticle(Article):
    def __init__(self, title, author, description):
        super().__init__(title, author, description)

    def show_additional_info(self, author: Author = None):
        if author is not None and isinstance(author, Author):
            print(f"Here is another author of this article:{author}")
        else:
            super().show_additional_info()

