import pytest
from helpers import (register_new_courier_and_return_login_password,
                    generate_random_string, delete_courier)
import requests
from data import BASE_URL, LOGIN


@pytest.fixture
def courier():
    """Курьер, уже созданный в системе. После теста удаляется."""
    login_pass = register_new_courier_and_return_login_password()
    assert login_pass, 'Не удалось создать курьера для теста'
    yield login_pass  # [login, password, first_name]
    delete_courier(login_pass[0], login_pass[1])


@pytest.fixture
def new_courier_data():
    """Данные для создания курьера, самого курьера в системе ещё нет. После теста удаляется."""
    payload = {
        'login': generate_random_string(10),
        'password': generate_random_string(10),
        'firstName': generate_random_string(10)
    }
    yield payload
    delete_courier(payload['login'], payload['password'])

@pytest.fixture
def courier_id(courier):
    """id курьера, созданного фикстурой courier. Сам курьер удаляется после теста."""
    response = requests.post(BASE_URL + LOGIN,
                            data={'login': courier[0], 'password': courier[1]})
    assert response.status_code == 200, 'Не удалось получить id курьера'
    return response.json()['id']
