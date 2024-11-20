import requests
import json
import hashlib
import random
from secret import *
import time
import csv_reader


# TEST_DATA_SDEK = {
#     {
# 	"number" : "ddOererre7450813980068",
# 	"comment" : "Новый заказ",
# 	"delivery_recipient_cost" : {
# 		"value" : 50
# 	},
# 	"delivery_recipient_cost_adv" : [ {
# 		"sum" : 3000,
# 		"threshold" : 200
# 	} ],
# 	"from_location" : {
# 		"code" : "44",
# 		"fias_guid" : "",
# 		"postal_code" : "",
# 		"longitude" : "",
# 		"latitude" : "",
# 		"country_code" : "",
# 		"region" : "",
# 		"sub_region" : "",
# 		"city" : "Москва",
# 		"kladr_code" : "",
# 		"address" : "пр. Ленинградский, д.4"
# 	},
# 	"to_location" : {
# 		"code" : "270",
# 		"fias_guid" : "",
# 		"postal_code" : "",
# 		"longitude" : "",
# 		"latitude" : "",
# 		"country_code" : "",
# 		"region" : "",
# 		"sub_region" : "",
# 		"city" : "Новосибирск",
# 		"kladr_code" : "",
# 		"address" : "ул. Блюхера, 32"
# 	},
# 	"packages" : [ {
# 		"number" : "bar-001",
# 		"comment" : "Упаковка",
# 		"height" : 10,
# 		"items" : [ {
# 			"ware_key" : "00055",
# 			"payment" : {
# 				"value" : 3000
# 			},
# 			"name" : "Товар",
# 			"cost" : 300,
# 			"amount" : 2,
# 			"weight" : 700,
# 			"url" : "www.item.ru"
# 		} ],
# 	"length" : 10,
# 	"weight" : 4000,
# 	"width" : 10
# 	} ],
# 	"recipient" : {
# 		"name" : "Иванов Иван",
# 		"phones" : [ {
# 		"number" : "+79134637228"
# 	} ]
# 	},
# 	"sender" : {
# 		"name" : "Петров Петр"
# 	},
# 	"services" : [ {
# 		"code" : "SECURE_PACKAGE_A2"
# 	} ],
# 	"tariff_code" : 139
#     }
#     }

# TEST_DATA_DELLIN = {
#     "order": {
#         "providerConnectId": 27517, # 27282 - Компас, # 26933 - Ржанов # 27517 - Деловые линии
#         "providerKey": "dellin", # код службы доставки
#         "pickupType": 1, # 1 - от двери, 2 - со склада
#         "deliveryType": 1, # 1 - до двери, 2 - до ПВЗ
#         "tariffId": 10699, # тариф службы доставки
#         "pickupDate": "2023-09-30",
#         "weight": 100,
#         "clientNumber": '12345'
#     },
#     "places": {
#         "height": 10,
#         "length": 10,
#         "width": 10,
#         "weight": 100,
#         "items": [{
#             "description": "Товар",
#             "quantity": 1
#         }]
#     },
#     "cost": {
#         "assessedCost": 100,
#         "codCost": 0, # сумма наложенного платежа
#         "isDeliveryPayedByRecipient": 0 # 0 - за доставку платит отправитель, 1 - получатель
#     },
#     "sender": {
#         "countryCode": "RU",
#         "postIndex": "117105",
#         "region": "Москва",
#         "city": "Москва",
#         "street": "проезд Нагорный",
#         "house": "7",
#         "block": "1",
#         "companyName": "Магазин Охраны Труды",
#         "contactName": "Кириллов Игорь",
#         "phone": "+7(495)215-52-41",
#         "comment": "тестовый комментарий",
#     },
#     "recipient": {
#         "countryCode": "RU",
#         "postIndex": "119634",
#         "region": "Москва",
#         "city": "Москва",
#         "street": "ул Лукинская",
#         "house": "7",
#         "block": "1",
#         "contactName": "Иванов Иван",
#         "phone": "+7(495)777-77-77",
#     },
#     "returnAddress": {
#         "countryCode": "RU",
#         "postIndex": "117105",
#         "region": "Москва",
#         "city": "Москва",
#         "street": "проезд Нагорный",
#         "house": "7",
#         "block": "1",
#         "companyName": "Магазин Охраны Труды",
#         "contactName": "Кириллов Игорь",
#         "phone": "+7(495)215-52-41",
#         "comment": "тестовый комментарий",
#     },
#     "places": [
#         {
#         "weight": 100,
#         "items": [
#             {
#             "weight": 100,
#             "description": "Товар 1",
#             "quantity": 1,
#             "assessedCost": 100,
#             }
#         ]
#         }
#     ],
#     "extraParams": [
#         {
#         "key": "testParam",
#         "value": "testValue"
#         }
#     ]
#     }




def apiship_auth():
    url = 'https://api.cdek.ru/v2/oauth/token?parameters'
    data = {
        {
        "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZSI6WyJvcmRlcjphbGw...",
        "token_type": "bearer",
        "expires_in": 3599,
        "scope": "order:all payment:all",
        "jti": "9adca50a-..."
        }
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response.json()




def get_auth_token():
    data = {'grant_type': 'client_credentials',
            'client_id': 'wx1coJQ59TqKYSbGe78KCqFPu2W0ptRN',
            'client_secret': 'JtiYuzo8SVYpa3L5vTeui2RyjSqNmMRE'}
    response = requests.post('https://api.cdek.ru/v2/oauth/token?parameters', data=data)
    try:

        return response.json()['access_token']
    except:
        # заглушка с неверным токеном
        print('lol')




def create_order(data):
    response = requests.post('https://api.cdek.ru/v2/orders',
                            json=data,
                           headers={'Authorization': 'Bearer {}'.format(get_auth_token())})
    return response.json()

def get_info(uid):
    response = requests.get('https://api.cdek.ru/v2/orders/' + uid,
                            json=data,
                           headers={'Authorization': 'Bearer {}'.format(get_auth_token())})

    return response.json()


def create_courier(uid, cdek_num, weight):
    data_courier = {
    "cdek_number": cdek_num,
    "order_uuid" : uid,
    "intake_date": "2025-10-24",
    "intake_time_from": "10:00",
    "intake_time_to": "17:00",
    # "name": name,
    "weight": weight,
    "sender": {
        "phones": [
            {
                "number": "+79589441654"
            }
        ]
    },
    
    "from_location": {
        #"fias_guid": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
        "city": "Москва",
        "address": "ул. Блюхера, 32"
    },
}
    
    response = requests.post('https://api.cdek.ru/v2/intakes',
                            json=data_courier,
                           headers={'Authorization': 'Bearer {}'.format(get_auth_token())})
    return response.json()


# data = {
# 	# "number" : "ddOererre7450813980068",
# 	"comment" : "Новый заказ",
# 	"delivery_recipient_cost" : {
# 		"value" : 50
# 	},
# 	"delivery_recipient_cost_adv" : [ {
# 		"sum" : 3000,
# 		"threshold" : 200
# 	} ],
# 	"from_location" : {
# 		"code" : "44",
# 		"fias_guid" : "",
# 		"postal_code" : "",
# 		"longitude" : "",
# 		"latitude" : "",
# 		"country_code" : "",
# 		"region" : "",
# 		"sub_region" : "",
# 		"city" : "Москва",
# 		"kladr_code" : "",
# 		"address" : "пр. Ленинградский, д.4"
# 	},
# 	"to_location" : {
# 		"code" : "270",
# 		"fias_guid" : "",
# 		"postal_code" : "",
# 		"longitude" : "",
# 		"latitude" : "",
# 		"country_code" : "",
# 		"region" : "",
# 		"sub_region" : "",
# 		"city" : "Новосибирск",
# 		"kladr_code" : "",
# 		"address" : "ул. Блюхера, 32"
# 	},
# 	"packages" : [ {
# 		"number" : "bar-001",
# 		"comment" : "Упаковка",
# 		"height" : 10,
# 		"items" : [ {
# 			"ware_key" : "00055",
# 			"payment" : {
# 				"value" : 3000
# 			},
# 			"name" : "Товар",
# 			"cost" : 300,
# 			"amount" : 2,
# 			"weight" : 700,
# 			"url" : "www.item.ru"
# 		} ],
# 	"length" : 10,
# 	"weight" : 800,
# 	"width" : 10,
#     "height": 10
# 	} ],
# 	"recipient" : {
# 		"name" : "Иванов Иван",
# 		"phones" : [ {
# 		"number" : "+79134637228"
# 	} ]
# 	},
# 	"sender" : {
# 		"name" : "Петров Петр", 
#         "type" : 2
# 	},
	
# 	"tariff_code" : 139
# }




def receipt_create(uuid):
    data = {
    "orders": [
        {
            "order_uuid": uuid
        }
    ],
    "copy_count": 2
}
    response = requests.post('https://api.cdek.ru/v2/print/orders',
                            json=data,
                           headers={'Authorization': 'Bearer {}'.format(get_auth_token())})

    return response.json()


def receipt_get(uuid):
    response = requests.get('https://api.cdek.ru/v2/print/orders/' + uuid,
                            #json=data,
                           headers={'Authorization': 'Bearer {}'.format(get_auth_token())})

    return response.json()




def download_receipt(link):
    response = requests.get(link,
                           headers={'Authorization': 'Bearer {}'.format(get_auth_token())})
    
    if response.status_code == 200:
        with open('nakladnaya.pdf', "wb") as file:
            file.write(response.content)
        print("Файл успешно скачан и сохранён.")
    else:
        print("Не удалось скачать файл. Код ошибки:", response.status_code)

    return response

data = csv_reader.main()[0]
print(data, '1111111111111111111111111')

create = create_order(data)


uuid = create['entity']['uuid']

info = get_info(uuid)
print(info, 2222222222222222222222222222222)
info_uid = info['entity']['uuid']
rec = receipt_create(uuid)

time.sleep(3)
uuid_for_receipt = rec['entity']['uuid']
print(uuid_for_receipt, '---------')
answer_for_receipt_get = receipt_get(uuid_for_receipt)
print(answer_for_receipt_get)

time.sleep(3)
print(download_receipt(answer_for_receipt_get['entity']['url']))
info = get_info(info_uid)
print(info, '33333333333333333333')
info_cdek_num = info['entity']['cdek_number']
time.sleep(3)

weigt_for_courier = data['packages'][0]['weight']
# name_for_courier = data['packages'][0]['items'][0]['name']
print(create_courier(info_uid, info_cdek_num, weigt_for_courier))

