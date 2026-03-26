from selenium.webdriver.common.by import By
from scrapers.base_scraper import BaseScraper
from models.company import Company

class CompanyScraper(BaseScraper):
    def scrape(self, company_url: str) -> Company:
        print(f"Scraping company: {company_url}")
        about_url = company_url + "about/"
        self._get(about_url)
        self._scroll_to_bottom()
        self._scroll_to_top()

        company = Company()
        company.company_url = company_url
        input("Page loaded. Press enter after inspecting")
        if self._elements(By.XPATH, "//h1"):
            company.name = self._text(By.XPATH, "//h1/text()[1]")
            print(f"Company name found: {company.name}")
        else:
            print("Company name not found.")
        if self._elements(By.XPATH, "//section[contains(@class,'org-about-module__margin-bottom')]/p[1]"):
            company.about = self._text(By.XPATH, "//section[contains(@class,'org-about-module__margin-bottom')]/p[1]")
            print(f"Company about found.")
        else:
            print("Company about not found.")
        #didn't scrape industry, headquarters, size, founded, specialties, website. Need to check the XPATH for these fields and update the code accordingly.
        print(f"Company scraped: {company.name}")
        return company
