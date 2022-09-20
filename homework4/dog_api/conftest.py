import pytest
import random
import requests


@pytest.fixture
def base_url():
    return "https://dog.ceo/"


@pytest.fixture
def get_dog_breed(base_url):
    breeds = requests.get(base_url + "api/breeds/list/all")
    breed = random.choice(list(breeds.json()['message'].keys()))
    return breed
