import pytest
import requests


@pytest.fixture()
def new_post_id():
    body = {
        "userId": 1,
        "title": "Varzhuhi",
        "body": "Muradyan"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    yield 1
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{post_id}')


@pytest.fixture()
def new_post_id_without_delete():
    body = {
        "userId": 1,
        "title": "Varzhuhi",
        "body": "Muradyan"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=body,
        headers=headers
    )
    post_id = response.json()['id']
    yield 1



@pytest.fixture(scope='session')
def start_session():
    print('START')
    yield
    print('END')