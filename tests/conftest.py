import pytest
from mdgen import MarkdownGenerator, MarkdownOutputGenerator


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
