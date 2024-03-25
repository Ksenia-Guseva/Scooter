# Гусева Ксения, 14-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data
# Функция для позитивной проверки
def positive_assert(track):
    order_response = sender_stand_request.get_treck_order(track)
    assert order_response.status_code == 200

# Тест 1. Статус заказа
def test_get_order_track_success_response():
    positive_assert(sender_stand_request.track)
    response = sender_stand_request.post_new_orders(data.order_body)
    track = response.json()["track"]
    order_response = sender_stand_request.get_treck_order(track)
    assert order_response.status_code == 200