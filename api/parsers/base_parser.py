"""
Describes base class for parser interface
"""
from api.models import OGInterface


class BaseInterfaceParser:
    def __init__(self, parser_id: int):
        parser = OGInterface.objects.get(pk=parser_id)
        self.name = parser.name
        self.description = parser.description
        self.github_link = parser.github_link

    def parse(self, url: str) -> dict:
        """
        Parse html-page by url and return OG-dict
        :param url:
        :return: dict with all OG attributes
        """
        raise NotImplementedError
