import pytest
import requests


@pytest.fixture
def url():
    return 'https://reqres.in/api'


@pytest.mark.users
def test_delete_user(url):
    response = requests.delete(url+'/user/2')
    assert response.status_code == 204
    print("delete user : ", response.status_code)
    response = requests.get(url + '/users/2')
    print(response.status_code)
    assert response.status_code == 404
