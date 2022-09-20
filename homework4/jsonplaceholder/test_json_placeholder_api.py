import pytest
import requests
import random

from jsonschema import validate
from schemas import post_schema


@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_post_schema(base_url, post_id):
    response = requests.get(base_url + f"posts/{post_id}")
    validate(instance=response.json(), schema=post_schema)


def test_create_post(base_url):
    data = {
        "title": "Test title",
        "body": "Test body",
        "userId": "56"
    }
    response = requests.post(base_url + "posts", data=data)
    assert response.status_code == 201
    for i in data.keys():
        assert data[i] == response.json()[i]


def test_delete_post(base_url):
    post_id = random.randint(1, 100)
    response = requests.delete(base_url + f"posts/{post_id}")
    assert response.status_code == 200
    assert response.json() == {}


@pytest.mark.parametrize("user_id", [1, 4, 7, 10])
def test_filter_by_user_id(base_url, user_id):
    response = requests.get(base_url + f"posts?userId={user_id}")
    for i in response.json():
        assert i["userId"] == user_id


@pytest.mark.parametrize("user_id", [1, 4, 7, 10])
def test_album_url(base_url, user_id):
    response = requests.get(base_url + f"albums/{user_id}/photos")
    url = "https://via.placeholder.com"
    for i in response.json():
        assert url in i["url"]
