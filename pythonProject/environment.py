import os


class Environment:
    DEV = 'dev'
    PROD = 'prod'

    URLS = {
        DEV: "https://website.dev2.pochtomat.team/",
        PROD: "https://pochtomat.ru/"
    }

    def __init__(self):
        try:
            self.env = os.environ['ENV']
        except KeyError:
            self.env = self.DEV

    def get_base_url(self):
        if self.env in self.URLS:
            return self.URLS[self.env]
        else:
            raise Exception(f"Can't find ENV value{self.env}")


ENV_OBJECT = Environment()