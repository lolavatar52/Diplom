# Екатерина Попова, 26-я когорта — Финальный проект. Инженер по тестированию плюс
# Импортируем данные заказа
from data import order_body
# Импортируем функции создания заказа и получение информации о заказе по номеру трека
from sender_stend_request import create_order, get_order


def test_order_creation_and_retrieval():
    # Создаём заказ
    response_create = create_order(order_body)
    # Сохраняем трек-номер заказа
    order_track = response_create.json()["track"]
    # Получаем информацию о заказе по номеру трека
    response_get = get_order(order_track)
    # Проверяем, что код ответа равен 200
    assert response_get.status_code == 200