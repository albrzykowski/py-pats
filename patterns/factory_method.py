from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending EMAIL: {message}")

class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass

    def notify(self, message):
        notification = self.create_notification()
        notification.send(message)

class EmailFactory(NotificationFactory):
    def create_notification(self):
        return EmailNotification()

class SMSFactory(NotificationFactory):
    def create_notification(self):
        return SMSNotification()


def client_code(factory: NotificationFactory):
    factory.notify("Hello world!")

client_code(EmailFactory())
client_code(SMSFactory())
