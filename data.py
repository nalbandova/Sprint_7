BASE_URL = 'https://qa-scooter.praktikum-services.ru'
COURIER = '/api/v1/courier'
LOGIN = '/api/v1/courier/login'
ORDERS = '/api/v1/orders'
ORDER_CANCEL = '/api/v1/orders/cancel'

ORDER_DATA = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-12-06",
    "comment": "Saske, come back to Konoha"
}

COURIER_ALREADY_EXISTS = 'Этот логин уже используется'
NOT_ENOUGH_DATA_FOR_CREATE = 'Недостаточно данных для создания учетной записи'
NOT_ENOUGH_DATA_FOR_LOGIN = 'Недостаточно данных для входа'
ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
COURIER_NOT_FOUND = 'Курьер с идентификатором {} не найден'
