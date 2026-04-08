class PaymentGateway:
    def charge(self, amount):
        print(f"Charging {amount}$")

class InventoryService:
    def reserve(self, item_id):
        print(f"Reserving item {item_id}")

class EmailService:
    def send_confirmation(self):
        print("Sending confirmation email")

class OrderFacade:
    def __init__(self):
        self.payment = PaymentGateway()
        self.inventory = InventoryService()
        self.email = EmailService()

    def place_order(self, item_id, amount):
        self.inventory.reserve(item_id)
        self.payment.charge(amount)
        self.email.send_confirmation()

facade = OrderFacade()
facade.place_order(item_id=123, amount=49.99)
