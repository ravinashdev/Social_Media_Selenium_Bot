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
class InstagramClient:
    def __init__(self, driver):
        self.driver = driver
        self.username = settings.instagram.USERNAME
        self.password = settings.instagram.PASSWORD
        self.base_url = settings.instagram.BASE_URL
        self.wait = WebDriverWait(self.driver, 10)
    def is_logged_in(self, driver):
        return "login" not in self.driver.current_url
    def login(self):
        self.driver.get(self.base_url)
        # Login
        login_email_box = self.wait.until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        login_email_box.send_keys(self.username)
        login_password_box = self.wait.until(
            EC.presence_of_element_located((By.NAME, "pass"))
        )
        login_password_box.send_keys(self.password)
        login_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Log in']"))
        )
        login_button.click()
        input(" Please solve Captcha then press <Enter> to proceed")
        print("Logging into Instagram")
    def post(self,message):
        new_post_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/create')]"))
        )
        new_post_button.click()
