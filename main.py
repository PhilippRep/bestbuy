"""Programm of a shop where you can take a look to all of the articles
which are active in the shop.
You can see also the total amount of the articles and it´s also possible to take a
order for more articles for the shop
"""

import products
import store

def list_all_products(store_obj):
    """Get all articles from Store class and print an overview"""
    counter = 1
    print("------")
    active_products = store_obj.get_all_products()
    length = len(active_products)
    if length == 0:
        print("Shop is empty")
        print("------")
    else:
        for prod in active_products:
            print(f"{counter}. ", end="")
            prod.show()
            counter += 1
        print("------")

def show_total_amount(store_obj):
    """The total amount of alle articles is count in Store class and
    here it shows the total amount of all articles in the shop
    """
    total_quantity = store_obj.get_total_quantity()
    print(f"Total of {total_quantity} items in store")

def make_an_order(store_obj, prod):
    """
    If now articles in the shop you get a message that you can´t take an order.
    otherwise get the articles from Store class and i can choose
    which article and which amount i want to order. i can fill my shpping list
    without a border. When i finish my order i get the total costs for the order.
    """
    active_products = store_obj.get_all_products()
    length = len(active_products)
    if length == 0:
        print("Shop is empty. No order is possible!")
    else:
        shopping_list = []
        list_all_products(store_obj)
        print("When you want to finish order, enter empty text.")
        while True:
            try:
                take_an_order = input("Which product # do you want? ")
                how_many = input("What amount do you want? ")
                if take_an_order == "" and how_many == "":
                    break
                shopping_list.append((prod[(int(take_an_order)) - 1], (int(how_many))))
                print("Product added to list!\n")
                continue
            except ValueError:
                print("Error adding product!")

        total_costs = store_obj.order(shopping_list)
        print(f"\nOrder made! Total payments: ${total_costs:.2f}")

def start(store_obj, product_list):
    """Shows the start menu where the user can take a choice
    what want to see or to exit the program"""
    while True:
        print("\n   Store Menu\n"
              "   __________\n\n"
              "1. List all products in store\n"
              "2. Show total amount in store\n"
              "3. Make an order\n"
              "4. Quit")
        try:
            choice = int(input("Please choose a number: "))
            if choice == 1:
                list_all_products(store_obj)
                continue
            if choice == 2:
                show_total_amount(store_obj)
                continue
            if choice == 3:
                make_an_order(store_obj, product_list)
                continue
            if choice == 4:
                break
        except ValueError:
            print("Error with your choice! Try again!")
            continue

def main():
    """list all the products and have the connection
    to Store class and start the menu
    """
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450.0, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250.0, quantity=500),
                 products.Product("Google Pixel 7", price=500.9, quantity=250)
                ]
    best_buy = store.Store(product_list)
    start(best_buy, product_list)

if __name__ == "__main__":
    main()