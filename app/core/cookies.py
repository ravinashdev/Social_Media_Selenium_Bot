class CookieManager:
    def __init__(self, driver):
        self.driver = driver
    def load(self, site, url):
        import os
        import pickle
        path = f"cookies/{site}.pkl"
        # Must open domain first
        self.driver.get(url)
        if not os.path.exists(path):
            print(f"⚠️ No cookies for {site}")
            return False
        with open(path, "rb") as f:
            cookies = pickle.load(f)
        for c in cookies:
            try:
                if "expiry" in c:
                    c["expiry"] = int(c["expiry"])
                self.driver.add_cookie(c)
            except Exception as e:
                print(f"Skipping cookie: {e}")
        self.driver.refresh()
        print(f"✅ Cookies loaded for {site}")
        return True

    def save(self, site):
        import pickle, os
        os.makedirs("cookies", exist_ok=True)
        path = f"cookies/{site}.pkl"
        with open(path, "wb") as f:
            pickle.dump(self.driver.get_cookies(), f)
        print(f"💾 Cookies saved for {site}")