# LinkedIn Scraper

A web scraper built with Selenium that scrapes job listings, user profiles, and company pages from LinkedIn.

---

## Project Structure
```
linkedin_scraper/
│
├── main.py                  # Entry point — runs scraper from CLI
├── config.py                # All configuration and credentials
├── driver_manager.py        # Chrome browser singleton
│
├── scrapers/
│   ├── base_scraper.py      # Shared logic (login, find, text helpers)
│   ├── job_scraper.py       # Scrapes job listings by keyword
│   ├── profile_scraper.py   # Scrapes a LinkedIn profile by URL
│   └── company_scraper.py   # Scrapes a LinkedIn company page by URL
│
├── models/
│   ├── job.py               # Job dataclass
│   ├── profile.py           # Profile dataclass
│   └── company.py           # Company dataclass
│
└── utils/
    ├── file_handler.py      # Saves output to CSV and JSON
    └── helpers.py           # Utility functions
```

---

## Features

- Scrape job listings by keyword and optional location
- Scrape a LinkedIn user profile given its URL
- Scrape a LinkedIn company page given its URL
- Extracts job title, description, experience level, job type, compensation, posted date
- Extracts profile name, headline, about, experience, education, and skills
- Extracts company industry, size, headquarters, founded year, specialties, and website
- Saves output to both CSV and JSON
- Modular OOP design — each scraper runs independently
- Single shared browser session across all scrapers via Singleton pattern
- Supports 2FA — pauses for manual login confirmation

---

## Requirements

- Python 3.10+
- Google Chrome browser
- ChromeDriver (matching your Chrome version)

### Python dependencies
```
selenium
```
## Setup

**1. Clone the repository**

**2. Create and activate a virtual environment**

**3. Install dependencies**

**4. Set environment variables for LinkedIn credentials**
```bash
# Windows PowerShell
$env:username = "your_email@example.com"
$env:password = "your_password"

# macOS / Linux
export username="your_email@example.com"
export password="your_password"
```

> ⚠️ Never hardcode credentials in the source code.
> Environment variables are reset when the terminal closes.
> To persist them, set them as system-level environment variables.

---

## Usage

### Scrape Job Listings
```bash
python main.py jobs --keyword "Data Analyst"
python main.py jobs --keyword "Data Analyst" --location "Bengaluru"
python main.py jobs --keyword "Data Analyst" --location "Bengaluru" --max-jobs 20
```

**Arguments:**

| Argument | Required | Default | Description |
|---|---|---|---|
| `--keyword` | Yes | — | Job title to search for |
| `--location` | No | Anywhere | City or region to filter by |
| `--max-jobs` | No | 10 | Maximum number of jobs to scrape |

**Output:** `jobs.csv`

---

### Scrape a Profile
```bash
python main.py profile --url "https://www.linkedin.com/in/username/"
```

**Arguments:**

| Argument | Required | Description |
|---|---|---|
| `--url` | Yes | Full LinkedIn profile URL |

**Output:** `profile.json`

---

### Scrape a Company
```bash
python main.py company --url "https://www.linkedin.com/company/google/"
```

**Arguments:**

| Argument | Required | Description |
|---|---|---|
| `--url` | Yes | Full LinkedIn company URL |

**Output:** `company.json`

---
