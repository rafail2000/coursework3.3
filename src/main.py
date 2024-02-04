from scripts.scripts import load_data, five_items, correct_date, discription_transfert


def main():
    data = load_data()
    five_operation = five_items(data)
    print(discription_transfert(five_operation))
    for item in five_operation:
        print(f'{correct_date(item["date"])} {discription_transfert(item["description"])}')








if __name__ == "__main__":
    main()