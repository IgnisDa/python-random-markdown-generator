from mdgen.base.header import MarkdownHeaderGenerator
from mdgen.base.text import MarkdownTextGenerator


class MarkdownGenerator:

    def new_text(self, text: str = None):
        if not isinstance(text, (str, int)):
            raise ValueError(f"`text` must be an instance of {str} or {int}")
        output = MarkdownTextGenerator(text)
        return output.new_text()

    def new_header(self, text: str = None, header_level: int = None,
                   linebreak=True):
        if not isinstance(text, (str, int)):
            raise ValueError(f"`text` must be an instance of {str} or {int}")
        if not isinstance(header_level, (int,)):
            raise ValueError(f"`header_level` must be an instance of or {int}")
        output = MarkdownHeaderGenerator(text, header_level, linebreak)
        return output.new_header()
