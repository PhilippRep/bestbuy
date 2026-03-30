from products import Product

class Store:

    def __init__(self, product_list):
        if not isinstance(product_list, list):
            raise TypeError("Must be a list of Product!")
        if not product_list:
            raise ValueError("Store is empty!")
        for product in product_list:
            if not isinstance(product, Product):
                raise TypeError("Only Product objects allowed")
        self.product_list = product_list.copy()

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects allowed")
        self.product_list.append(product)

    def remove_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects allowed")
        if product not in self.product_list:
            raise ValueError("Product not in Store!")
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
        if not isinstance(shopping_list, list):
            raise TypeError("Shopping list must be a list")
        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise TypeError("Only Product objects are allowed!")
            if not isinstance(quantity, int):
                raise TypeError("Only integers as quantity are allowed")
            if not product.is_active():
                raise ValueError("Product is not active")
            if quantity <= 0:
                raise ValueError("quantity must be higher than 0")
            total_price += product.buy(quantity)
        return total_price



