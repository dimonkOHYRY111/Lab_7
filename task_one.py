def print_all(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")


def add_magazine(dictionary, name, price, circulation):
    dictionary[name] = {"price": price, "circulation": circulation}
    print(f"Журнал '{name}' успішно додано.")


def remove_magazine(dictionary, name):
    if name in dictionary:
        del dictionary[name]
        print(f"Журнал '{name}' успішно видалено.")
    else:
        print(f"Журнал '{name}' не знайдено.")


def sorted_keys(dictionary):
    for key in sorted(dictionary.keys()):
        print(f"{key}: {dictionary[key]}")


def average_price(dictionary):
    total_price = 0
    count = 0
    for magazine, data in dictionary.items():
        if data["circulation"] < 10000:
            total_price += data["price"]
            count += 1
    if count > 0:
        avg_price = total_price / count
        print(f"Середня вартість журналів з тиражем менше 10 000: {avg_price:.2f}")
    else:
        print("Журналів з тиражем менше 10 000 не знайдено.")


magazines = {
    "Magazine A": {"price": 12.50, "circulation": 15000},
    "Magazine B": {"price": 8.75, "circulation": 9000},
    "Magazine C": {"price": 5.50, "circulation": 5000},
    "Magazine D": {"price": 10.25, "circulation": 12000},
    "Magazine E": {"price": 7.80, "circulation": 8000}
}

print("Всі журнали:")
print_all(magazines)

add_magazine(magazines, "Magazine F", 9.40, 7500)

remove_magazine(magazines, "Magazine A")

print("\nВсі журнали:")
print_all(magazines)

print("\nЖурнали за відсортованими ключами:")
sorted_keys(magazines)

average_price(magazines)