class Product:
    def __init__(self, name, price, quantity):

        if not isinstance(name, str):
            raise TypeError("Name must be a text!")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number like 12.99!")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be a number like 2!")
        if name == "":
            raise ValueError("Name is empty")
        if price <= 0:
            raise ValueError("Value should be higher 0!")
        if quantity < 0:
            raise ValueError("Value should be higher 0!")
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__active = True

    def is_active(self):
        return self.__active

    def activate(self):
        self.__active = True
        return self.__active

    def deactivate(self):
        self.__active = False
        return self.__active

    def buy(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Value should be higher than 0!")
        if not self.__active:
            raise ValueError("Order not possible")
        if quantity > self.__quantity:
            raise ValueError("Not enough products in stock")
        total_buy = self.__price * quantity
        self.__quantity = self.__quantity - quantity
        return total_buy

    def set_quantity(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity < 0:
            raise ValueError("Value should be min. 0!")
        if quantity == 0:
            self.deactivate()
        elif quantity > 0:
            self.activate()
        self.__quantity = quantity
        return self.__quantity

    def get_quantity(self):
        return self.__quantity

    def show(self):
        return f"{self.__name}, Price: {self.__price}, Quantity: {self.__quantity}"
