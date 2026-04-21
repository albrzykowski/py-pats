from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"[LOG]: {message}")

class NullLogger(Logger):
    def log(self, message: str):
        # Do nothing
        pass


class PaymentService:
    def __init__(self, logger: Logger):
        self.logger = logger

    def process_payment(self, amount: float):
        self.logger.log(f"Starting payment: {amount}")

        if amount <= 0:
            self.logger.log("Invalid amount!")
            return False

        self.logger.log("Payment processed successfully")
        return True

if __name__ == "__main__":
    print("=== With real logger ===")
    service_with_logs = PaymentService(ConsoleLogger())
    service_with_logs.process_payment(100)

    print("\n=== With null logger ===")
    service_without_logs = PaymentService(NullLogger())
    service_without_logs.process_payment(100)