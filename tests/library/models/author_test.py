from datetime import datetime

import pytest

from bdd_helper import *
from library.models import Author


@pytest.mark.django_db
def test_author_db():
    Given("author in db")
    date_str="2012-12-25"
    date_value=datetime.strptime(date_str, "%Y-%m-%d").date()
    author = Author(first_name="John",last_name="Doe",birth_date =date_value)
    author.save()


    When("find")
    authors=Author.objects.all()
    result=authors.filter(first_name="John").first()

    Then("it is the expected")
    assert result == author