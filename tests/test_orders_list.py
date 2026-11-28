import allure

from api_methods import get_orders
from data import COURIER_NOT_FOUND


class TestOrdersList:

    @allure.title('В теле ответа возвращается список заказов')
    def test_get_orders_list(self):
        response = get_orders()

        assert response.status_code == 200
        assert isinstance(response.json()['orders'], list)

    @allure.title('Список заказов существующего курьера возвращается списком')
    def test_get_orders_list_of_courier(self, courier_id):
        response = get_orders({'courierId': courier_id})

        assert response.status_code == 200
        assert isinstance(response.json()['orders'], list)

    @allure.title('Ошибка при запросе заказов несуществующего курьера')
    def test_get_orders_list_of_nonexistent_courier(self):
        nonexistent_id = 999999999

        response = get_orders({'courierId': nonexistent_id})

        assert response.status_code == 404
        assert COURIER_NOT_FOUND.format(nonexistent_id) in response.json()['message']
        