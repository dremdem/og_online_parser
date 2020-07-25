import pytest

from django.core.management import call_command

from api.models import OGInterface


@pytest.fixture
def test_parser_id(db) -> int:
    """
    Fixture for populating a parsing interface to a test database
    :return: parser_id
    """
    meta_parser = OGInterface(name='metadata_parser',
                              description='python library for getting metadata',
                              module_name='md_parser',
                              class_name='MetaParser',
                              github_link='https://github.com/jvanasco/metadata_parser')
    meta_parser.save()

    return meta_parser.id


@pytest.fixture
def test_last_urls(db) -> None:
    fixtures = ['urlhistory.json']

    for fixture in fixtures:
        call_command('loaddata', fixture)


