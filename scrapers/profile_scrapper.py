from selenium.webdriver.common.by import By
from scrapers.base_scraper import BaseScraper
from models.profile import Profile
from typing import List

class ProfileScraper(BaseScraper):

    def _parse_experience(self) -> str:
        entries = []
        items = self._find_all(By.Xpath, "//section[contains(@componentkey,'ExperienceTopLevelSection')]//div[contains(@componentkey, 'entity-collection-item')]")

        for item in items:
            entries.append({
                "title": self._safe_text(item, By.Xpath, "//a[not(@componentkey)]/div/div/div/p[1]"),
                "company": self._safe_text(item, By.Xpath, "//a[not(@componentkey)]/div/div/div/p[2]"),
                "duration": self._safe_text(item, By.Xpath, "//a[not(@componentkey)]/div/div/following-sibling::p[1]"),
            })

        return entries

    # def _parse_skills(self) -> List[str]:
    #     items = self._find_all(By.Xpath, "")
    #     return [i.text.strip()for i in items if i.text.strip()]
    
    def _safe_text(self,parent,xpath: str, default="N/A") -> str:
        try:
            return parent.find_element(By.XPATH,xpath).text.strip()
        except:
            return default
        
    def scrape(self, profile_url: str) -> Profile:
        print(f"Scraping profile: {profile_url}")
        self._get(profile_url)

        profile = Profile()
        profile.profile_url = profile_url
        profile.name = self._text(By.XPATH, "//section//a//h2")
        profile.headline = self._text(By.XPATH, "//div[@aria-haspopup='dialog']/parent::div/following-sibling::p[1]")
        profile.location = self._text(By.XPATH, "//div[@aria-haspopup='dialog']/parent::div/following-sibling::div/p[1]")
        profile.about = self._text(By.XPATH, "//section[contains(@componentkey, 'About')]")
        profile.experience = self._parse_experience()
        # profile.skills = self._parse_skills()
        # profile.education = self._text(By.XPATH, "")
        print(f"Scraped profile: {profile.name}")
        return profile
