import allure
import pytest

from api_methods import create_order
from data import ORDER_DATA


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

        response = create_order(payload)

        assert response.status_code == 201
        created_tracks.append(response.json()['track'])
        assert isinstance(response.json()['track'], int)

    @allure.title('Заказ создаётся без указания цвета: код 201 и в ответе есть track')
    def test_create_order_without_color(self, created_tracks):
        response = create_order(ORDER_DATA)

        assert response.status_code == 201
        created_tracks.append(response.json()['track'])
        assert isinstance(response.json()['track'], int)
        