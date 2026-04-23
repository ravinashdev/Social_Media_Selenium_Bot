from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from app.core.config import settings

def get_driver():
    options = Options()
    options.profile_path = settings.selenium.MOZILLA_PROFILE_PATH
    driver = webdriver.Firefox(
        service=(GeckoDriverManager().install(),),
        options=options,
    )
    return driver