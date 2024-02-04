from scripts.scripts import load_data, five_items, correct_date


def main():
    data = load_data()
    items = five_items(data)
    for item in items:
        print(correct_date(item))






if __name__ == "__main__":
    main()