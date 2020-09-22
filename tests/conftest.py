import pytest

from mdgen.markdown import MarkdownGenerator


@pytest.fixture()
def markdown_generator():

    def _markdown_generator(*args, **kwargs):
        return MarkdownGenerator(*args, **kwargs)

    return _markdown_generator
