class Product:
    def __init__(self, name, price, quantity):
        if not isinstance(name, str):
            raise ValueError("Name must be a text!")
        if not isinstance(price, float):
            raise ValueError("Price must be a number like 12.99!")
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be a number like 2!")
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__active = True

    def is_active(self):
        return self.__active

    def buy(self, quantity):
        total_buy = self.__price * quantity
        self.__quantity = self.__quantity + quantity
        return total_buy

    def set_quantity(self, quantity):
        if self.__quantity - quantity <= 0:
            self.__active = False
        self.__quantity = self.__quantity + quantity
        return self.__quantity

    def get_quantity(self):
        return self.__quantity


    def show(self):
        print(f"{self.__name}, Price: {self.__price}, Quantity: {self.__quantity}")
