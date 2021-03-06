"""
Python Open Graph parser from https://github.com/HenrikOssipoff/python-opengraph
"""

from api.parsers.base_parser import BaseInterfaceParser
from opengraph import OpenGraph


class HOParser(BaseInterfaceParser):
    def parse(self, url: str) -> dict:
        og = OpenGraph(url=url)
        self.json_markup = og.__data__
        return self.og_str_markup
