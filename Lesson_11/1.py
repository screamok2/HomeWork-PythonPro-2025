from datetime import datetime, timedelta
import queue
import threading
import time
import random

OrderRequestBody = tuple[str, datetime]


storage = {
    "users": [],
    "delivery" :["uklon", "uber"],
    "dishes": [
        {
            "id": 1,
            "name": "Salad",
            "value": 1099,
            "restaurant": "Silpo",
        },
        {
            "id": 2,
            "name": "Soda",
            "value": 199,
            "restaurant": "Silpo",
        },
        {
            "id": 3,
            "name": "Pizza",
            "value": 599,
            "restaurant": "Kvadrat",
        },
    ],
    # ...
}


class Scheduler:
    def __init__(self):
        self.orders: queue.Queue[OrderRequestBody] = queue.Queue()

    def process_orders(self) -> None:

        print("SCHEDULER PROCESSING...")

        while True:
            order = self.orders.get(True)

            time_to_wait = order[1] - datetime.now()

            if time_to_wait.total_seconds() > 0:
                self.orders.put(order)
                time.sleep(0.5)
            else:

                print(f"\n\t{order[0]} SENT TO SHIPPING DEPARTMENT")

                dd.add_order(order)

    def add_order(self, order: OrderRequestBody) -> None:
        self.orders.put(order)
        print(f"\n\t{order[0]} ADDED FOR PROCESSING")

class Delivery :
    def __init__(self):
        self.delivery_queue : queue.Queue[OrderRequestBody] = queue.Queue()
        self.delivery_providers = storage["delivery"]

    def add_order(self, order: OrderRequestBody) -> None:
        self.delivery_queue.put(order)
        print(f"Order  {order[0]}  get by SHIPPING DEPARTMENT")


    def delivery (self):
        print(f"DELIVERY........")
        while True:
            deliv = self.delivery_queue.get(True)


            print(f"{deliv[0]} delivered BY {self.select_delivery_provider()}")


    def select_delivery_provider(self):
        provider  = random.choice(self.delivery_providers)
        if provider == "uklon":
            time.sleep(5)

        if provider == "uber":
            time.sleep(3)

        return provider

dd = Delivery()
def main():
    scheduler = Scheduler()
    thread = threading.Thread(target=scheduler.process_orders, daemon=True)
    thread.start()

    thread1 = threading.Thread(target=dd.delivery, daemon=True)
    thread1.start()


    # user input:
    # A 5 (in 5 days)
    # B 3 (in 3 days)
    while True:
        order_details = input("Enter order details: ")
        data = order_details.split(" ")
        order_name = data[0]
        delay = datetime.now() + timedelta(seconds=int(data[1]))
        scheduler.add_order(order=(order_name, delay))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        raise SystemExit(0)