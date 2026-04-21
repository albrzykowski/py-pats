class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current_index = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.max_count:
            raise StopIteration

        if self.current_index == 0:
            self.current_index += 1
            return 0
        elif self.current_index == 1:
            self.current_index += 1
            return 1

        next_value = self.a + self.b
        self.a, self.b = self.b, next_value

        self.current_index += 1
        return next_value

if __name__ == "__main__":
    fib = FibonacciIterator(10)

    for number in fib:
        print(number)