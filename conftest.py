import pytest

from api_methods import create_courier, delete_courier, login_courier, cancel_order
from helpers import generate_courier_data


@pytest.fixture
def courier():
    """Курьер, созданный в системе. После теста удаляется."""
    payload = generate_courier_data()
    create_courier(payload)
    yield payload
    delete_courier(payload['login'], payload['password'])


@pytest.fixture
def new_courier_data():
    """Данные нового курьера, которого ещё нет в системе. После теста курьер удаляется."""
    payload = generate_courier_data()
    yield payload
    delete_courier(payload['login'], payload['password'])


@pytest.fixture
def courier_id(courier):
    """id курьера, созданного фикстурой courier."""
    response = login_courier({'login': courier['login'], 'password': courier['password']})
    return response.json()['id']


@pytest.fixture
def created_tracks():
    """Список треков заказов, созданных в тесте. После теста заказы отменяются."""
    tracks = []
    yield tracks
    for track in tracks:
        cancel_order(track)
        