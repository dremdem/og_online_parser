"""
Select parser by ID
"""
import importlib

from api.models import OGInterface
from api.parsers.base_parser import BaseInterfaceParser


def select_parser_by_id(parser_id: int) -> BaseInterfaceParser:
    """
    Retrieve the parser's module and class names from the DB
    :param parser_id: ID of a parse
    :return: Parser class
    """
    parser = OGInterface.objects.get(pk=parser_id)
    parser_module = importlib.import_module(f'api.parsers.{parser.module_name}')
    _ParserClass = getattr(parser_module, parser.class_name)
    return _ParserClass(parser_id)
