"""
Main module for serving parsers
"""

import importlib

from django.conf import settings

from api.models import OGInterface, UrlHistory
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


def add_last_url(url: str) -> None:
    """
    Add the last url to the history
    :param url: url string
    """

    # if this url will be found, then updated_at date will be updated
    UrlHistory.objects.update_or_create(url=url)


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

    add_last_url(payload['url'])

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


def get_last_n_urls() -> dict:
    """
    Return last N urls from the DB sorted by updated date from new to old
    """

    last_urls = UrlHistory.objects.all().order_by('-updated_at')[:settings.LAST_N_URLS]
    list_last_urls = {url.id: url.url for url in last_urls}

    return list_last_urls
