from dataclasses import dataclass, field
from typing import Optional

# dataclass to avoid boilerplate code (__init__) for job attributes
@dataclass
class Job:
    title: str = ""
    company: str = ""
    location: str = ""
    description: str = ""
    experience: str = ""
    compensation: str = ""
    job_type: str = ""        # Full-time, Part-time, Contract etc.
    posted_date: str = ""
    job_url: str = ""

    def to_dict(self):
        return self.__dict__