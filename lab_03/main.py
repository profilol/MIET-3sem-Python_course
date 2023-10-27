from model.author import Author
from model.commentary import Commentary
from model.article.joke_article import JokeArticle
from model.article.science_article import ScienceArticle
from model.journal import Journal

if __name__ == "__main__":
    article_lst = []
    author = Author(name="ABC", surname="DEF", age=42)  # create random author

    joke_article = JokeArticle("Joke1", author, "Guide for wyvern")  # create first joke article
    joke_article2 = JokeArticle("Joke1", author, "Guide for brewmaster")  # create second joke article

    science_article = ScienceArticle("GAN", author, "GAN research")  # create first science article

    # Trying polymorphism:

    article_lst.append(joke_article)
    article_lst.append(science_article)

    for i in article_lst:
        i.show_additional_info(author)

    for i in article_lst:
        i.show_additional_info()

    journal = Journal("All things", [], [])  # Create object for aggregation

    journal.add_article(joke_article2)
    journal.add_article(science_article)

    commentary = Commentary(author, joke_article2, "Cool")

    journal.add_commentary(commentary)
    journal.add_commentary(commentary)

    print(journal)

    gen = journal.create_commentary_generator()  # Create commentary generator

    for i in gen:  # Launch generator
        print(i)

    for i in journal.generated_commentaries:  # Show generated with generator comments
        print(i)
