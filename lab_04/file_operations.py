import os
from abc import ABCMeta
from model.article.article import Article
import shelve

from user_exceptions import WrongDataInFileException, WrongFileFormat


class FileOperations(ABCMeta):

    BINARY_DIRECTORY = "./binary_files/"

    @staticmethod
    def add_article(article: Article, filename: str):
        try:
            with shelve.open(filename, 'a') as file:
                index = len(file)
                file[str(index)] = article
        except Exception as e:
            print("File doesn't exist")
            with shelve.open(filename, 'n') as file:
                index = 0
                file[str(index)] = article




    @staticmethod
    def save_all_articles(article_list: list[Article], filename: str):
        with shelve.open(filename, 'n') as file:
            for i in range(len(article_list)):
                file[str(i)] = article_list[i]

    @staticmethod
    def load_all_articles(filename: str):
        loaded_articles = []
        try:
            with shelve.open(filename, "r") as file:
                for i in file:
                    if not isinstance(file[i], Article):
                        raise WrongDataInFileException
                    loaded_articles.append(file[i])
                    return loaded_articles
        except WrongDataInFileException:
            raise WrongDataInFileException
        except Exception:
            raise WrongFileFormat


    # @staticmethod
    # def create_bin_directory():
    #     if not os.path.isdir(FileOperations.BINARY_DIRECTORY):
    #         os.mkdir(FileOperations.BINARY_DIRECTORY)
