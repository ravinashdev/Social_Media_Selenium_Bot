from app.core.config import settings
# Waiting classes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# print(settings.as_dict())
class TwitterClient:
    def __init__(self, driver):
        self.driver = driver
        self.username = settings.twitter.USERNAME
        self.password = settings.twitter.PASSWORD
        self.base_url = settings.twitter.BASE_URL
    def login(self):
        self.driver.get(self.base_url)
        print("Logging into Twitter")
