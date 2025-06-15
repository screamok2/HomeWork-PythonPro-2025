import mysql.connector
import datetime



connection_payload = {
    'host' : "localhost",
    'user' : "root",
    'password' : "0712880Rjkz",
    'database' : "catering"
}
conn = mysql.connector.connect (**connection_payload)


if conn.is_connected():
    print("connected")

class User:
    name: str
    phone: str
    role: str
    id: int | None = None

    def all_users(self):
        cursor = conn.cursor()
        cursor.execute("SELECT * from users;")
        users = cursor.fetchall()
        for i  in users:
            print(i)
    def add_user(self, name, phone, role):
        self.name = name
        self.phone = phone
        self.role = role
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, phone, role) VALUES (%s, %s, %s)",(self.name, self.phone, self.role))
        conn.commit()
    def delete_user(self,id):
        self.id = id
        cursor = conn.cursor()
        cursor.execute("SELECT * from users WHERE id = %s;",(self.id,))
        user = cursor.fetchone()
        if user:
            cursor.execute("DELETE FROM users WHERE id = %s;",(self.id,))
            conn.commit()
            print(f"User with ID {self.id} deleted")
        else:
            print("user not found")
    def update_user(self,id):
        self.id = id
        cursor = conn.cursor()
        cursor.execute("SELECT * from users WHERE id = %s;", (self.id,))
        user = cursor.fetchone()
        print(user)
        if user:
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            new_role = input("Enter new role: ")
            cursor.execute("UPDATE users SET name = %s, phone = %s, role = %s WHERE id = %s;",
                           (new_name, new_phone, new_role, self.id))
            conn.commit()
            print(f"USER {user[1]} updated")
            print(user)
        else:
            print("user not found")
    def show_users(self):
        item = input("Enter the role or name: ")
        if item == "USER" or "ADMIN":
            cursor = conn.cursor()
            cursor.execute("SELECT * from users WHERE role = %s;", (item,))
            users = cursor.fetchall()
            for i  in users:
                print(i)
        if item == "ALL":
            user.all_users()

        else:
            cursor = conn.cursor()
            cursor.execute("SELECT * from users WHERE name = %s;", (item,))
            users = cursor.fetchall()
            for i in users:
                print(i)
    def delete_all(self):
        item = input("Enter the role: ")
        if item == "USER" or "ADMIN":
            cursor = conn.cursor()
            cursor.execute("SELECT * from users WHERE role = %s;", (item,))
            users = cursor.fetchall()
            confirmation = input("Y/N??")
            if confirmation == "Y":
                for i in users:
                    cursor.execute("DELETE FROM users WHERE role = %s;", (item,))
                    conn.commit()
                print("all users deleted")
            else:
                print("Deleting canceled")

class Dish:
    name: str
    price: int
    id: int | None = None

    def all_diches(self):
        cursor = conn.cursor()
        cursor.execute("SELECT * from dishes;")
        dishes = cursor.fetchall()
        for i in dishes:
            print(i)

    def add_dishes(self, name, price):
        self.name = name
        self.price = price
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dishes (name, price) VALUES (%s, %s)",(self.name, self.price))
        conn.commit()

    def delete_dish(self,id):
        self.id = id
        cursor = conn.cursor()
        cursor.execute("SELECT * from dishes WHERE id = %s;", (self.id,))
        dish = cursor.fetchone()
        if dish:
            cursor.execute("DELETE FROM dishes WHERE id = %s;", (self.id,))
            conn.commit()
            print(f"Dish with ID {self.id} deleted")
        else:
            print("Dish not found")

    def update_dish(self,id):
        self.id = id
        cursor = conn.cursor()
        cursor.execute("SELECT * from dishes WHERE id = %s;", (self.id,))
        dish = cursor.fetchone()
        print(dish)
        if dish:
            new_name = input(" Enter new name: ")
            new_price = input(" Enter new price: ")
            cursor = conn.cursor()
            cursor.execute("UPDATE dishes SET name = %s,price = %s WHERE id = %s;", (new_name, new_price, self.id))
            conn.commit()
        else:
            print("Dish not found")

    def show_dishes(self):
        item = str(input("Enter the key: "))
        cursor = conn.cursor()
        cursor.execute("SELECT * from dishes WHERE name = %s;", (item,))
        dishes = cursor.fetchall()
        for i in dishes:
            print(i)

class Order:
    user_id: int
    date: str
    total: float
    status: str
    id: int | None = None

    def all_orders(self):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM orders;")
        orders = cursor.fetchall()
        for order in orders:
            print(order)

    def add_order(self, user_id, total, status):
        self.user_id = user_id
        self.total = total
        self.status = status
        cursor = conn.cursor()
        now = datetime.datetime.now()
        cursor.execute(
            "INSERT INTO orders (user_id, data, total, status) VALUES (%s, %s, %s, %s);",
            (self.user_id, now, self.total, self.status)
        )
        conn.commit()

    def delete_order(self, id):
        self.id = id
        cursor = conn.cursor()
        cursor.execute("DELETE FROM orders WHERE id = %s;", (self.id,))
        conn.commit()
        print(f"Order with ID {self.id} deleted")

    def update_order(self, id):
        self.id = id
        new_status = input("Enter new status: ")
        cursor = conn.cursor()
        cursor.execute("UPDATE orders SET status = %s WHERE id = %s;", (new_status, self.id))
        conn.commit()

    def show_orders_by_user(self, user_id):
        cursor = conn.cursor()
        cursor.execute( "SELECT * FROM users WHERE id = %s;", (user_id,))
        user = cursor.fetchone()
        print(f"{user}")
        cursor.execute("SELECT * FROM orders WHERE user_id = %s;", (user_id,))
        orders = cursor.fetchall()
        for order in orders:
            print(order)

class OrderItem:
    order_id: int
    dish_id: int
    quantity: int
    id: int | None = None

    def all_order_items(self):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM order_items;")
        items = cursor.fetchall()
        for item in items:
            print(item)

    def add_order_item(self, order_id, dish_id, quantity):
        self.order_id = order_id
        self.dish_id = dish_id
        self.quantity = quantity
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO order_items (order_id, dish_id, quantity) VALUES (%s, %s, %s);",
            (self.order_id, self.dish_id, self.quantity)
        )
        conn.commit()

    def delete_order_item(self, id):
        self.id = id
        cursor = conn.cursor()
        cursor.execute("DELETE FROM order_items WHERE id = %s;", (self.id,))
        conn.commit()
        print(f"Order item with ID {self.id} deleted")

    def update_order_item(self, id):
        self.id = id
        new_quantity = input("Enter new quantity: ")
        cursor = conn.cursor()
        cursor.execute("UPDATE order_items SET quantity = %s WHERE id = %s;", (new_quantity, self.id))
        conn.commit()

    def show_items_by_order(self, order_id):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM order_items WHERE order_id = %s;", (order_id,))
        items = cursor.fetchall()
        for item in items:
            print(item)


user = User()

#user.add_user("ADMIN", "6665465464","ADMIN")
#user.delete_user("10")
#user.update_user("1")
#user.show_users()
#user.all_users()
#user.delete_all()

dish = Dish()
#dish.add_dishes("salsa", "20")
#dish.delete_dish("23")
#dish.update_dish("23")
#dish.all_diches()
#dish.show_dishes()

order = Order()

#order.add_order("4", '50', 'PENDING')
#order.delete_order("1")
#order.show_orders_by_user("1")

#order.all_orders()

