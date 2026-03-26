import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from scrapers.base_scraper import BaseScraper
from models.job import Job
from typing import List

class JobScraper(BaseScraper):
    def search(self, keyword: str, location: str = ""):
        self._get(f"{self._base_url()}jobs/")

        keyword_input = self._find(By.XPATH, "//input[@data-testid='typeahead-input']")

        if keyword_input:
            keyword_input.clear()
            keyword_input.send_keys(keyword)
            time.sleep(1)
            keyword_input.send_keys(Keys.ENTER)
        
        if location:
            location_input = self._find(By.XPATH, "")
            if location_input:
                location_input.clear()
                location_input.send_keys(location)
        
        # search_btn = self._find(By.XPATH, "")
        # if search_btn:
        #     search_btn.click()
        # time.sleep(5) 
    
    def _base_url(self):
        from config import Config
        return Config.url

    def _get_job_cards(self) -> list:
        return self._find_all(By.XPATH, "//div[@componentkey='SearchResultsMainContent']/div/div[@style]")
    
    def _parse_job(self, card) -> Job:
        job = Job()
        try:
            card.click()  # Open job details
            time.sleep(3)  # Wait for details to load
            job.title = self._text(By.XPATH, "//div[@data-component-type='LazyColumn']//p/a[@data-original-url]")
            job.company = self._text(By.XPATH, "//div[@data-component-type='LazyColumn']//p/a[contains(@href,'/company/')]")
            job.location = self._text(By.XPATH, "(//div[@data-component-type='LazyColumn' and @componentkey]//p/span[@class='_4bbc6e71'])[1]")
            job.description = self._text(By.XPATH, "//div[contains(@componentkey,'JobDetails_AboutTheJob')]//span[@data-testid='expandable-text-box']")
            # job.experience = self._text(By.XPATH, "")
            # job.compensation = self._text(By.XPATH, "")
            job.job_type = self._text(By.XPATH, "((//div[@data-component-type='LazyColumn' and @componentkey])[2]//a[contains(@href,'/search-results/?currentJobId')])[1]")
            # job.posted_date = self._text(By.XPATH, "")
            job.job_url = self.driver.current_url
        except Exception as e:
            print(f"Error parsing job card: {e}")
        return job
    
    def scrape(self, keyword: str, location: str = "", max_jobs: int = 10) -> List[Job]:
        print(f"Searching jobs: '{keyword}' in '{location or 'Anywhere'}'")
        self.search(keyword, location)

        cards = self._get_job_cards()
        jobs = []

        for i, card in enumerate(cards[:max_jobs]):
            print(f"  Scraping job {i + 1}/{min(max_jobs, len(cards))}...")
            job = self._parse_job(card)
            jobs.append(job)

        print(f"Scraped {len(jobs)} jobs.")
        return jobs