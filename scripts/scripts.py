import json
from pprint import pprint

from config import PATH
from datetime import datetime


def load_data():
    '''Загружает json файл с данными EXECUTED'''
    with open(PATH, encoding='UTF-8') as read_data:
        data = json.load(read_data)
        operation_list = []
        for operation in data:
            if operation.get("state") == "EXECUTED":
                operation_list.append(operation)
        return operation_list


def five_items(sort_items):
    '''Отображает пять последних транзакций в списке'''
    sort_list = sorted(sort_items, key=lambda x: datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f"),
                       reverse=True)
    last_five = sort_list[:5]
    return last_five


def correct_data(value):
    '''Выыод даты в требуемом формате'''
    date_list = []
    for data in value:
        date = datetime.strptime(data['date'], "%Y-%m-%dT%H:%M:%S.%f")
        date_format = f'{date:%d.%m.%Y}'
        date_list.append(date_format)
    return date_list


def discription_transfert(description):
    '''Описание перевода'''
    transfert_data = []
    for data in description:
        resault = data["description"]
        transfert_data.append(resault)
    return transfert_data


def departure_account(account):
    '''Данные отправителя'''
    encrypted_account = []
    for data in account:
        account_list = data.get("from")
        if data == "NoneType":
            continue
        else:
            encrypted_account.append(account_list[:-10] + '*' * 6 + account_list[-4:])

    return encrypted_account
pprint(departure_account(load_data()))

def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]


def get_from(items):
    '''Шифрование счёта отправителя'''
    pass

