class UserManagement:
    def __init__(self,UserName=None,Email=None,Address=None,Phone=None,Gender=None):
        self.__UserName = UserName
        self.__Email = Email
        self.__Address = Address
        self.__Phone = Phone
        self.__Gender = Gender

    #getter method
    def get_user_name(self):
        return self.__UserName
    def get_email(self):
        return self.__Email
    def get_address(self):
        return self.__Address
    def get_phone(self):
        return self.__Phone
    def get_gender(self):
        return self.__Gender

    def set_user_name(self,name):
        self.__UserName = name
    def set_email(self,email):
        self.__Email = email
    def set_address(self,address):
        self.__Address = address
    def set_phone(self,phone):
        self.__Phone = phone
    def set_gender(self,gender):
        self.__Gender = gender
    def add_user(self):
        user_name=input("Enter your name: ")
        user_email=input("Enter your email: ")
        address=input("Enter your address: ")
        phone=input("Enter your phone: ")
        gender=input("Enter your gender: ")
        user_obj=UserManagement(user_name,user_email,address,phone,gender)
        user_data.append(user_obj)
        print("User added successfully!")

    def view_users(self):
        print("\n--- User Details ---")
        for data in user_data:
            print("user_name: ", data.get_user_name() ,"\n" 
                  "user email: ",data.get_email(),"\n"
                  "User address: ",data.get_address(),"\n"
                  "User phone: ",data.get_phone(),"\n"
                  "User gender: ",data.get_gender())
    def delete_user(self):

        email = input("Enter your email: ")

        for data in user_data:

            if data.get_email() == email:
                user_data.remove(data)
                print("User deleted successfully!")
                return

        print("User not found!")


    def update_user(self):

        email = input("Enter your email: ")

        for data in user_data:

            if data.get_email() == email:

                print("Enter new details:")

                new_name = input("New Username : ")
                new_address = input("New Address  : ")
                new_phone = input("New Phone    : ")
                new_gender = input("New Gender   : ")

                data.set_user_name(new_name)
                data.set_address(new_address)
                data.set_phone(new_phone)
                data.set_gender(new_gender)

                print("User updated successfully!")
                return

        print("User not found!")



"""user_management = UserManagement()
user_management.set_user_name("ram")
print(user_management.get_user_name())

user_management1 = UserManagement("amar")
print(user_management1.get_user_name())

user_data=[]
print(user_data.append("ravi"))
print(user_data)
user_management2 = UserManagement(UserName="ravi",Email="",Address="123 Main Street")
user_management3=UserManagement()
user_management3.add_user()
print(user_management3.get_user_name())"""


if __name__ == "__main__":
    print("welcome to code:  ")
    user_data=list()
    user_management=UserManagement()
    while True:
        print("1. add user\n"
              "2. view users\n"
              "3. delete user\n"
              "4.update user\n"
              "5. exit")
        option=input("Enter your choice: ")
        if option=="1":
            user_management.add_user()
        elif option=="2":
            user_management.view_users()
        elif option=="3":
            user_management.delete_user()
        elif option=="4":
            user_management.update_user()
        elif option=="5":
            break
        else:
            print("please enter a valid choice")




