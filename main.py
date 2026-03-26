import argparse
from driver_manager import DriverManager
from scrapers.job_scrapper import JobScraper
from scrapers.profile_scrapper import ProfileScraper
from scrapers.company_scrapper import CompanyScraper
from utils.file_handler import FileHandler

def run_job_scraper(args):
    scraper = JobScraper()
    scraper.login()
    jobs = scraper.scrape(
        keyword=args.keyword,
        location=args.location or "",
        max_jobs=args.max_jobs)
    FileHandler.save_csv([j.to_dict() for j in jobs], "jobs.csv")
    # FileHandler.save_json([j.to_dict() for j in jobs], "jobs.json")

def run_profile_scraper(args):
    scraper = ProfileScraper()
    scraper.login()
    profile = scraper.scrape(args.url)
    FileHandler.save_json(profile.to_dict(), "profile.json")

def run_company_scraper(args):
    scraper = CompanyScraper()
    scraper.login()
    company = scraper.scrape(args.url)
    FileHandler.save_json(company.to_dict(), "example/company.json")

def main():
    parser = argparse.ArgumentParser(description="LinkedIn Scraper", formatter_class=argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers(dest="command", required=True, help="Which scraper to run")

    # ---- Job Scraper ----
    job_parser = subparsers.add_parser("job", help="Scrape job listings")
    job_parser.add_argument("--keyword", required=True, help="Job title or keywords to search for")
    job_parser.add_argument("--location", default="", help="Location to search for jobs (optional)")
    job_parser.add_argument("--max-jobs", type=int, default=10, help="Maximum number of jobs to scrape (max is 25)")

    # ---- Profile Scraper ----
    profile_parser = subparsers.add_parser("profile", help="Scrape a LinkedIn profile")
    profile_parser.add_argument("--url", required=True, help="URL of the LinkedIn profile to scrape")

    # ---- Company Scraper ----
    company_parser = subparsers.add_parser("company", help="Scrape a LinkedIn company page")
    company_parser.add_argument("--url", required=True, help="URL of the LinkedIn company page to scrape")

    args = parser.parse_args()

    try:
        if args.command == "job":
            run_job_scraper(args)
        elif args.command == "profile":
            run_profile_scraper(args)
        elif args.command == "company":
            run_company_scraper(args)
    except Exception as e:
        print(f"An error occurred: {e}")
    # finally:
    #     DriverManager.get_instance().quit()

if __name__ == "__main__":
    main()