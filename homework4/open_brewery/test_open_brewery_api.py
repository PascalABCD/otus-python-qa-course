import pytest
import requests
import schemas

from jsonschema import validate


brewery_types = ["micro", "nano", "regional", "brewpub", "large",
                 "planning", "bar", "contract", "proprietor", "closed"]


@pytest.mark.parametrize("query, page_size", [("dog", 3), ("cat", 5)])
def test_check_search_query_in_name(base_url, query, page_size):
    response = requests.get(base_url + f"/search?query={query}&per_page={page_size}")
    name = query.capitalize()
    for brewery in response.json():
        assert name in brewery['name']


@pytest.mark.xfail(reason="more than 15 breweries returned")
@pytest.mark.parametrize("query", ["dog", "brewery"])
def test_maximum_number_of_breweries(base_url, query):
    response = requests.get(base_url + f"/autocomplete?query={query}")
    assert len(response.json()) <= 15


@pytest.mark.parametrize("name", ["sleepy-dog-brewing-co-tempe", "playground-brewery-goyang-si"])
def test_response_schema_single_brewery(base_url, name):
    response = requests.get(base_url + f"/{name}")
    validate(response.json(), schemas.single_brewery_schema)


@pytest.mark.xfail(reason="brewery type taproom is not in the documentation")
@pytest.mark.parametrize("page", range(1, 101))
def test_check_brewery_type(base_url, page):
    index = 50
    response = requests.get(base_url + f"?page={page}&per_page={index}")
    for i in range(index):
        assert response.json()[i]['brewery_type'] in brewery_types


@pytest.mark.parametrize("page", range(1, 50))
def test_postal_code_format(base_url, page):
    index = 25
    response = requests.get(base_url + f"?page={page}&per_page={index}")
    for i in range(index):
        if len(response.json()[i]['postal_code']) == 5:
            assert response.json()[i]['postal_code'].isdigit()
        elif len(response.json()[i]['postal_code']) == 10:
            assert response.json()[i]['postal_code'][5] == "-"
