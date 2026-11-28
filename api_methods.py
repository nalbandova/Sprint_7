import allure
import requests

from data import BASE_URL, COURIER, LOGIN, ORDERS, ORDER_CANCEL


@allure.step('Создать курьера')
def create_courier(payload):
    return requests.post(BASE_URL + COURIER, data=payload)


@allure.step('Авторизовать курьера')
def login_courier(payload):
    return requests.post(BASE_URL + LOGIN, data=payload)


@allure.step('Удалить курьера')
def delete_courier(login, password):
    response = login_courier({'login': login, 'password': password})
    if response.status_code == 200:
        return requests.delete(f"{BASE_URL}{COURIER}/{response.json()['id']}")


@allure.step('Создать заказ')
def create_order(payload):
    return requests.post(BASE_URL + ORDERS, json=payload)


@allure.step('Отменить заказ')
def cancel_order(track):
    return requests.put(BASE_URL + ORDER_CANCEL, json={'track': track})


@allure.step('Получить список заказов')
def get_orders(params=None):
    return requests.get(BASE_URL + ORDERS, params=params)
