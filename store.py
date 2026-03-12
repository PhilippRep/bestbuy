from products import Product

class Store:

    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        self.product_list.append(product)

    def remove_product(self, product):
        self.product_list.remove(product)

    def get_total_quantity(self):
        total = 0
        for product in self.product_list:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        active_products = []
        for item in self.product_list:
            if item.is_active():
                active_products.append(item)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


def main():
    product_list = [Product("MacBook Air M2", price=1450.0, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250.0, quantity=500),
                    Product("Google Pixel 7", price=500.0, quantity=250),
                    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(active_products[0], 1), (active_products[1], 2)]))
if __name__ == "__main__":
    main()


