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
