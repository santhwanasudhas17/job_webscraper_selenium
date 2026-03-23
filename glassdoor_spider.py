from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def create_driver():
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Uncomment to run headlessly
    options.add_argument('--start-maximized')
    options.add_argument('--disable-notifications')
    driver = webdriver.Chrome(options=options)
    return driver

def login(driver):
    username = os.getenv("username")
    password = os.getenv("password")

    if not username or not password:
        raise ValueError("Set username and password environment variables.")

    url = "https://in.linkedin.com/"
    driver.get(url)

    time.sleep(7)

    driver.find_element(By.XPATH, "//a[@data-tracking-control-name='guest_homepage-basic_nav-header-signin']").click()
    time.sleep(5) 

    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@aria-label='Sign in']").click()

    input("Press Enter once login is confirmed (complete 2FA if prompted)..")
    print("Login successful.")

def run_scraper(keyword, location="India", max_jobs=10):
    driver = create_driver()

    try:
        login(driver)
        # search_jobs(driver, keyword, location)

        # job_cards = get_job_listings(driver)
        # all_jobs = []

        # for i, card in enumerate(job_cards[:max_jobs]):
        #     print(f"Scraping job {i + 1}...")
        #     details = scrape_job_details(driver, card)
        #     if details:
        #         all_jobs.append(details)

        # save_to_csv(all_jobs)

    finally:
        driver.quit()


# --- Entry point ---
if __name__ == "__main__":
    run_scraper(keyword="Data Analyst", location="Bengaluru", max_jobs=10)