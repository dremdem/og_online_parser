"""
Test for all routes
"""

from rest_framework.test import APIClient


def test_get_json_by_url(test_parser_id) -> None:
    """
    Test parse route
    :param test_parser_id: fixture for populating test DB
    """
    client = APIClient()
    response = client.post('/parse/',
                           {'url': 'http://www.youtube.com', 'interface_id': '1'}, format='json')
    assert response.status_code == 200
    assert type(response.data) == str


def test_parsers(test_parser_id) -> None:
    """
    Test parse route
    :param test_parser_id: fixture for populating test DB
    """
    client = APIClient()
    response = client.get('/parsers/')
    assert response.status_code == 200
    assert type(response.data) == list


def test_last_n_urls(test_last_urls) -> None:
    """
    Test last_urls route
    :param test_last_urls: fixture for populating test DB with last urls
    """
    client = APIClient()
    response = client.get('/last_urls/')
    assert response.status_code == 200
    assert type(response.data) == dict


