class State:
    def pay(self, order):
        raise NotImplementedError()

    def ship(self, order):
        raise NotImplementedError()

    def cancel(self, order):
        raise NotImplementedError()


class NewState(State):
    def pay(self, order):
        order.set_state(PaidState())

    def ship(self, order):
        raise Exception("Cannot ship unpaid order")

    def cancel(self, order):
        order.set_state(CancelledState())


class PaidState(State):
    def pay(self, order):
        raise Exception("Already paid")

    def ship(self, order):
        order.set_state(ShippedState())

    def cancel(self, order):
        order.set_state(CancelledState())


class ShippedState(State):
    def pay(self, order):
        raise Exception("Already shipped")

    def ship(self, order):
        raise Exception("Already shipped")

    def cancel(self, order):
        raise Exception("Cannot cancel shipped order")


class CancelledState(State):
    def pay(self, order):
        raise Exception("Order cancelled")

    def ship(self, order):
        raise Exception("Order cancelled")

    def cancel(self, order):
        raise Exception("Already cancelled")


class Order:
    def __init__(self):
        self.state = NewState()

    def set_state(self, state):
        self.state = state

    def pay(self):
        self.state.pay(self)

    def ship(self):
        self.state.ship(self)

    def cancel(self):
        self.state.cancel(self)


order = Order()
order.pay()
# order.cancel()
order.ship()
print(type(order.state).__name__)
