# Sprint_7: тестирование API Яндекс.Самокат

Автотесты для API учебного сервиса [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/).
Документация API: https://qa-scooter.praktikum-services.ru/docs/

## Что проверяется

- **Создание курьера** (`POST /api/v1/courier`): успешное создание, дубликаты, обязательные поля, коды и тела ответов.
- **Логин курьера** (`POST /api/v1/courier/login`): успешный вход и `id` в ответе, обязательные поля, неверные данные, несуществующий пользователь.
- **Создание заказа** (`POST /api/v1/orders`): параметризованные тесты по цвету (BLACK, GREY, оба, пустой список, без поля), наличие `track`.
- **Список заказов** (`GET /api/v1/orders`): в ответе возвращается список заказов, ошибка для несуществующего курьера.

Тесты независимы. Курьеры и заказы создаются перед тестом, а после него курьеры удаляются, заказы отменяются.

## Структура проекта

```
Sprint_7/
├── tests/
│   ├── test_create_courier.py
│   ├── test_login_courier.py
│   ├── test_create_order.py
│   └── test_orders_list.py
├── conftest.py        # фикстуры
├── data.py            # URL, ручки, тестовые данные
├── helpers.py         # генерация данных, удаление курьера
├── requirements.txt
└── allure_report/     # готовый Allure-отчёт
```

## Установка и запуск

```
python -m venv .venv
source .venv/Scripts/activate      # Windows (Git Bash)
pip install -r requirements.txt
pytest -v
```

## Allure-отчёт

```
pytest --alluredir=allure_results
allure generate allure_results -o allure_report --clean
allure open allure_report
```

## Известные расхождения стенда с документацией

Тесты ожидают фактические ответы стенда:

| Запрос | По документации | Фактически |
|---|---|---|
| Логин курьера без поля `password` | 400, `Недостаточно данных для входа` | 504, `Service unavailable` |
