"""
Main module for serving parsers
"""

from api.parsers.parser_selector import select_parser_by_id


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

    _ParserClass = select_parser_by_id(payload['interface_id'])
    parser = _ParserClass(payload['interface_id'])

    return parser.parse(payload['url'])



