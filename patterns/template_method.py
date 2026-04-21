
from abc import ABC, abstractmethod

class OrderProcessor(ABC):
    def process_order(self):
        self.validate_order()
        self.process_payment()
        self.deliver()
        self.send_confirmation()

    def validate_order(self):
        print("Validating order...")

    @abstractmethod
    def process_payment(self):
        pass

    @abstractmethod
    def deliver(self):
        pass

    def send_confirmation(self):
        print("Sending confirmation email to customer")


class OnlineOrderProcessor(OrderProcessor):
    def process_payment(self):
        print("Processing online payment (credit card / PayPal)")

    def deliver(self):
        print("Sending download link via email")


class StorePickupOrderProcessor(OrderProcessor):
    def process_payment(self):
        print("Processing payment at pickup (POS terminal)")

    def deliver(self):
        print("Preparing order for in-store pickup")

if __name__ == "__main__":
    print("=== Online Order ===")
    online = OnlineOrderProcessor()
    online.process_order()

    print("\n=== Store Pickup Order ===")
    pickup = StorePickupOrderProcessor()
    pickup.process_order()