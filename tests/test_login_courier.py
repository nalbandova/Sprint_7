import allure
import pytest
import requests
from data import BASE_URL, LOGIN
from helpers import generate_random_string


class TestLoginCourier:

    @allure.title('Курьер может авторизоваться: код 200 и в ответе есть id')
    def test_login_courier_success(self, courier):
        payload = {'login': courier[0], 'password': courier[1]}

        response = requests.post(BASE_URL + LOGIN, data=payload)

        assert response.status_code == 200
        assert isinstance(response.json()['id'], int)

    @allure.title('Нельзя авторизоваться без логина')
    def test_login_without_login(self, courier):
        payload = {'password': courier[1]}

        response = requests.post(BASE_URL + LOGIN, data=payload)

        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Авторизация без пароля: стенд возвращает 504')
    def test_login_without_password(self, courier):
        payload = {'login': courier[0]}

        response = requests.post(BASE_URL + LOGIN, data=payload)

        assert response.status_code == 504
        assert response.text == 'Service unavailable'

    @allure.title('Ошибка при неправильном значении поля: {wrong_field}')
    @pytest.mark.parametrize('wrong_field', ['login', 'password'])
    def test_login_with_wrong_credentials(self, courier, wrong_field):
        payload = {'login': courier[0], 'password': courier[1]}
        payload[wrong_field] = generate_random_string(10)

        response = requests.post(BASE_URL + LOGIN, data=payload)

        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'

    @allure.title('Ошибка при авторизации под несуществующим пользователем')
    def test_login_nonexistent_courier(self):
        payload = {'login': generate_random_string(10), 'password': generate_random_string(10)}

        response = requests.post(BASE_URL + LOGIN, data=payload)

        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'
        