from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount}$ with CREDIT CARD")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount}$ with PAYPAL")

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


context = PaymentContext(CreditCardPayment())
context.pay(100)

context.set_strategy(PayPalPayment())
context.pay(200)
