from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import Config

class DriverManager:
    _instance = None  # Singleton — one driver across all scrapers

    def __init__(self):
        self.driver = self._create_driver()
    
    # To open same browser
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def _create_driver(self):
        options = Options()
        if Config.HEADLESS:
            options.add_argument('--headless')
        # options.add_argument('--start-maximized')
        options.add_argument('--disable-notifications')
        options.add_argument('--disable-blink-features=AutomationControlled') #Hides Selenium automation signals from websites
        options.add_experimental_option("excludeSwitches", ["enable-automation"]) #Removes the "Chrome is being controlled by automated software" message
        return webdriver.Chrome(options=options)

    # To close the browser so that in future same browser is not used
    def quit(self):
        if self.driver:
            self.driver.quit()
            DriverManager._instance = None
