import pytest

from django.urls import reverse
from bdd_helper import *


def test_index(client):
    Given("url")
    url = reverse('home.index')

    When("Get response")
    response = client.get(url)

    Then("it is ok")
    assert response.status_code == 200
    assert "Welcome to Movies Store" in str(response.content)

def test_about(client):
    Given("url")
    url = reverse('home.about')

    When("Get response")
    response = client.get(url)

    Then("it is ok")
    assert response.status_code == 200
    assert "we offer a vast digital library" in str(response.content)