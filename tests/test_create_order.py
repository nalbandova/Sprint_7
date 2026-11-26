import allure
import pytest
import requests
from data import BASE_URL, ORDERS, ORDER_CANCEL, ORDER_DATA


@pytest.fixture
def created_tracks():
    """Список треков заказов, созданных в тесте. После теста все заказы отменяются."""
    tracks = []
    yield tracks
    for track in tracks:
        requests.put(BASE_URL + ORDER_CANCEL, json={'track': track})


class TestCreateOrder:

    @allure.title('Заказ создаётся с цветом {color}: код 201 и в ответе есть track')
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        []
    ], ids=['black', 'grey', 'black_and_grey', 'empty_color'])
    def test_create_order_with_color(self, created_tracks, color):
        payload = {**ORDER_DATA, 'color': color}

        response = requests.post(BASE_URL + ORDERS, json=payload)
        if response.status_code == 201:
            created_tracks.append(response.json()['track'])

        assert response.status_code == 201
        assert isinstance(response.json()['track'], int)

    @allure.title('Заказ создаётся без указания цвета: код 201 и в ответе есть track')
    def test_create_order_without_color(self, created_tracks):
        response = requests.post(BASE_URL + ORDERS, json=ORDER_DATA)
        if response.status_code == 201:
            created_tracks.append(response.json()['track'])

        assert response.status_code == 201
        assert isinstance(response.json()['track'], int)
