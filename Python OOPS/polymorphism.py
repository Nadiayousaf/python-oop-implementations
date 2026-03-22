class EmailNotification:
    def send(self, message):
        print(f"Email sent: {message}")


class SMSNotification:
    def send(self, message):
        print(f"SMS sent: {message}")


class WhatsAppNotification:
    def send(self, message):
        print(f"WhatsApp sent: {message}")


# Polymorphism in action
notifications = [
    EmailNotification(),
    SMSNotification(),
    WhatsAppNotification()
]

for n in notifications:
    n.send("Hello User")