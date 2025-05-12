# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные для создания заказа
# содержит имя, фамилию, адрес, станцию метро, телефон, срок аренды, дата оренды, коментарий, цвет самоката
order_body = {
    "firstName": "Vasily",
    "lastName": "Vakulenko",
    "address": "Rostov-na-Donu, dom 1488.",
    "metroStation": 9,
    "phone": "+7 800 555 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-01-02",
    "comment": "Moya igra, ona mne prinadlezhit",
    "color": [
        "BLACK"
    ]
}  
