import allure
import pytest

from api_methods import create_courier
from data import COURIER_ALREADY_EXISTS, NOT_ENOUGH_DATA_FOR_CREATE


class TestCreateCourier:

    @allure.title('Курьера можно создать: код 201 и ok равно true')
    def test_create_courier_success(self, new_courier_data):
        response = create_courier(new_courier_data)

        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_duplicate_courier(self, courier):
        response = create_courier(courier)

        assert response.status_code == 409
        assert COURIER_ALREADY_EXISTS in response.json()['message']

    @allure.title('Нельзя создать курьера с уже существующим логином, но другими данными')
    def test_create_courier_with_existing_login(self, courier):
        payload = {'login': courier['login'], 'password': 'other_password', 'firstName': 'other_name'}

        response = create_courier(payload)

        assert response.status_code == 409
        assert COURIER_ALREADY_EXISTS in response.json()['message']

    @allure.title('Нельзя создать курьера без обязательного поля: {missing_field}')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_without_required_field(self, new_courier_data, missing_field):
        payload = new_courier_data.copy()
        payload.pop(missing_field)

        response = create_courier(payload)

        assert response.status_code == 400
        assert response.json()['message'] == NOT_ENOUGH_DATA_FOR_CREATE
        