class OldPaymentSystem:
    def make_payment(self, amount):
        print(f"Paid {amount}$ using OLD system")

class PaymentProcessor:
    def pay(self, amount):
        pass

class PaymentAdapter(PaymentProcessor):
    def __init__(self, old_system):
        self.old_system = old_system

    def pay(self, amount):
        self.old_system.make_payment(amount)


def process_payment(processor: PaymentProcessor):
    processor.pay(100)


old_system = OldPaymentSystem()
adapter = PaymentAdapter(old_system)

process_payment(adapter)
