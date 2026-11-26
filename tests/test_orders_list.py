import allure
import pytest
import requests
from data import BASE_URL, ORDERS


class TestOrdersList:

    @allure.title('В теле ответа возвращается список заказов')
    def test_get_orders_list(self):
        response = requests.get(BASE_URL + ORDERS)

        assert response.status_code == 200
        assert isinstance(response.json()['orders'], list)

    @allure.title('Список заказов существующего курьера возвращается списком')
    def test_get_orders_list_of_courier(self, courier_id):
        response = requests.get(BASE_URL + ORDERS, params={'courierId': courier_id})

        assert response.status_code == 200
        assert isinstance(response.json()['orders'], list)

    @allure.title('Ошибка при запросе заказов несуществующего курьера')
    def test_get_orders_list_of_nonexistent_courier(self):
        nonexistent_id = 999999999

        response = requests.get(BASE_URL + ORDERS, params={'courierId': nonexistent_id})

        assert response.status_code == 404
        assert f'Курьер с идентификатором {nonexistent_id} не найден' in response.json()['message']
        