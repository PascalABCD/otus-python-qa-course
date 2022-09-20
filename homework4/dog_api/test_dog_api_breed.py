import pytest
import requests


link = "https://images.dog.ceo/breeds/"


def test_api_get_breed_list_all(base_url):
    response = requests.get(base_url + "api/breeds/list/all")
    assert response.status_code == 200
    assert response.json()['status'] == "success"


def test_api_get_breed_image(base_url, get_dog_breed):
    response = requests.get(base_url + f"api/breed/{get_dog_breed}/images")
    assert response.status_code == 200
    assert response.json()['status'] == "success"


@pytest.mark.parametrize("breed", ['hound', 'terrier', 'sheepdog', 'retriever'])
def test_api_get_subbreed_image_check_link(base_url, breed):
    response = requests.get(base_url + f"api/breed/{breed}/images")
    assert link in response.json()['message'][0]


@pytest.mark.parametrize("limit", [1, 5, 49, 50])
def test_api_get_breed_images_limit(base_url, get_dog_breed, limit):
    response = requests.get(base_url + f"api/breed/{get_dog_breed}/images/random/{limit}")
    assert response.status_code == 200
    assert response.json()['status'] == "success"


@pytest.mark.xfail(reason="more than 50 images are returned")
def test_api_get_breed_images_exceed_limit(base_url, get_dog_breed):
    response = requests.get(base_url + f"api/breed/{get_dog_breed}/images/random/51")
    assert response.status_code == 400
    assert response.json()['status'] == "error"
