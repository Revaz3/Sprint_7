CREATE_COURIER = 'http://qa-scooter.praktikum-services.ru/api/v1/courier'
LOGIN_COURIER = 'http://qa-scooter.praktikum-services.ru/api/v1/courier/login'
CREATE_ORDER = 'http://qa-scooter.praktikum-services.ru/api/v1/orders'
GET_ORDERS = 'http://qa-scooter.praktikum-services.ru/api/v1/orders'

login_valid = 'Mark'
password_valid = '3222244!'

order_data_black = {
    "firstName": "Garry",
    "lastName": "Potter",
    "address": "Moscow",
    "metroStation": 4,
    "phone": "+7 963 225 95 95",
    "rentTime": 5,
    "deliveryDate": "2024-08-06",
    "comment": "S",
    "color": [
        "BLACK"
    ]
}

order_data_grey = {
    "firstName": "Frodo",
    "lastName": "Baggyns",
    "address": "Moscow",
    "metroStation": 4,
    "phone": "+7 903 339 67 08",
    "rentTime": 5,
    "deliveryDate": "2024-08-06",
    "comment": "Go",
    "color": [
        "GREY"
    ]
}

order_data_multicolor = {
    "firstName": "Fred",
    "lastName": "Barny",
    "address": "Moscow",
    "metroStation": 3,
    "phone": "+7 916 378 9643",
    "rentTime": 1,
    "deliveryDate": "2024-08-06",
    "comment": "Fast",
    "color": [
        "GREY", "BLACK"
    ]
}

order_data_no_color = {
    "firstName": "Kot",
    "lastName": "Matroskin",
    "address": "Prostokvashino",
    "metroStation": 3,
    "phone": "+7 967 235 7508",
    "rentTime": 4,
    "deliveryDate": "2024-08-06",
    "comment": "Korova",
    "color": []
}