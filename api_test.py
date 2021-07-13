import requests
import json
import json

url = 'https://reqres.in/'


def test_get_list_users():
    response = requests.get(url+'api/users?page=2')
    assert response.status_code == 200
    print("get list users : ", response.status_code)


def test_get_single_user():
    response = requests.get(url+'api/users?2')
    assert response.status_code == 200
    print("get single user : ", response.status_code)


def test_get_not_existing_user():
    response = requests.get(url+'api/users/23')
    assert response.status_code == 404
    print("get not existing user : ", response.status_code)


def test_get_list_resource():
    response = requests.get(url+'api/unknown')
    assert response.status_code == 200
    print("get list resource : ", response.status_code)


def test_get_single_resource():
    response = requests.get(url+'api/unknown/2')
    assert response.status_code == 200
    print("get single resource : ", response.status_code)


def test_get_not_existing_resource():
    response = requests.get(url+'api/unknown/23')
    assert response.status_code == 404
    print("get not existing resource : ", response.status_code)


def test_post_create_user():
    data = {"name": "morpheus", "job": "leader"}
    json_data = json.dumps(data)
    response = requests.post(url+'api/users', json_data)
    assert response.status_code == 201
    print("post create user : ", response.status_code)


def test_put_update_user():
    data = {"name": "morpheus", "job": "zion resident"}
    json_data = json.dumps(data)
    response = requests.put(url+'api/users/2', json_data)
    assert response.status_code == 200
    print("put update user : ", response.status_code)


def test_patch_update_user():
    data = {"name": "morpheus", "job": "zion resident"}
    json_data = json.dumps(data)
    response = requests.patch(url+'api/users/2', json_data)
    assert response.status_code == 200
    print("patch update user : ", response.status_code)


def test_delete_user():
    response = requests.delete(url+'api/user/2')
    assert response.status_code == 204
    print("delete user : ", response.status_code)


def test_post_register():
    data = {"email": 'eve.holt@reqres.in', "password": "pistol"}
    json_data = json.dumps(data)
    response = requests.post(url+'api/register', data)
    assert response.status_code == 200
    print("post register : ", response.status_code)


def test_post_failed_register():
    data = {"email": 'eve.holt@reqres.in'}
    json_data = json.dumps(data)
    response = requests.post(url+'api/register', json_data)
    assert response.status_code == 400
    print("post failed register : ", response.status_code)


def test_post_login():
    data = {"email": 'eve.holt@reqres.in', "password": "cityslicka"}
    json_data = json.dumps(data)
    response = requests.post(url+'api/login', data)
    assert response.status_code == 200
    print("post login : ", response.status_code)


def test_post_failed_login():
    data = {"email": "peter@klaven"}
    json_data = json.dumps(data)
    response = requests.post(url+'api/login', json_data)
    assert response.status_code == 400
    print("post failed login : ", response.status_code)


def test_get_list_users_delayed():
    response = requests.get(url+'api/users?delay=3')
    assert response.status_code == 200
    print("get list users delayed : ", response.status_code)


test_get_list_users()
test_get_single_user()
test_get_not_existing_user()
test_get_list_resource()
test_get_single_resource()
test_get_not_existing_resource()
test_post_create_user()
test_put_update_user()
test_patch_update_user()
test_delete_user()
test_post_register()
test_post_failed_register()
test_post_login()
test_post_failed_login()
test_get_list_users_delayed()
