import pytest
import requests


@pytest.fixture
def url():
    return 'https://reqres.in/api'


@pytest.mark.users
def test_patch_update_user(url):
    data = {"name": "morpheus", "job": "zion resident"}
    response = requests.patch(url+'/users/2', data)
    assert response.status_code == 200
    print("patch update user : ", response.status_code)
    response = requests.get(url + '/users?2')
    print(response.status_code)
    assert str(response.content).find('"name":"morpheus", "job":"zion resident"') != -1
