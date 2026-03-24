import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_manager import DriverManager
from config import Config

class BaseScraper:
    def __init__(self):
        self.driver = DriverManager.get_instance().driver
        self.wait = WebDriverWait(self.driver, Config.WAIT_TIME)

    def _get(self, url):
        self.driver.get(url)
        time.sleep(Config.PAGE_LOAD_WAIT)

    def _find(self, by: By, value: str):
        try:
            return self.wait.until(EC.presence_of_element_located((by, value)))
        except:
            return None
    
    def _find_all(self, by: By, value: str):
        try:
            return self.driver.find_elements(by, value)
        except:
            return []
    
    def _text(self, by: By, value: str, default="N/A"):
        element = self._find(by, value)
        return element.text.strip() if element else default
    
    def login(self):
        Config.validate()
        self._get(f"{Config.url}")

        self._find(By.XPATH, "//a[@data-tracking-control-name='guest_homepage-basic_nav-header-signin']").click()
        time.sleep(5)
         
        self._find(By.ID, "username").send_keys(Config.username)
        self._find(By.ID, "password").send_keys(Config.password)
        self._find(By.XPATH, "//button[@aria-label='Sign in']").click()

        input("Press Enter once login is confirmed (complete 2FA if prompted)..")
        print("Login successful.")
    
    def scrape(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement this method.")