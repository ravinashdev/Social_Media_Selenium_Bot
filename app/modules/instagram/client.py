from app.core.config import settings

class InstagramClient:
    def __init__(self, driver):
        self.driver = driver
        self.username = settings.instagram.USERNAME
        self.password = settings.instagram.PASSWORD
    def login(self):
        print("Logging into Instagram")