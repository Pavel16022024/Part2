import data
import requests
import configuration

# Запрос на создание нового заказа
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=order_body)

# Запрос на получение заказа по его трек номеру
def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER + "?t=" + str(track_number))