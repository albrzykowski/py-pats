class Mediator:
    def notify(self, sender, event, data=None):
        pass


class OrderMediator(Mediator):
    def __init__(self):
        self.payment = None
        self.inventory = None
        self.notification = None

    def notify(self, sender, event, data=None):
        if event == "order_created":
            if self.inventory.reserve(data):
                self.payment.process(data)
            else:
                self.notification.send("Out of stock")

        elif event == "payment_success":
            self.notification.send("Order completed")

        elif event == "payment_failed":
            self.inventory.release(data)
            self.notification.send("Payment failed")


class Component:
    def __init__(self, mediator):
        self.mediator = mediator


class Inventory(Component):
    def __init__(self, mediator):
        super().__init__(mediator)
        self.stock = {"item": 2}

    def reserve(self, order):
        item = order["item"]
        if self.stock.get(item, 0) > 0:
            self.stock[item] -= 1
            return True
        return False

    def release(self, order):
        item = order["item"]
        self.stock[item] += 1


class Payment(Component):
    def process(self, order):
        if order.get("valid", True):
            self.mediator.notify(self, "payment_success", order)
        else:
            self.mediator.notify(self, "payment_failed", order)


class Notification(Component):
    def send(self, message):
        print(message)


mediator = OrderMediator()

inventory = Inventory(mediator)
payment = Payment(mediator)
notification = Notification(mediator)

mediator.inventory = inventory
mediator.payment = payment
mediator.notification = notification

order = {"item": "item", "valid": True}

mediator.notify(None, "order_created", order)
