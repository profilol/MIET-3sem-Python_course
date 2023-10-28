from model.article.joke_article import JokeArticle
from model.article.science_article import ScienceArticle
from model.article.article_enum import ArticleEnum
from model.commentary import Commentary
from model.author import Author
from file_operations import FileOperations
from user_exceptions import WrongDataInFileException, WrongFileFormat


if __name__ == '__main__':
    # author = Author.input_author()
    #
    # print(author)

    # Sanya
    # Voodosh
    # 38
    # Physics of HOMM3
    # JebusCross

    # joke_article = JokeArticle.input_article()
    # science_article = ScienceArticle.input_article()
    # joke_commentary = Commentary.input_commentary(ArticleEnum.JokeArticle)

    author = Author(name="Sanya", surname="Voodosh", age=38)
    science_article = ScienceArticle(title="ABC", author=author, description="HOMM3")

    article_list = [science_article]

    filename = "articles_file"

    FileOperations.save_all_articles(article_list, filename)

    load_list = FileOperations.load_all_articles(filename)

    FileOperations.add_article(science_article, "new_file")

    for i in load_list:
        print(i)

    try:
        FileOperations.load_all_articles("randomfile")
    except WrongFileFormat:
        print("Wrong binary file format")
    except WrongDataInFileException:
        print("Wrong data in file")

    # print(joke_commentary)
    # print(isinstance(science_article, ScienceArticle))


