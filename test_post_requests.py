import pytest
import requests


@pytest.fixture
def url():
    return 'https://reqres.in/api'


@pytest.mark.users
def test_post_create_user(url):
    data = {"name": "morpheus", "job": "leader"}
    response = requests.post(url+'/users', data)
    assert response.status_code == 201
    assert response.request.body.find("morpheus") != -1
    assert response.request.body.find("leader") != -1
    print("post create user : ", response.status_code)
    response = requests.get(url+'/users?name=morpheus')
    print(response.status_code)
    assert str(response.content).find('"name":"morpheus", "job":"leader"') != -1


@pytest.mark.register
def test_post_register(url):
    data = {'email': 'eve.holt@reqres.in', "password": "pistol"}
    response = requests.post(url+'/register', data)
    assert response.status_code == 200
    print("post register : ", response.status_code)
    response = requests.get(url + '/register?email=eve.holt@reqres.in')
    print(response.status_code)
    assert str(response.content).find('"email":"eve.holt@reqres.in", "password":"pistol"') != -1


@pytest.mark.register
def test_post_failed_register(url):
    data = {"email": 'eve.holt@reqres.in'}
    response = requests.post(url+'/register', data)
    assert response.status_code == 400
    print("post failed register : ", response.status_code)
    response = requests.get(url + '/register?email=eve.holt@reqres.in')
    print(response.status_code)
    assert str(response.content).find('"email":"eve.holt@reqres.in"') == -1


@pytest.mark.login
def test_post_login(url):
    data = {"email": 'eve.holt@reqres.in', "password": "cityslicka"}
    response = requests.post(url+'/login', data)
    assert response.status_code == 200
    print("post login : ", response.status_code)
    response = requests.get(url + '/login?email=eve.holt@reqres.in')
    print(response.status_code)
    assert str(response.content).find('"email":"eve.holt@reqres.in", "password":"cityslicka"') != -1


@pytest.mark.login
def test_post_failed_login(url):
    data = {"email": "peter@klaven"}
    response = requests.post(url+'/login', data)
    assert response.status_code == 400
    print("post failed login : ", response.status_code)
