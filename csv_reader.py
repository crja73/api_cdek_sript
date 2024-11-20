import csv


def main():
    def get_all_information(file_name):
        list_of_orders = []
        with open(file_name) as scv_file:   # расширение поставить под себя
            csv_reader = csv.reader(scv_file)
            for row in csv_reader:    # это перебираем сырые стрки в csv
                oreder_list = []   # это мы создаем списко, чтобы туда красиво закинуть все параметры заказа после обработки, так как в ожном элементе списка может быть несколько других (не разделившихся) элементов
                for inf in ';'.join(row).split(';'):
                    new_inf = inf.replace(';', '')   # избалвяемся от лишней ';'
                    new_inf = new_inf.strip()
                    if new_inf != '' and new_inf != '-':
                        oreder_list.append(new_inf)
                list_of_orders.append(oreder_list)   # в оьбщий список заказов закидываем сформированные и обработанный заказ

            del list_of_orders[0]   # удаление наименований столбцов

        return list_of_orders

    get_all_information('Telegram_Bot_Compas-СДЭК.csv')

    def create_json():
        def crete_data(order):
        #[0'Ирина Кириллова', 1'Ржанов Артем Владимирович', 2'74952155241', 3'16', 4'magazinot@mail.ru', 5'Москва', 6'Нагорный проезд', 7'7с1', 8'1100', 9'Макарова Екатерина Владимировна', 10'ПЛАСТИКФИЛМ', 11'7802578575', 12'79001151622', 13'209', 14'170100 г. Тверь', 15'ул. Красные Горки', 16'д.32 стр.4', 17'1-30-20-8-1800-Товары ОТ #69639', 18'Товары ОТ']
            city_from = order[5]
            address_from = " ".join(order[6:9])
            recip_company = order[10]
            recip_name = order[9]
            tin_1 = order[11]
            recip_phone_number = ''.join(order[12][1:])
            recip_phone_number = '7' + recip_phone_number
            sender_name = order[0]
            sender_company = order[1]
            sender_phones = order[2]
            
            if len(order) == 19:
                size_info = order[17].split('-')
                length = int(size_info[1])    # длина
                weight = int(size_info[4])    # вес
                width = int(size_info[2])   # ширина
                height = int(size_info[3])     # высота
                comment_package = size_info[-1]   # коментарий к упаковке
                city_to = order[14]
                adres_to = ''.join(order[15:17])
                order_name = order[18]
            else:
                size_info = order[16].split('-')
                length = int(size_info[1])    # длина
                weight = int(size_info[4])    # вес
                width = int(size_info[2])   # ширина
                height = int(size_info[3])     # высота
                comment_package = size_info[-1]   # коментарий к упаковке
                city_to = order[13]
                adres_to = ''.join(order[14:16])
                order_name = order[17]
                

                data = {
            "type": 2,
            # "number" : "ddOererre7450813980068",
            "comment" : "Новый заказ",
            # "delivery_recipient_cost" : {
            # 	"value" : 50
            # },
            # "delivery_recipient_cost_adv" : [ {
            # 	"sum" : 3000,
            # 	"threshold" : 200
            # } ],
            "from_location" : {
                #"code" : "44",
                #"fias_guid" : "",
                # "postal_code" : "",
                # "longitude" : "",
                # "latitude" : "",
                # "country_code" : "",
                # "region" : "",
                # "sub_region" : "",
                "city" : city_from,
                #"kladr_code" : "",
                "address" : address_from
            },
            "to_location" : {
                #"code" : "270",  #это пвз код
                # "fias_guid" : "",
                # "postal_code" : "",
                # "longitude" : "",
                # "latitude" : "",
                # "country_code" : "",
                # "region" : "",
                # "sub_region" : "",
                "city" : city_to,
                #"kladr_code" : "",
                "address" : adres_to
            },
            "packages" : [ {
                "number" : "bar-001",
                "comment" : comment_package,
                "height" : height,
                # "items" : [ {
                #     "ware_key" : "00055",
                #     # "payment" : {
                #     # 	"value" : 3000
                #     # },
                #     "name" : order_name,
                #     #"cost" : 300,
                #     "amount" : 1,   # кол-во мест
                #     "weight" : weight,
                #     #"url" : "www.item.ru"
                # } ],
            "length" : length,
            "weight" : weight,
            "width" : width,
            "height": height
            } ],
            "recipient" : {    # получатель
                "company": recip_company,
                "name" : recip_name,
                "tin": tin_1,
                "phones" : [ {
                "number" : recip_phone_number
            } ]
            },
            "sender" : {
                "company": sender_company, 
                "name" : sender_name,
                "type" : 2,    # тип заказа - доставка
                "phones": [
            {
                "number": sender_phones
            }
        ]
            },
            
            
            "tariff_code" : 480   # тариф: дверь в дверь ()
        }
            
                return data
        

        list_of_orders_redy = []
        list_of_orders = get_all_information('Telegram_Bot_Compas-СДЭК.csv')
        for oreder in list_of_orders:

            list_of_orders_redy.append(crete_data(oreder))
        return list_of_orders_redy
    
    datas = create_json()
    return datas


# ОШИБАЕТСЯ, ЕСЛИ СТОИТ НОМЕР КВАРТИРЫ ИЛИ ОФИСА!

# ['Ирина Кириллова', 'Ржанов Артем Владимирович', '74952155241', '16', 'magazinot@mail.ru', 'Москва', 'Нагорный проезд', '7с1', '1100', 'Макарова Екатерина Владимировна', 'ПЛАСТИКФИЛМ', '7802578575', '79001151622', '209', '170100 г. Тверь', 'ул. Красные Горки', 'д.32 стр.4', '1-30-20-8-1800-Товары ОТ #69639', 'Товары ОТ']
# ['Ирина Кириллова', 'Ржанов Артем Владимирович', '74952155241', '16', 'magazinot@mail.ru', 'Москва', 'Нагорный проезд', '7с1', '1100', 'Фурманова Алина Андреевна', 'Электротехническая группа ТОР', '5022038656', '79254851445', 'Коломна', 'Озерский проезд', '4/2', '1-30-20-12-2800-Товары ОТ #69566', 'Товары ОТ']
# ['Ирина Кириллова', 'Ржанов Артем Владимирович', '74952155241', '16', 'magazinot@mail.ru', 'Москва', 'Нагорный проезд', '7с1', '1100', 'Граборов Александр', 'СКиФ', '2469002502', '79059776821', '647000 Россия Красноярский край Таймырский Долгано-Ненецкий район г.Дудинка', 'ул. Бегичева', 'д.12', 'кв. 28', '1-28-28-20-3600-Товары ОТ #69140', 'Товары ОТ']
