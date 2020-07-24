from api.parsers.base_parser import BaseInterfaceParser
import metadata_parser


class MetaParser(BaseInterfaceParser):
    def parse(self, url: str) -> dict:
        page = metadata_parser.MetadataParser(url=url)
        return page.metadata

