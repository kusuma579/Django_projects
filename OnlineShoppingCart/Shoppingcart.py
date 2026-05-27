class ShoppingCart:
    def __init__(self, ProductName=None, Price=None, Quantity=None):
        self.__ProductName = ProductName
        self.__Price = Price
        self.__Quantity = Quantity
    def get_product_name(self):
        return self.__ProductName
    def get_price(self):
        return self.__Price
    def get_quantity(self):
        return self.__Quantity
    def set_product_name(self, name):
        self.__ProductName = name
    def set_price(self, price):
        self.__Price = price
    def set_quantity(self, quantity):
        self.__Quantity = quantity
    def add_product(self):
        product_name = input("Enter product name: ")
        product_price = float(input("Enter product price: "))
        product_quantity = int(input("Enter product quantity: "))
        product_obj = ShoppingCart(
            product_name,
            product_price,
            product_quantity
        )
        cart_data.append(product_obj)
        print("Product added successfully!")
    def view_products(self):
        print("\n----- CART PRODUCTS -----")
        total_bill = 0
        for data in cart_data:
            total = data.get_price() * data.get_quantity()
            total_bill = total_bill + total
            print(
                "Product Name: ", data.get_product_name(), "\n",
                "Product Price: ", data.get_price(), "\n",
                "Product Quantity: ", data.get_quantity(), "\n",
                "Total: ", total
            )
        print("\nTotal Bill =", total_bill)
    def delete_product(self):
        product_name = input("Enter product name to delete: ")
        found = False
        for data in cart_data:
            if data.get_product_name() == product_name:
                cart_data.remove(data)
                found = True
                print("Product deleted successfully!")
                break
        if found == False:
            print("Product not found!")
    def update_product(self):
        product_name = input("Enter product name to update: ")
        found = False
        for data in cart_data:
            if data.get_product_name() == product_name:
                new_quantity = int(input("Enter new quantity: "))
                data.set_quantity(new_quantity)
                found = True
                print("Quantity updated successfully!")
                break
        if found == False:
            print("Product not found!")
    def generate_bill(self):
        total_bill = 0
        for data in cart_data:
            total = data.get_price() * data.get_quantity()
            total_bill = total_bill + total
        discount = 0
        if total_bill >= 5000:
            discount = total_bill * 0.20
        elif total_bill >= 2000:
            discount = total_bill * 0.10
        final_amount = total_bill - discount
        print("\n----- FINAL BILL -----")
        print("Total Bill: ", total_bill)
        print("Discount: ", discount)
        print("Final Amount: ", final_amount)
if __name__ == "__main__":
    print("WELCOME TO SHOPPING CART SYSTEM")
    cart_data = list()
    shopping_cart = ShoppingCart()
    while True:
        print("\n1. Add Product\n"
              "2. View Products\n"
              "3. Delete Product\n"
              "4. Update Quantity\n"
              "5. Generate Bill\n"
              "6. Exit")
        option = input("Enter your choice: ")
        if option == "1":
            shopping_cart.add_product()
        elif option == "2":
            shopping_cart.view_products()
        elif option == "3":
            shopping_cart.delete_product()
        elif option == "4":
            shopping_cart.update_product()
        elif option == "5":
            shopping_cart.generate_bill()
        elif option == "6":
            print("Thank You!")
            break
        else:
            print("Please enter a valid choice")


