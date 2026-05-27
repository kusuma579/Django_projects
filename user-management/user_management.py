






































class UserManagement:
    def __init__(self):
        self.users = []
    def add_user(self, username, email, address, phone, gender):
        for user in self.users:
            if user["email"] == email:
                print("User with this email already exists!")
                return
        user = {
            "username": username,
            "email": email,
            "address": address,
            "phone": phone,
            "gender": gender
        }
        self.users.append(user)
        print("User added successfully!")
    def view_users(self):
        if len(self.users) == 0:
            print("No users found!")
            return
        print("\n--- User Details ---")
        for user in self.users:
            print(f"""
Username : {user['username']}
Email    : {user['email']}
Address  : {user['address']}
Phone    : {user['phone']}
Gender   : {user['gender']}
--------------------------
""")
    def update_user(self, email):
        for user in self.users:
            if user["email"] == email:
                print("Enter new details:")
                user["username"] = input("New Username : ")
                user["address"] = input("New Address  : ")
                user["phone"] = input("New Phone    : ")
                user["gender"] = input("New Gender   : ")
                print("User updated successfully!")
                return
        print("User not found!")
    def delete_user(self, email):
        for user in self.users:
            if user["email"] == email:
                self.users.remove(user)
                print("User deleted successfully!")
                return

        print("User not found!")
obj = UserManagement()

while True:
    print("\n===== USER MANAGEMENT SYSTEM =====")
    print("1. Add User")
    print("2. View Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        username = input("Enter Username : ")
        email = input("Enter Email    : ")
        address = input("Enter Address  : ")
        phone = input("Enter Phone    : ")
        gender = input("Enter Gender   : ")

        obj.add_user(username, email, address, phone, gender)

    elif choice == 2:
        obj.view_users()

    elif choice == 3:
        email = input("Enter email to update user: ")
        obj.update_user(email)

    elif choice == 4:
        email = input("Enter email to delete user: ")
        obj.delete_user(email)

    elif choice == 5:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
