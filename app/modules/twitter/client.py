# Config
from app.core.config import settings
# Waiting classes
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Selection Classes
from selenium.webdriver.common.by import By
# Keyboard
from selenium.webdriver.common.keys import Keys
# print(settings.as_dict())
class TwitterClient:
    def __init__(self, driver):
        self.driver = driver
        self.username = settings.twitter.USERNAME
        self.password = settings.twitter.PASSWORD
        self.base_url = settings.twitter.BASE_URL
        self.wait = WebDriverWait(self.driver, 10)
    def login(self):
        landing_page = self.driver.get(self.base_url)
        # # Click Login Button
        # login_button = self.wait.until(
        #     EC.presence_of_element_located((By.XPATH, "//span[text()='Sign in']"))
        # )
        # login_button.click()
        # # Input email address
        # username_field = self.wait.until(
        #     EC.visibility_of_element_located((By.NAME, "text"))
        # )
        # username_field.send_keys(self.username)
        # input(" Please log in manually in the browser, then press ENTER here...")
        # print("Logging into Twitter")
