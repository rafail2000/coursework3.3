from scripts.scripts import load_data, five_items, correct_date, account_of_sender


def main():
    data = load_data()
    five_operation = five_items(data)
    for item in five_operation:
        print(f'{correct_date(item["date"])} {item.get("description")}')
        print(f'{account_of_sender(item)}')







if __name__ == "__main__":
    main()