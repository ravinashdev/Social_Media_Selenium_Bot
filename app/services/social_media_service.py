from app.core.driver import get_driver
from app.modules.twitter.client import TwitterClient
from app.modules.instagram.client import InstagramClient

class SocialMediaService:
    def run(self):
        driver = get_driver()
        twitter = TwitterClient(driver)
        instagram = InstagramClient(driver)
        twitter.login()
        instagram.login()