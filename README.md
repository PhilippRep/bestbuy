# 🛒 Simple Store System

A small object-oriented Python program that simulates a shop where users can view products, check stock, and place orders.

---

## 📦 Features

- View all **active products** in the store
- Display total quantity of all products
- Place orders with multiple products
- Automatic stock reduction after purchase
- Input validation with proper error handling
- Clean separation between `Product`, `Store`, and user interface

---

## 🧱 Project Structure


.
├── products.py # Product class (logic for individual items)
├── store.py # Store class (manages product list & orders)
└── main.py # User interface / program entry point


---

## 🧩 Classes Overview

### 📦 Product

Represents a single product in the store.

**Attributes:**
- `name`
- `price`
- `quantity`
- `active` (indicates if product is available)

**Key Methods:**
- `buy(quantity)` → reduces stock and returns total price  
- `set_quantity(quantity)` → updates stock and activation status  
- `activate()` / `deactivate()` → control product availability  
- `is_active()` → checks if product is available  
- `get_quantity()` → returns current stock  
- `show()` → returns product information as a string  

---

### 🏬 Store

Manages a collection of products and handles orders.

**Key Methods:**
- `add_product(product)` → adds a product to the store  
- `remove_product(product)` → removes a product  
- `get_all_products()` → returns only active products  
- `get_total_quantity()` → total stock across all products  
- `order(shopping_list)` → processes an order and returns total cost  

---

## 🛍️ How Ordering Works

1. The program displays all **active products**
2. The user selects:
   - product number
   - quantity
3. Multiple items can be added to the shopping list
4. Enter **empty input twice** to finish the order
5. The total price is calculated and displayed

---

## ▶️ How to Run

Make sure you have Python installed, then run:

```bash
python main.py
⚠️ Input Rules
Product must exist in the list
Quantity must be a positive integer
Only active products can be ordered
Empty input (twice) ends the order
🛠️ Design Notes
Uses encapsulation (__private attributes)
Clear separation of responsibilities:
Product → handles item logic
Store → handles collection & orders
main.py → user interaction
Includes proper error handling (TypeError, ValueError)
🚀 Possible Improvements
Save/load inventory from file or database
Add user accounts
Improve UI (e.g., GUI or web app)
Add discounts or promotions
Add unit tests
👨‍💻 Author

Created as a learning project to practice:

Object-Oriented Programming (OOP)
Input validation
Program structure and design
📜 License

This project is for educational purposes.