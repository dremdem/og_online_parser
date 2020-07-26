"""
Describes base class for parser interface
"""
import json


class BaseInterfaceParser:
    json_markup = {}

    def parse(self, url: str) -> dict:
        """
        Parse html-page by url and return OG-dict
        Also you should to store OG mark as JSON to json_markup variable
        :param url:
        :return: dict with all OG attributes
        """
        raise NotImplementedError

    @property
    def og_str_markup(self):
        """
        Return OG markup as pretty printed str
        """
        return json.dumps(self.json_markup, indent=4, ensure_ascii=False)
