class Ecommerce:
    def __init__(self):
        self.cart = []
        self.order_history = []
    def add_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        product = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.cart.append(product)
        print("Product added successfully")
    def remove_product(self):
        name = input("Enter product name to remove: ")
        found = False
        for product in self.cart:
            if product["name"] == name:
                self.cart.remove(product)
                found = True
                print("Product removed")
                break
        if found == False:
            print("Product not found")
    def update_quantity(self):
        name = input("Enter product name: ")
        quantity = int(input("Enter new quantity: "))
        found = False
        for product in self.cart:
            if product["name"] == name:
                product["quantity"] = quantity
                found = True
                print("Quantity updated")
                break
        if found == False:
            print("Product not found")
    def view_cart(self):
        total_bill = 0
        print("\n----- CART ITEMS -----")
        for product in self.cart:
            total = product["price"] * product["quantity"]
            total_bill = total_bill + total
            print(
                product["name"],
                "| Price:", product["price"],
                "| Quantity:", product["quantity"],
                "| Total:", total
            )
        print("\nTotal Bill =", total_bill)
    def generate_bill(self):
        total_bill = 0
        for product in self.cart:
            total = product["price"] * product["quantity"]
            total_bill = total_bill + total
        discount = 0
        if total_bill >= 5000:
            discount = total_bill * 0.20
        elif total_bill >= 2000:
            discount = total_bill * 0.10
        final_amount = total_bill - discount
        print("\n----- BILL -----")
        print("Total Bill =", total_bill)
        print("Discount =", discount)
        print("Final Amount =", final_amount)
        self.order_history.append(final_amount)
    def view_history(self):
        print("\n----- ORDER HISTORY -----")
        for order in self.order_history:
            print("Order Amount =", order)
obj = Ecommerce()
while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. Update Quantity")
    print("4. View Cart")
    print("5. Generate Bill")
    print("6. View Order History")
    print("7. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        obj.add_product()
    elif choice == 2:
        obj.remove_product()
    elif choice == 3:
        obj.update_quantity()
    elif choice == 4:
        obj.view_cart()
    elif choice == 5:
        obj.generate_bill()
    elif choice == 6:
        obj.view_history()
    elif choice == 7:
        print("Thank You")
        break
    else:
        print("Invalid choice")