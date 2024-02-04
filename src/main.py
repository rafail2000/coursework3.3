from scripts.scripts import load_data, five_items, correct_date


def main():
    data = load_data()
    five_operation = five_items(data)
    for item in five_operation:
        print(correct_date(item['date']))








if __name__ == "__main__":
    main()