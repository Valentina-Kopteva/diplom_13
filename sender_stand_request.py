import requests
import configuration

#создание заказа с телом из order_body
def create_order(order_body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=order_body)

#получение данных о заказе по треку
def get_order_info_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFO + str(track))
