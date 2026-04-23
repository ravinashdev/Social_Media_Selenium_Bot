from app.core.config import settings

class TwitterClient:
    def __init__(self, driver):
        self.driver = driver
        self.username = settings.twitter.USERNAME
        self.password = settings.twitter.PASSWORD
        self.base_url = settings.twitter.BASE_URL
    def login(self):
        print("Logging into Twitter")
    def scrape_profile(self, username):
        print(f"Scraping {username}")