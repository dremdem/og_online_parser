"""
Main module for serving parsers
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
    return _ParserClass()


def check_payload(payload: dict) -> bool:
    """
    Check if a response data is valid
    :param payload: data from response
    :return: True if a all attributes exists in the dict
    """
    if 'url' in payload and 'interface_id' in payload:
        return True


def parse_url(payload: dict) -> str:
    """
    Parsing url by responses data
    :param payload:
    :return: string dump of open graph JSON
    """

    result = {'errors': ''}

    try:
        data_validation = check_payload(payload)
    except:
        data_validation = False

    if not data_validation:
        result['errors'] = 'Your response date is not valid'

    parser = select_parser_by_id(payload['interface_id'])
    parser.parse(payload['url'])

    return parser.og_str_markup


def get_parsers() -> dict:
    """
    Return all parsers from DB
    :return: dict of parsers with the following structure:
    {
        <parser_id>: {
            'name': <name>,
            'description': <description>,
            'github_link': <link>
        },
        ...
    }
    """

    parsers = OGInterface.objects.all()

    parser_list = {
        p.id: {'name': p.name,
               'description': p.description,
               'github_link': p.github_link}
        for p in parsers}

    return parser_list
