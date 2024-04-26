import sender_stand_requests
import data

# Павел Шалаев, 15-я когорта — Финальный проект. Инженер по тестированию плюс

# Тест проверки создания заказа
def test_create_order():
    order_response = sender_stand_requests.create_order(data.order_body)
    track_number = order_response.json()["track"]
    get_order_response = sender_stand_requests.get_order(track_number)

    assert get_order_response.status_code == 200