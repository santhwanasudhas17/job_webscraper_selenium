from dataclasses import dataclass, field
from typing import List

@dataclass
class Company:
    name: str = ""
    industry: str = ""
    headquarters: str = ""
    size: str = ""
    founded: str = ""
    specialties: str = ""
    about: str = ""
    website: str = ""
    company_url: str = ""

    def to_dict(self):
        return self.__dict__