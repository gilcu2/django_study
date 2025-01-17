import pytest

from django.urls import reverse
from bdd_helper import *


def test_index(client):
    Given("url")
    url = reverse('movies.index')

    When("Get response")
    response = client.get(url)

    Then("it is ok")
    assert response.status_code == 200
    assert "Inception" in str(response.content)

def test_show(client):
    Given("url")
    url = reverse('movies.show',args=[2])

    When("Get response")
    response = client.get(url)

    Then("it is ok")
    assert response.status_code == 200
    assert "A journey to a distant world" in str(response.content)