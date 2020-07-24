"""
Test utils
"""

from api.parsers.utils import select_parser_by_id, get_parsers
from api.parsers.base_parser import BaseInterfaceParser


def test_select_parser_by_id(test_parser_id) -> None:
    """
    Test for parser selector
    :param test_parser_id: fixture for populating test DB
    """
    parser_class = select_parser_by_id(test_parser_id)
    assert isinstance(parser_class, BaseInterfaceParser)


def test_get_parsers(test_parser_id) -> None:
    all_parsers = get_parsers()
    assert type(all_parsers) == list
