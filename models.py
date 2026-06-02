class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity, price):
        if name in self.products:
            self.products[name]["quantity"] += quantity
        else:
            self.products[name] = {
                "quantity": quantity,
                "price": price
            }

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(f"{name} беше премахнат.")
        else:
            print("Продуктът не съществува.")

    def show_products(self):
        if not self.products:
            print("Няма налични продукти.")
            return

        print("\nСкладова наличност:")
        for name, data in self.products.items():
            print(
                f"Продукт: {name} | "
                f"Количество: {data['quantity']} | "
                f"Цена: {data['price']} евро."
            )