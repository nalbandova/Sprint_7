import allure
import pytest
import requests
from data import BASE_URL, COURIER


class TestCreateCourier:

    @allure.title('Курьера можно создать: код 201 и "ok": true')
    def test_create_courier_success(self, new_courier_data):
        response = requests.post(BASE_URL + COURIER, data=new_courier_data)

        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self, courier):
        payload = {'login': courier[0], 'password': courier[1], 'firstName': courier[2]}

        response = requests.post(BASE_URL + COURIER, data=payload)

        assert response.status_code == 409
        assert 'Этот логин уже используется' in response.json()['message']

    @allure.title('Нельзя создать курьера с уже существующим логином, но другими данными')
    def test_create_courier_with_existing_login(self, courier):
        payload = {'login': courier[0], 'password': 'other_password', 'firstName': 'other_name'}

        response = requests.post(BASE_URL + COURIER, data=payload)

        assert response.status_code == 409
        assert 'Этот логин уже используется' in response.json()['message']

    @allure.title('Нельзя создать курьера без обязательного поля: {missing_field}')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_without_required_field(self, new_courier_data, missing_field):
        payload = new_courier_data.copy()
        payload.pop(missing_field)

        response = requests.post(BASE_URL + COURIER, data=payload)

        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'
        