class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__active = True
        if not isinstance(name, str):
            raise ValueError("Name must be a text!")
        if not isinstance(price, float):
            raise ValueError("Price must be a number like 12.99!")
        if not isinstance(quantity, int):
            raise ValueError("Quantity must be a number like 2!")

    def is_active(self):
        if self.__active:
            return True
        else:
            return False

    def buy(self, quantity):
        total_buy = self.__price * quantity
        self.__quantity = self.__quantity + quantity
        return total_buy

    def set_quantity(self, quantity):
        if self.__quantity - quantity <= 0:
            self.__active = False
        self.__quantity = self.__quantity + quantity


    def show(self):
        print(f"{self.__name}, Price: {self.__price}, Quantity: {self.__quantity}")

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250.00, quantity=500)
    mac = Product("MacBook Air M2", price=1450.00, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()