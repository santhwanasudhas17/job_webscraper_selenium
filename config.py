import os

class Config:
    username = os.getenv("username")
    password = os.getenv("password")

    url = "https://in.linkedin.com/"

    IMPLICIT_WAIT = 10
    PAGE_LOAD_WAIT = 5
    HEADLESS = False  

    @classmethod
    def validate(cls):
        if not cls.username or not cls.password:
            raise ValueError("Set username and password environment variables.")