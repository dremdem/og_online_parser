from api.parsers.parser_selector import select_parser_by_id
from api.parsers.base_parser import BaseInterfaceParser


def test_select_parser_by_id(test_parser_id):
    parser_class = select_parser_by_id(test_parser_id)
    assert isinstance(parser_class, BaseInterfaceParser)
