import requests
import json
import pytest


@pytest.fixture
def url():
    return 'https://reqres.in/api'


@pytest.mark.parametrize("path, status, verify", [('/users?page=2', 200, '"page":2'), ('/users/2', 200, '"id":2'),
                                                  ('/users/23', 404, None), ('/unknown', 200, '"page":1'),
                                                  ('/unknown/2', 200, '"id":2'), ('/unknown/23', 404, None),
                                                  ('/users?delay=3', 200, '"page":1')])
@pytest.mark.get
def test_get_list_users(url, path, status, verify):
    response = requests.get(url+path)
    assert response.status_code == status
    assert response.content is not None
    if verify is not None:
        assert str(response.content).find(verify) != -1
    print("get response status : ", response.status_code)


def test_post_create_user(url):
    data = {"name": "morpheus", "job": "leader"}
    json_data = json.dumps(data)
    response = requests.post(url+'/users', json_data)
    assert response.status_code == 201
    assert response.request.body.find("morpheus") != -1
    assert response.request.body.find("leader") != -1
    print("post create user : ", response.status_code)
    response = requests.get(url+'/users?name=morpheus')
    print(response.status_code)
    assert str(response.content).find('"name":"morpheus", "job":"leader"') != -1


@pytest.mark.put
def test_put_update_user(url):
    data = {"name": "morpheus", "job": "zion resident"}
    json_data = json.dumps(data)
    response = requests.put(url+'/users/2', json_data)
    assert response.status_code == 200
    print("put update user : ", response.status_code)
    response = requests.get(url + '/users?2')
    print(response.status_code)
    assert str(response.content).find('"name":"morpheus", "job":"zion resident"') != -1


@pytest.mark.patch
def test_patch_update_user(url):
    data = {"name": "morpheus", "job": "zion resident"}
    json_data = json.dumps(data)
    response = requests.patch(url+'/users/2', json_data)
    assert response.status_code == 200
    print("patch update user : ", response.status_code)
    response = requests.get(url + '/users?2')
    print(response.status_code)
    assert str(response.content).find('"name":"morpheus", "job":"zion resident"') != -1


@pytest.mark.delete
def test_delete_user(url):
    response = requests.delete(url+'/user/2')
    assert response.status_code == 204
    print("delete user : ", response.status_code)
    response = requests.get(url + '/users/2')
    print(response.status_code)
    assert response.status_code == 404


@pytest.mark.post
def test_post_register(url):
    data = {'email': 'eve.holt@reqres.in', "password": "pistol"}
    response = requests.post(url+'/register', data)
    assert response.status_code == 200
    print("post register : ", response.status_code)
    response = requests.get(url + '/register?email=eve.holt@reqres.in')
    print(response.status_code)
    assert str(response.content).find('"email":"eve.holt@reqres.in", "password":"pistol"') != -1


@pytest.mark.post
def test_post_failed_register(url):
    data = {"email": 'eve.holt@reqres.in'}
    json_data = json.dumps(data)
    response = requests.post(url+'/register', json_data)
    assert response.status_code == 400
    print("post failed register : ", response.status_code)
    response = requests.get(url + '/register?email=eve.holt@reqres.in')
    print(response.status_code)
    assert str(response.content).find('"email":"eve.holt@reqres.in"') == -1


@pytest.mark.post
def test_post_login(url):
    data = {"email": 'eve.holt@reqres.in', "password": "cityslicka"}
    response = requests.post(url+'/login', data)
    assert response.status_code == 200
    print("post login : ", response.status_code)
    response = requests.get(url + '/login?email=eve.holt@reqres.in')
    print(response.status_code)
    assert str(response.content).find('"email":"eve.holt@reqres.in", "password":"cityslicka"') != -1


@pytest.mark.post
def test_post_failed_login(url):
    data = {"email": "peter@klaven"}
    json_data = json.dumps(data)
    response = requests.post(url+'/login', json_data)
    assert response.status_code == 400
    print("post failed login : ", response.status_code)
