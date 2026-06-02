from models import Inventory

inventory = Inventory()

while True:
    print("\n===== СКЛАДОВА НАЛИЧНОСТ =====")
    print("1. Добави продукт")
    print("2. Изтрий продукт")
    print("3. Покажи всички продукти")
    print("4. Изход")

    choice = input("Изберете опция: ")

    if choice == "1":
        name = input("Име на продукт: ")
        quantity = int(input("Количество: "))
        price = float(input("Цена: "))

        inventory.add_product(name, quantity, price)
        print("Продуктът е добавен успешно.")

    elif choice == "2":
        name = input("Име на продукт за изтриване: ")
        inventory.remove_product(name)

    elif choice == "3":
        inventory.show_products()

    elif choice == "4":
        print("Край на програмата.")
        break

    else:
        print("Невалиден избор.")