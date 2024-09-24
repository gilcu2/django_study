from library.models import Book,Author
from bdd_helper import *
from datetime import date,datetime
import pytest

# @pytest.mark.django_db
def test_get_age():
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
