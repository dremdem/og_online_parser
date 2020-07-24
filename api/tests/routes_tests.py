from rest_framework.test import APIClient


def test_get_json_by_url(test_parser_id):
    client = APIClient()
    response = client.post('/parse/',
                           {'url': 'http://www.youtube.com', 'interface_id': '1'}, format='json')
    assert response.status_code == 200
    assert type(response.data) == dict
