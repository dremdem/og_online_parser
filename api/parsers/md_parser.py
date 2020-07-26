"""
Meta parser from https://github.com/jvanasco/metadata_parser
"""

from api.parsers.base_parser import BaseInterfaceParser
import metadata_parser


class MetaParser(BaseInterfaceParser):
    def parse(self, url: str) -> dict:
        page = metadata_parser.MetadataParser(url=url)
        self.json_markup = page.metadata
        return self.og_str_markup
