import allure
import pytest

from api_methods import login_courier
from data import ACCOUNT_NOT_FOUND, NOT_ENOUGH_DATA_FOR_LOGIN
from helpers import generate_random_string


class TestLoginCourier:

    @allure.title('Курьер может авторизоваться: код 200 и в ответе есть id')
    def test_login_courier_success(self, courier):
        payload = {'login': courier['login'], 'password': courier['password']}

        response = login_courier(payload)

        assert response.status_code == 200
        assert isinstance(response.json()['id'], int)

    @allure.title('Нельзя авторизоваться без обязательного поля: {missing_field}')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_login_without_required_field(self, courier, missing_field):
        payload = {'login': courier['login'], 'password': courier['password']}
        payload.pop(missing_field)

        response = login_courier(payload)

        assert response.status_code == 400
        assert response.json()['message'] == NOT_ENOUGH_DATA_FOR_LOGIN

    @allure.title('Ошибка при неправильном значении поля: {wrong_field}')
    @pytest.mark.parametrize('wrong_field', ['login', 'password'])
    def test_login_with_wrong_credentials(self, courier, wrong_field):
        payload = {'login': courier['login'], 'password': courier['password']}
        payload[wrong_field] = generate_random_string(10)

        response = login_courier(payload)

        assert response.status_code == 404
        assert response.json()['message'] == ACCOUNT_NOT_FOUND

    @allure.title('Ошибка при авторизации под несуществующим пользователем')
    def test_login_nonexistent_courier(self):
        payload = {'login': generate_random_string(10), 'password': generate_random_string(10)}

        response = login_courier(payload)

        assert response.status_code == 404
        assert response.json()['message'] == ACCOUNT_NOT_FOUND
        