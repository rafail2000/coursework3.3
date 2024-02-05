from scripts.scripts import load_data, five_items, correct_date, account_of_sender


def test_load_data():
    assert load_data() is not None


def test_five_items():
    assert five_items(load_data()) != 5

def test_correct_date():
    assert correct_date("2018-06-30T02:08:58.425572") == "30.06.2018"

def test_account_of_sender():
    assert account_of_sender({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }) == "Maestro 159683******5199"
