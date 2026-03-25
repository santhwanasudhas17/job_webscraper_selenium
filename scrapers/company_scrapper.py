from selenium.webdriver.common.by import By
from scrapers.base_scraper import BaseScraper
from models.company import Company

class CompanyScraper(BaseScraper):
    def scrape(self, company_url: str) -> Company:
        print(f"Scraping company: {company_url}")
        about_url = company_url + "about/"

        company = Company()
        company.company_url = company_url
        company.name = self._text(By.XPATH, "//h1[contains(@class,'org-top-card-summary__title')]")
        company.about = self._text(By.XPATH, "//div[@class='org-about-module__description']/div/span[1]")

        print(f"Company scraped: {company.name}")
        return company
