# diplom_13

Автотест на создание курьера и проверки, что по треку заказа можно получить данные о заказе.
- Для запуска тестов должны быть установлены пакеты pytest и requests (через вкладку терминал: pip install pytest / pip install requests);
- Запуск всех тестов выполняется командой pytest.

Работа с базой данных

- Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).

- Задание 2
Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.
