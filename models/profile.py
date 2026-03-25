from dataclasses import dataclass, field
from typing import List

@dataclass
class Profile:
    name: str = ""
    headline: str = ""
    location: str = ""
    about: str = ""
    experience: List[dict] = field(default_factory=list)   # [{title, company, duration, description}]
    # education: List[dict] = field(default_factory=list)    # [{school, degree, duration}]
    # skills: List[str] = field(default_factory=list)
    profile_url: str = ""

    def to_dict(self):
        return self.__dict__