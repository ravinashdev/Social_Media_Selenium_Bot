# Driver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
# Config
from app.core.config import settings
# Cookies
from app.core.cookies import CookieManager


def get_driver():
    options = Options()
    options.add_argument("-profile")
    options.add_argument(settings.selenium.MOZILLA_PROFILE_PATH)
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference("useAutomationExtension", False)
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options,
    )
    # Initialize cookie manager AFTER driver exists
    cookie_manager = CookieManager(driver)
    # Try loading cookies
    if not cookie_manager.load("instagram", "https://instagram.com"):
        input("👉 Log in manually to Instagram, then press ENTER...")
        cookie_manager.save("instagram")
    return driver
