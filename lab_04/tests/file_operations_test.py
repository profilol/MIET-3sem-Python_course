import os

import pytest
import shelve
from file_operations import FileOperations
from user_exceptions import WrongDataInFileException, WrongFileFormat
from model.article.joke_article import JokeArticle
from model.article.science_article import ScienceArticle
from model.author import Author
from model.article.article import Article


cog_dir = "./cog_files"

@pytest.fixture(scope="module")
def create_empty_file():
    os.mkdir(cog_dir)
    empty_file_name = cog_dir + "/empty_file"
    empty_file = shelve.open(empty_file_name, "n")
    empty_file.close()
    yield empty_file_name

    for root, dirs, files in os.walk(cog_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(cog_dir)


@pytest.fixture(scope="module")
def create_wrong_data_file():
    os.mkdir(cog_dir)
    wrong_data_file_name = cog_dir + "/wrong_data_file"
    wrong_data_file = shelve.open(wrong_data_file_name, "n")
    wrong_data_file["0"] = "abc"
    wrong_data_file.close()
    yield wrong_data_file_name

    for root, dirs, files in os.walk(cog_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(cog_dir)


@pytest.fixture(scope="module")
def create_file_for_saving():
    os.mkdir(cog_dir)
    data_file_name = cog_dir + "/data_file"
    data_file = shelve.open(data_file_name, "n")
    data_file.close()

    yield data_file_name

    for root, dirs, files in os.walk(cog_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(cog_dir)

def test_empty_article_file(create_empty_file):
    with pytest.raises(WrongFileFormat):
        FileOperations.load_all_articles(create_empty_file)


def test_wrong_article_data(create_wrong_data_file):
    with pytest.raises(WrongDataInFileException):
        FileOperations.load_all_articles(create_wrong_data_file)


def test_save_article_data(create_file_for_saving):
    author = Author(name="Sanya", surname="Voodosh", age=38)
    science_article = ScienceArticle(title="ABC", author=author, description="HOMM3")
    joke_article = JokeArticle(title="ABC", author=author, description="HOMM3")

    article_list = [science_article, joke_article]

    file_saving = create_file_for_saving

    FileOperations.save_all_articles(article_list, file_saving)

    loaded_articles = FileOperations.load_all_articles(file_saving)

    for i in loaded_articles:
        assert (isinstance(i, Article))

