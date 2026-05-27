

















































class ShoppingCart:
    def __init__(self):
        self.products = {
            1: {"name": "Laptop", "price": 50000},
            2: {"name": "Mobile", "price": 20000},
            3: {"name": "Headphones", "price": 2000},
            4: {"name": "Keyboard", "price": 1500}
        }

        self.cart = []
    def show_products(self):
        print("\n------ AVAILABLE PRODUCTS ------")

        for pid, details in self.products.items():
            print(f"ID: {pid}")
            print(f"Product: {details['name']}")
            print(f"Price: ₹{details['price']}")
            print("-----------------------------")
    def add_to_cart(self):

        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter Quantity: "))

        if product_id in self.products:

            product = self.products[product_id]
            item = {
                "id": product_id,
                "name": product["name"],
                "price": product["price"],
                "quantity": quantity
            }

            self.cart.append(item)

            print(f"{product['name']} added to cart successfully!")

        else:
            print("Invalid Product ID!")

    def view_cart(self):

        if len(self.cart) == 0:
            print("\nCart is Empty!")
            return

        print("\n------ YOUR CART ------")

        total = 0

        for item in self.cart:

            subtotal = item["price"] * item["quantity"]
            total += subtotal

            print(f"Product : {item['name']}")
            print(f"Price   : ₹{item['price']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Subtotal: ₹{subtotal}")
            print("---------------------------")

        print(f"Total Amount = ₹{total}")

    def remove_from_cart(self):

        product_id = int(input("Enter Product ID to remove: "))

        for item in self.cart:

            if item["id"] == product_id:
                self.cart.remove(item)
                print(f"{item['name']} removed from cart!")
                return

        print("Product not found in cart!")
    def checkout(self):

        if len(self.cart) == 0:
            print("Cart is Empty!")
            return

        self.view_cart()

        print("\nOrder Placed Successfully!")
        print("Thank You for Shopping!")
        self.cart.clear()
shop = ShoppingCart()
while True:
    print("\n========== ONLINE SHOPPING CART ==========")
    print("1. Show Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Remove from Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        shop.show_products()
    elif choice == 2:
        shop.add_to_cart()
    elif choice == 3:
        shop.view_cart()
    elif choice == 4:
        shop.remove_from_cart()
    elif choice == 5:
        shop.checkout()
    elif choice == 6:
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice!")