from library.models import Book,Author, Publisher
from bdd_helper import *
from datetime import date,datetime
import pytest

# @pytest.mark.django_db
def test_get_book_age():
    Given("book with date")
    date_str="2012-12-25"
    date_value=datetime.strptime(date_str, "%Y-%m-%d").date()
    author = Author(first_name="John",last_name="Doe",birth_date =date_value)
    book = Book(title="Django Unchained", author=author, publication_date=date_value,
                isbn="9781234567897")

    When("get age")
    age=book.get_age()

    Then("it is the expected")
    assert age==date.today().year-date_value.year

@pytest.mark.django_db
def test_save_book():
    Given("book with date")
    date_str="2012-12-25"
    date_value=datetime.strptime(date_str, "%Y-%m-%d").date()
    author = Author(first_name="John",last_name="Doe",birth_date =date_value)
    book = Book(title="Django Unchained", author=author, publication_date=date_value,
                isbn="9781234567897")

    When("save")
    author.save()
    book.save()

    And("load")
    books = Book.objects.filter(author=author)

    Then("it is the expected")
    assert len(books) > 0

@pytest.mark.django_db
def test_book_with_publisher():
    Given("book and publisher")
    date_str="2012-12-25"
    date_value=datetime.strptime(date_str, "%Y-%m-%d").date()

    author = Author(first_name="John",last_name="Doe",birth_date =date_value)
    book = Book(title="Django Unchained", author=author, publication_date=date_value,
                isbn="9781234567897")
    author.save()
    book.save()

    publisher = Publisher(name="Knowledge Hub Publishing",
                           address="456 Elm St", city="San Francisco", state_province="CA",
                           country="USA", website="http://knowledgehub.com")
    publisher.save()
    book.publishers.add(publisher)

    When("get")
    book_get = Book.objects.get(id=1)

    Then("it is the expected")
    assert book_get.title == "Django Unchained"