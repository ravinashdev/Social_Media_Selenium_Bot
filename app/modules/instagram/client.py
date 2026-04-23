from app.core.config import settings
# Waiting classes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# print(settings.as_dict())
class InstagramClient:
    def __init__(self, driver):
        self.driver = driver
        self.username = settings.instagram.USERNAME
        self.password = settings.instagram.PASSWORD
        self.base_url = settings.instagram.BASE_URL
    def login(self):
        self.driver.get(self.base_url)
        print("Logging into Instagram")