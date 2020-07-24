import pytest

from api.models import OGInterface


@pytest.fixture
def test_parser_id(db) -> int:
    meta_parser = OGInterface(name='metadata_parser',
                              description='python library for getting metadata',
                              module_name='md_parser',
                              class_name='MetaParser',
                              github_link='github_link')
    meta_parser.save()

    return meta_parser.id
