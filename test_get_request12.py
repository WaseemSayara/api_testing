import pytest
import requests


@pytest.fixture
def url():
    return 'https://reqres.in/api'


def make_resource_json(values):
    user_json = {'id': values[0], 'name': values[1], 'year': values[2], 'color': values[3],
                 'pantone_value': values[4]}
    return user_json


def make_user_json(values):
    user_json = {'id': values[0], 'email': values[1], 'first_name': values[2], 'last_name': values[3],
                 'avatar': values[4]}
    return user_json


@pytest.mark.users
def test_get_list_users(url):
    response = requests.get(url+'/users?page=2')
    assert response.status_code == 200
    assert response.content is not None
    assert response.json()["page"] == 2
    response_data = response.json()['data'][0]
    values = [7, 'michael.lawson@reqres.in', 'Michael', 'Lawson', 'https://reqres.in/img/faces/7-image.jpg']
    test_values = make_user_json(values)
    keys = list(test_values.keys())
    for key in keys:
        assert response_data[key] == test_values[key]

    print("get response status : ", response.status_code)


@pytest.mark.users
def test_get_single_user(url):
    response = requests.get(url+'/users/2')
    assert response.status_code == 200
    assert response.content is not None
    response_data = response.json()['data']
    values = [2, 'janet.weaver@reqres.in', 'Janet', 'Weaver', 'https://reqres.in/img/faces/2-image.jpg']
    test_values = make_user_json(values)
    keys = list(test_values.keys())
    for key in keys:
        assert response_data[key] == test_values[key]
    print("get single user : ", response.status_code)


@pytest.mark.users
def test_get_not_existing_user(url):
    response = requests.get(url+'/users/23')
    assert response.status_code == 404
    print("get not existing user : ", response.status_code)


@pytest.mark.resource
def test_get_list_resource(url):
    response = requests.get(url+'/unknown')
    assert response.status_code == 200
    assert response.content is not None
    assert response.json()["page"] == 1
    response_data = response.json()['data'][0]
    values = [1, 'cerulean', 2000, '#98B2D1', '15-4020']
    test_values = make_resource_json(values)
    keys = list(test_values.keys())
    for key in keys:
        assert response_data[key] == test_values[key]
    print("get list resource : ", response.status_code)


@pytest.mark.resource
def test_get_single_resource(url):
    response = requests.get(url+'/unknown/2')
    assert response.status_code == 200
    assert response.content is not None
    response_data = response.json()['data']
    values = [2, 'fuchsia rose', 2001, '#C74375', '17-2031']
    test_values = make_resource_json(values)
    keys = list(test_values.keys())
    for key in keys:
        assert response_data[key] == test_values[key]
    print("get single resource : ", response.status_code)


@pytest.mark.resource
def test_get_not_existing_resource(url):
    response = requests.get(url+'api/unknown/23')
    assert response.status_code == 404
    print("get not existing resource : ", response.status_code)


@pytest.mark.users
def test_get_list_users_delayed(url):
    response = requests.get(url+'/users?delay=3')
    assert response.status_code == 200
    assert response.content is not None
    assert response.json()["page"] == 1
    response_data = response.json()['data'][0]
    values = [1, 'george.bluth@reqres.in', 'George', 'Bluth', 'https://reqres.in/img/faces/1-image.jpg']
    test_values = make_user_json(values)
    keys = list(test_values.keys())
    for key in keys:
        assert response_data[key] == test_values[key]
    print("get list users delayed : ", response.status_code)
