import pytest
from faker import Faker
from mdgen import (MarkdownGenerator, MarkdownOutputGenerator,
                   MarkdownPostProvider)


@pytest.fixture()
def markdown_generator():

    def _markdown_generator(*args, **kwargs):
        return MarkdownGenerator(*args, **kwargs)

    return _markdown_generator


@pytest.fixture()
def markdown_output_generator():

    def _markdown_output_generator(*args, **kwargs):
        return MarkdownOutputGenerator(*args, **kwargs)

    return _markdown_output_generator


@pytest.fixture()
def fake_post_faker(faker):

    def _fake_post_faker(*args, **kwargs):
        fake = Faker()
        fake.add_provider(MarkdownPostProvider)
        return fake

    return _fake_post_faker()
