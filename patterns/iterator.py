from typing import List

class Order:
    def __init__(self, order_id: int, amount: float, is_paid: bool):
        self.order_id = order_id
        self.amount = amount
        self.is_paid = is_paid

    def __repr__(self):
        status = "PAID" if self.is_paid else "UNPAID"
        return f"Order(id={self.order_id}, amount={self.amount}, {status})"


class PaidOrdersIterator:
    def __init__(self, orders: List[Order]):
        self._orders = orders
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self._index < len(self._orders):
            current = self._orders[self._index]
            self._index += 1

            if current.is_paid:
                return current

        raise StopIteration


class OrderRepository:
    def __init__(self):
        self._orders: List[Order] = []

    def add_order(self, order: Order):
        self._orders.append(order)

    def get_paid_orders(self):
        return PaidOrdersIterator(self._orders)

if __name__ == "__main__":
    repo = OrderRepository()

    repo.add_order(Order(1, 100, True))
    repo.add_order(Order(2, 50, False))
    repo.add_order(Order(3, 200, True))

    print("Paid orders:")
    for order in repo.get_paid_orders():
        print(order)