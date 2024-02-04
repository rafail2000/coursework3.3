from scripts.scripts import sort_transactions, five_items, time_correct, get_from
from utils.read_json_file import load_data


def main():
    data = load_data()
    ex_items = get_transactions(data)
    sort_items = sort_transactions(ex_items)
    items = five_items(sort_items)
    for item in items:
        print(time_correct(item["date"]), item["discription"])
        print(get_from(item), get_to(item))
        print(get_money(item))





if __name__ == "__main__":
    main()