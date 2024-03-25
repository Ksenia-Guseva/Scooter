import configuration
import requests
import data

def post_new_orders (order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                             json=order_body)
response = post_new_orders(data.order_body)
print(response.status_code)

#Сохраняем трек
track = response.json()["track"]
print(track)


# Запрос на получение информации о заказе по треку
def get_treck_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TRACK_ORDER, params={"t": track})
response = get_treck_order(track)
print(response.status_code)