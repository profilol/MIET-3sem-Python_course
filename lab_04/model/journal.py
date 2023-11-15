from model.commentary import Commentary
from model.article.article import Article
from model.author import Author
from typing import Generator


class Journal:
    def __init__(self, title: str, article_list: list[Article], commentary_list: list[Commentary]):
        if not all(isinstance(element, Article) for element in article_list):
            raise Exception("Can't assign non-article list to journal's article list field")
        elif not all(isinstance(element, Commentary) for element in commentary_list):
            raise Exception("Can't assign non-commentary list to journal's commentary list field")
        else:
            self.__title = title
            self.__article_list = article_list
            self.__commentary_list = commentary_list
            self.__generated_commentaries = []

    @property
    def title(self) -> str:
        return self.__title

    @property
    def article_list(self) -> list[Article]:
        return self.__article_list

    @property
    def commentary_list(self) -> list[Commentary]:
        return self.__commentary_list

    @property
    def generated_commentaries(self) -> list[Commentary]:
        return self.__generated_commentaries

    def add_article(self, article: Article):
        if not isinstance(article, Article):
            print("Can't append non-article object into article list")
        else:
            self.__article_list.append(article)

    def add_commentary(self, commentary: Commentary):
        if not isinstance(commentary, Commentary):
            print("Can't append non-commentary object into commentary list")
        else:
            for i in self.__article_list:
                if i == commentary.article:
                    self.__commentary_list.append(commentary)

    def __str__(self):
        result_string = (f"[Journal title: {self.__title}\n"
                         f"Articles: {[str(i) for i in self.__article_list]}\n"
                         f"Commentaries: {[str(i) for i in self.__commentary_list]}]")

        return result_string

    def __my_gen(self):
        default_author = Author("Sanya", "Voodosh", 38)
        for i in self.article_list:
            cur_commentary = Commentary(default_author, i, f"DEF")
            self.__generated_commentaries.append(cur_commentary)
            yield cur_commentary

    def create_commentary_generator(self) -> Generator:
        commentary_generator = self.__my_gen()
        return commentary_generator
